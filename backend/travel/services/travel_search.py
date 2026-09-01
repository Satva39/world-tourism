from .duffel import DuffelFlightProvider


class TravelSearchService:
    """
    Provider-independent travel search service.

    The service automatically resolves nearby airports from
    coordinates before performing a flight search.
    """

    def __init__(self):
        self.flight_provider = DuffelFlightProvider()

    def search_flights(
        self,
        origin_latitude,
        origin_longitude,
        destination_latitude,
        destination_longitude,
        departure_date,
        adults=1,
    ):
        origin_airports = self.flight_provider.find_nearby_airports(
            latitude=origin_latitude,
            longitude=origin_longitude,
        )

        destination_airports = self.flight_provider.find_nearby_airports(
            latitude=destination_latitude,
            longitude=destination_longitude,
        )

        if not origin_airports:
            return {
                "success": False,
                "message": "No nearby departure airport found.",
                "options": [],
            }

        if not destination_airports:
            return {
                "success": False,
                "message": "No nearby destination airport found.",
                "options": [],
            }

        origin = origin_airports[0]["iata_code"]
        destination = destination_airports[0]["iata_code"]

        result = self.flight_provider.search(
            origin=origin,
            destination=destination,
            departure_date=departure_date,
            adults=adults,
        )

        return {
            "success": True,
            "origin": {
                "airport": origin_airports[0],
            },
            "destination": {
                "airport": destination_airports[0],
            },
            "results": result,
        }
