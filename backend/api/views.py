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
            'SELECT sighting_id, image_url FROM api_sighting_image ORDER BY sighting_id'
        )
        columns = [col[0] for col in cursor.description]
        rows = [dict(zip(columns, row)) for row in cursor.fetchall()]
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
        rows = [dict(zip(columns, row)) for row in cursor.fetchall()]

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
        rows = [dict(zip(columns, row)) for row in cursor.fetchall()]

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
        rows = [dict(zip(columns, row)) for row in cursor.fetchall()]

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
        rows = [dict(zip(columns, row)) for row in cursor.fetchall()]

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
            ORDER BY s.common_name, hs.open_month_day
            '''
        )

        columns = [col[0] for col in cursor.description]
        rows = [dict(zip(columns, row)) for row in cursor.fetchall()]

    return JsonResponse(rows, safe=False)