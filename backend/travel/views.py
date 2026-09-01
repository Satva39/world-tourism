from datetime import date

from django.http import JsonResponse
from django.views.decorators.http import require_GET

from .services.travel_search import TravelSearchService


@require_GET
def flight_search(request):
    try:
        origin_latitude = float(request.GET["origin_latitude"])
        origin_longitude = float(request.GET["origin_longitude"])
        destination_latitude = float(request.GET["destination_latitude"])
        destination_longitude = float(request.GET["destination_longitude"])
        departure_date = request.GET["departure_date"]

        date.fromisoformat(departure_date)

    except KeyError as exc:
        return JsonResponse(
            {
                "success": False,
                "message": f"Missing parameter: {exc.args[0]}",
            },
            status=400,
        )

    except ValueError:
        return JsonResponse(
            {
                "success": False,
                "message": "Invalid coordinates or departure date.",
            },
            status=400,
        )

    try:
        service = TravelSearchService()

        result = service.search_flights(
            origin_latitude=origin_latitude,
            origin_longitude=origin_longitude,
            destination_latitude=destination_latitude,
            destination_longitude=destination_longitude,
            departure_date=departure_date,
        )

        return JsonResponse(result)

    except Exception as exc:
        return JsonResponse(
            {
                "success": False,
                "message": str(exc),
                "options": [],
            },
            status=502,
        )
