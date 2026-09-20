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