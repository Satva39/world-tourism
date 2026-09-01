from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db.models.place import Place
from app.db.models.place_details import PlaceDetails

router = APIRouter(
    prefix="/api/place-details",
    tags=["Place Details"],
)


@router.get("/{place_id}")
def get_place_details(
    place_id: int,
    db: Session = Depends(get_db),
):
    place = db.query(Place).filter(Place.id == place_id).first()

    if not place:
        raise HTTPException(
            status_code=404,
            detail="Place not found",
        )

    details = db.query(PlaceDetails).filter(PlaceDetails.place_id == place_id).first()

    if not details:
        raise HTTPException(
            status_code=404,
            detail="Place details not found",
        )

    return {
        "place": {
            "id": place.id,
            "name": place.name,
            "slug": place.slug,
            "short_description": place.short_description,
            "description": place.description,
            "latitude": place.latitude,
            "longitude": place.longitude,
        },
        "details": {
            "entry_fee": details.entry_fee,
            "opening_hours": details.opening_hours,
            "best_time": details.best_time,
            "duration": details.duration,
            "how_to_reach": details.how_to_reach,
            "facilities": details.facilities,
            "ticket_url": details.ticket_url,
        },
        "images": [
            {
                "id": image.id,
                "image_url": image.image_url,
                "alt_text": image.alt_text,
                "is_cover": image.is_cover,
                "sort_order": image.sort_order,
            }
            for image in place.images
        ],
    }
