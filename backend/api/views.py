from django.db import connection
from django.http import JsonResponse


def health(request):
    return JsonResponse({"status": "ok"})


def members(request):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT id, first_name, last_name, grade_in_years FROM members ORDER BY id"
        )
        columns = [col[0] for col in cursor.description]
        rows = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return JsonResponse(rows, safe=False)

def sightings(request):
    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT id, user_id, sighting_type, timestamp, description, "locationLongitude", "locationLatitude" FROM api_sighting ORDER BY id'
        )
        columns = [col[0] for col in cursor.description]
        rows = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return JsonResponse(rows, safe=False)

def animal_sightings(request):
    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT sighting_id, common_name, species FROM api_animal_sighting ORDER BY sighting_id'
        )
        columns = [col[0] for col in cursor.description]
        rows = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return JsonResponse(rows, safe=False)

def vegetation_sightings(request):
    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT sighting_id, common_name, species FROM api_vegetation_sighting ORDER BY sighting_id'
        )
        columns = [col[0] for col in cursor.description]
        rows = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return JsonResponse(rows, safe=False)

def image(request):
    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT sighting_id, image_url FROM api_image_sighting ORDER BY sighting_id'
        )
        columns = [col[0] for col in cursor.description]
        rows = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return JsonResponse(rows, safe=False)