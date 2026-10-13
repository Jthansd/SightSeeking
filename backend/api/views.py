import json

from django.contrib.auth import get_user_model
from django.db import connection, transaction
from django.http import JsonResponse
from django.utils.dateparse import parse_datetime
from django.views.decorators.csrf import csrf_exempt

from .models import Animal_Sighting, Sighting, Species


def health(request):
    return JsonResponse({"status": "ok"})


def members(request):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT id, first_name, last_name, grade_in_years "
            "FROM members ORDER BY id"
        )

        columns = [col[0] for col in cursor.description]
        rows = [dict(zip(columns, row)) for row in cursor.fetchall()]

    return JsonResponse(rows, safe=False)


@csrf_exempt
def sightings(request):

    # ========================================================
    # GET - Return all sightings
    # ========================================================

    if request.method == "GET":
        with connection.cursor() as cursor:
            cursor.execute(
                '''
                SELECT
                    s.id,
                    s.user_id,
                    s.sighting_type,
                    s.timestamp,
                    s.description,
                    s."locationLongitude",
                    s."locationLatitude",
                    s.observed_at,
                    s.animal_count,
                    s.behavior,
                    s.notes,
                    a.common_name
                FROM api_sighting s
                LEFT JOIN api_animal_sighting a
                    ON a.sighting_id = s.id
                ORDER BY s.id DESC
                '''
            )

            columns = [col[0] for col in cursor.description]

            rows = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]

        return JsonResponse(rows, safe=False)

    # ========================================================
    # POST - Create a new sighting
    # ========================================================

    if request.method == "POST":
        try:
            data = json.loads(request.body)

            species_name = data.get("species", "").strip()
            latitude = data.get("latitude")
            longitude = data.get("longitude")
            observed_at = parse_datetime(
                data.get("observedAt", "")
            )

            animal_count = int(
                data.get("animalCount", 1)
            )

            behavior = data.get(
                "behavior",
                ""
            )

            notes = data.get(
                "notes",
                ""
            ).strip()

            # ------------------------------------------------
            # Validation
            # ------------------------------------------------

            if not species_name:
                return JsonResponse(
                    {
                        "error":
                        "Species is required."
                    },
                    status=400
                )

            if latitude in (None, ""):
                return JsonResponse(
                    {
                        "error":
                        "Latitude is required."
                    },
                    status=400
                )

            if longitude in (None, ""):
                return JsonResponse(
                    {
                        "error":
                        "Longitude is required."
                    },
                    status=400
                )

            if observed_at is None:
                return JsonResponse(
                    {
                        "error":
                        "A valid observation date and time is required."
                    },
                    status=400
                )

            if animal_count < 1:
                return JsonResponse(
                    {
                        "error":
                        "Animal count must be at least 1."
                    },
                    status=400
                )

            valid_behaviors = {
                choice[0]
                for choice in Sighting.Behavior.choices
            }

            if behavior and behavior not in valid_behaviors:
                return JsonResponse(
                    {
                        "error":
                        "Invalid behavior."
                    },
                    status=400
                )

            # ------------------------------------------------
            # Determine user
            # ------------------------------------------------

            User = get_user_model()

            if request.user.is_authenticated:
                user = request.user
            else:
                user = User.objects.first()

            if user is None:
                return JsonResponse(
                    {
                        "error":
                        "No user exists in the database."
                    },
                    status=400
                )

            # ------------------------------------------------
            # Find normalized species record if one exists
            # ------------------------------------------------

            species_record = Species.objects.filter(
                common_name__iexact=species_name
            ).first()

            # ------------------------------------------------
            # Save sighting + animal sighting together
            # ------------------------------------------------

            with transaction.atomic():

                sighting = Sighting.objects.create(
                    user=user,

                    sighting_type=(
                        Sighting.SightingType.ANIMAL
                    ),

                    description=(
                        notes
                        or f"{species_name} sighting"
                    ),

                    locationLongitude=float(
                        longitude
                    ),

                    locationLatitude=float(
                        latitude
                    ),

                    observed_at=observed_at,

                    animal_count=animal_count,

                    behavior=behavior,

                    notes=notes,

                    is_public=True
                )

                Animal_Sighting.objects.create(
                    sighting=sighting,

                    common_name=species_name,

                    species=(
                        species_record.scientific_name
                        if species_record
                        else ""
                    ),

                    species_record=species_record
                )

            return JsonResponse(
                {
                    "message":
                    "Sighting created successfully.",

                    "id":
                    sighting.id
                },
                status=201
            )

        except json.JSONDecodeError:
            return JsonResponse(
                {
                    "error":
                    "Invalid JSON."
                },
                status=400
            )

        except (ValueError, TypeError) as error:
            return JsonResponse(
                {
                    "error":
                    str(error)
                },
                status=400
            )

        except Exception as error:
            return JsonResponse(
                {
                    "error":
                    str(error)
                },
                status=500
            )

    return JsonResponse(
        {
            "error":
            "Method not allowed."
        },
        status=405
    )


def animal_sightings(request):
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            SELECT
                sighting_id,
                common_name,
                species
            FROM api_animal_sighting
            ORDER BY sighting_id
            '''
        )

        columns = [col[0] for col in cursor.description]

        rows = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    return JsonResponse(rows, safe=False)


def vegetation_sightings(request):
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            SELECT
                sighting_id,
                common_name,
                species
            FROM api_vegetation_sighting
            ORDER BY sighting_id
            '''
        )

        columns = [col[0] for col in cursor.description]

        rows = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    return JsonResponse(rows, safe=False)


def image(request):
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            SELECT
                sighting_id,
                image_url
            FROM api_sighting_image
            ORDER BY sighting_id
            '''
        )

        columns = [col[0] for col in cursor.description]

        rows = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    return JsonResponse(rows, safe=False)


def species(request):
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            SELECT
                s.id,
                s.common_name,
                s.scientific_name,
                s.is_game_species,
                s.conservation_status,
                s.description,
                c.name AS category
            FROM api_species s
            JOIN api_speciescategory c
                ON s.category_id = c.id
            ORDER BY s.common_name
            '''
        )

        columns = [col[0] for col in cursor.description]

        rows = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    return JsonResponse(rows, safe=False)


def regions(request):
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            SELECT
                id,
                name,
                region_type,
                min_lat,
                max_lat,
                min_lon,
                max_lon,
                elevation_ft
            FROM api_region
            ORDER BY name
            '''
        )

        columns = [col[0] for col in cursor.description]

        rows = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    return JsonResponse(rows, safe=False)


def habitats(request):
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            SELECT
                id,
                name
            FROM api_habitat
            ORDER BY name
            '''
        )

        columns = [col[0] for col in cursor.description]

        rows = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    return JsonResponse(rows, safe=False)


def weather_conditions(request):
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            SELECT
                id,
                name
            FROM api_weathercondition
            ORDER BY name
            '''
        )

        columns = [col[0] for col in cursor.description]

        rows = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    return JsonResponse(rows, safe=False)


def hunting_seasons(request):
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            SELECT
                hs.id,
                s.common_name AS species,
                hs.zone,
                hs.weapon,
                hs.open_month_day,
                hs.close_month_day,
                hs.notes
            FROM api_huntingseason hs
            JOIN api_species s
                ON hs.species_id = s.id
            ORDER BY
                s.common_name,
                hs.open_month_day
            '''
        )

        columns = [col[0] for col in cursor.description]

        rows = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    return JsonResponse(rows, safe=False)