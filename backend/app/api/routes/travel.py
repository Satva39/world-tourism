from datetime import date

from fastapi import APIRouter, HTTPException, Query

from travel.services.travel_search import TravelSearchService
from travel.services.duffel import DuffelFlightProvider

router = APIRouter(
    prefix="/api/travel",
    tags=["Travel"],
)

service = TravelSearchService()


@router.get("/flights")
def search_flights(
    origin_latitude: float = Query(...),
    origin_longitude: float = Query(...),
    destination_latitude: float = Query(...),
    destination_longitude: float = Query(...),
    departure_date: date = Query(...),
    adults: int = Query(1, ge=1),
):
    try:
        return service.search_flights(
            origin_latitude=origin_latitude,
            origin_longitude=origin_longitude,
            destination_latitude=destination_latitude,
            destination_longitude=destination_longitude,
            departure_date=departure_date.isoformat(),
            adults=adults,
        )

    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail=str(exc),
        )


@router.post("/flights/{offer_id}/booking-link")
def create_booking_link(offer_id: str):
    try:
        provider = DuffelFlightProvider()

        result = provider.create_booking_link(
            offer_id=offer_id,
        )

        return {
            "success": True,
            "url": result["url"],
            "reference": result.get("reference"),
        }

    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail=str(exc),
        )
