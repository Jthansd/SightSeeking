import json

from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db import transaction
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token


# ============================================================
# HELPERS
# ============================================================

def get_token_user(request):
    """Return the user for the request's "Authorization: Token <key>"
    header, or None if the header is missing or the token is invalid."""

    scheme, _, key = request.headers.get("Authorization", "").partition(" ")

    if scheme != "Token" or not key:
        return None

    token = Token.objects.select_related("user").filter(key=key).first()

    if token is None or not token.user.is_active:
        return None

    return token.user


def user_json(user):
    return {
        "id": user.id,
        "username": user.username,
        "email": user.email,
    }


def error(message, status=400):
    return JsonResponse({"error": message}, status=status)


def read_json(request):
    try:
        return json.loads(request.body)
    except json.JSONDecodeError:
        return None


# ============================================================
# REGISTER - create an account and log in
# ============================================================

@csrf_exempt
def register(request):
    if request.method != "POST":
        return error("Method not allowed.", 405)

    data = read_json(request)

    if data is None:
        return error("Invalid JSON.")

    username = str(data.get("username", "")).strip()
    email = str(data.get("email", "")).strip()
    password = str(data.get("password", ""))

    if not username or not email or not password:
        return error("Username, email, and password are required.")

    User = get_user_model()

    try:
        # Same rules Django uses for usernames: letters, digits, @/./+/-/_
        User.username_validator(username)
    except ValidationError:
        return error(
            "Usernames may only contain letters, numbers, and @ . + - _"
        )

    if len(username) > 150:
        return error("Username must be 150 characters or fewer.")

    try:
        validate_email(email)
    except ValidationError:
        return error("Please enter a valid email address.")

    # Case-insensitive, so "Jonathan" and "jonathan" can't both exist.
    if User.objects.filter(username__iexact=username).exists():
        return error("That username is already taken.")

    if User.objects.filter(email__iexact=email).exists():
        return error("An account with that email already exists.")

    # Runs the AUTH_PASSWORD_VALIDATORS from settings.py
    # (minimum length, too common, all numbers, too similar to username).
    try:
        validate_password(password, user=User(username=username, email=email))
    except ValidationError as e:
        return error(" ".join(e.messages))

    # All or nothing: if the token can't be created, don't keep the account.
    with transaction.atomic():
        # create_user hashes the password; the plain text is never stored.
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )

        token = Token.objects.create(user=user)

    return JsonResponse(
        {"token": token.key, "user": user_json(user)},
        status=201,
    )


# ============================================================
# LOGIN - check username/password and return a token
# ============================================================

@csrf_exempt
def login(request):
    if request.method != "POST":
        return error("Method not allowed.", 405)

    data = read_json(request)

    if data is None:
        return error("Invalid JSON.")

    username = str(data.get("username", "")).strip()
    password = str(data.get("password", ""))

    if not username or not password:
        return error("Username and password are required.")

    # Let people log in regardless of capitalization.
    User = get_user_model()
    match = User.objects.filter(username__iexact=username).first()

    user = authenticate(
        request,
        username=match.username if match else username,
        password=password,
    )

    if user is None:
        return error("Incorrect username or password.", 401)

    token, _ = Token.objects.get_or_create(user=user)

    return JsonResponse({"token": token.key, "user": user_json(user)})


# ============================================================
# LOGOUT - delete the token so it can't be used again
# ============================================================

@csrf_exempt
def logout(request):
    if request.method != "POST":
        return error("Method not allowed.", 405)

    user = get_token_user(request)

    if user is not None:
        Token.objects.filter(user=user).delete()

    return JsonResponse({"message": "Logged out."})


# ============================================================
# ME - who is logged in? (used when the site loads)
# ============================================================

def me(request):
    if request.method != "GET":
        return error("Method not allowed.", 405)

    user = get_token_user(request)

    if user is None:
        return error("Not logged in.", 401)

    return JsonResponse({"user": user_json(user)})
