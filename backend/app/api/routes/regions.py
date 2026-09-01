from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.models.place_image import PlaceImage
from app.db.database import get_db
from app.db.models.region import Region
from app.db.models.place import Place

router = APIRouter(
    prefix="/api/regions",
    tags=["Regions"],
)


@router.get("/{region_id}")
def get_region(
    region_id: int,
    db: Session = Depends(get_db),
):
    region = db.query(Region).filter(Region.id == region_id).first()

    if not region:
        raise HTTPException(
            status_code=404,
            detail="Region not found",
        )

    return {
        "id": region.id,
        "country_id": region.country_id,
        "name": region.name,
        "slug": region.slug,
        "region_type": region.region_type,
    }


@router.get("/{region_id}/places")
def get_region_places(
    region_id: int,
    db: Session = Depends(get_db),
):
    region = db.query(Region).filter(Region.id == region_id).first()

    if not region:
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

    result = []


    for place in places:
        cover_image = (
            db.query(PlaceImage)
            .filter(
                PlaceImage.place_id == place.id,
                PlaceImage.is_cover.is_(True),
            )
            .order_by(PlaceImage.sort_order.asc())
            .first()
        )
    
        result.append(
            {
                "id": place.id,
                "name": place.name,
                "slug": place.slug,
                "short_description": place.short_description,
                "description": place.description,
                "latitude": place.latitude,
                "longitude": place.longitude,
                "cover_image": (cover_image.image_url if cover_image else None),
            }
        )
    
    return result


@router.get("/country/{country_id}")
def get_regions_by_country(
    country_id: int,
    db: Session = Depends(get_db),
):
    regions = (
        db.query(Region)
        .filter(Region.country_id == country_id)
        .order_by(Region.name)
        .all()
    )

    return [
        {
            "id": region.id,
            "country_id": region.country_id,
            "name": region.name,
            "slug": region.slug,
            "region_type": region.region_type,
        }
        for region in regions
    ]
