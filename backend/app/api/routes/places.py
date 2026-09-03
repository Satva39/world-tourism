from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models.place_image import PlaceImage
from app.db.database import SessionLocal
from app.db.models.place import Place
from app.db.models.region import Region

router = APIRouter(prefix="/places", tags=["Places"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/region/{region_id}")
def get_region_places(
    region_id: int,
    db: Session = Depends(get_db),
):
    region = db.get(Region, region_id)

    if region is None:
        raise HTTPException(
            status_code=404,
            detail="Region not found",
        )

    places = (
        db.query(Place)
        .filter(
            Place.region_id == region_id,
            Place.is_active.is_(True),
        )
        .order_by(Place.name)
        .all()
    )

    return [
        {
            "id": place.id,
            "region_id": place.region_id,
            "name": place.name,
            "slug": place.slug,
            "cover_image": next(
                (image.image_url for image in place.images if image.is_cover),
                None,
            ),
        }
        for place in places
    ]


@router.get("/featured")
def get_featured_places(
    db: Session = Depends(get_db),
):
    places = (
        db.query(Place)
        .filter(
            Place.is_featured.is_(True),
            Place.is_active.is_(True),
        )
        .order_by(Place.name.asc())
        .limit(6)
        .all()
    )

    return [
        {
            "id": place.id,
            "region_id": place.region_id,
            "name": place.name,
            "slug": place.slug,
            "short_description": place.short_description,
            "country_id": (place.region.country_id if place.region else None),
            "cover_image": next(
                (image.image_url for image in place.images if image.is_cover),
                None,
            ),
        }
        for place in places
    ]


@router.get("/{place_id}")
def get_place(
    place_id: int,
    db: Session = Depends(get_db),
):
    place = db.get(Place, place_id)

    if place is None or not place.is_active:
        raise HTTPException(
            status_code=404,
            detail="Place not found",
        )

    return {
        "id": place.id,
        "region_id": place.region_id,
        "name": place.name,
        "slug": place.slug,
        "short_description": place.short_description,
        "description": place.description,
        "latitude": place.latitude,
        "longitude": place.longitude,
        "is_featured": place.is_featured,
        "is_active": place.is_active,
        "images": [
            {
                "id": image.id,
                "image_url": image.image_url,
                "alt_text": image.alt_text,
                "is_primary": image.is_primary,
                "display_order": image.display_order,
            }
            for image in place.images
        ],
        "details": (
            {
                "entry_fee": place.details.entry_fee,
                "opening_hours": place.details.opening_hours,
                "best_time": place.details.best_time,
                "duration": place.details.duration,
                "how_to_reach": place.details.how_to_reach,
                "facilities": place.details.facilities,
                "ticket_url": place.details.ticket_url,
            }
            if place.details
            else None
        ),
    }
