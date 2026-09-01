from fastapi import APIRouter, Depends, Query
from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db.models.country import Country
from app.db.models.region import Region
from app.db.models.place import Place

router = APIRouter(
    prefix="/api/search",
    tags=["Search"],
)


@router.get("")
def search(
    q: str = Query(..., min_length=1, max_length=100),
    db: Session = Depends(get_db),
):
    search_text = f"%{q.strip()}%"

    countries = (
        db.query(Country).filter(Country.name.ilike(search_text)).limit(10).all()
    )

    regions = db.query(Region).filter(Region.name.ilike(search_text)).limit(20).all()

    places = (
        db.query(Place, Region.country_id)
        .join(Region, Place.region_id == Region.id)
        .filter(
            or_(
                Place.name.ilike(search_text),
                Place.short_description.ilike(search_text),
                Place.description.ilike(search_text),
            )
        )
        .limit(30)
        .all()
    )

    return {
        "query": q,
        "countries": [
            {
                "id": country.id,
                "name": country.name,
                "slug": country.slug,
            }
            for country in countries
        ],
        "regions": [
            {
                "id": region.id,
                "country_id": region.country_id,
                "name": region.name,
                "slug": region.slug,
                "region_type": region.region_type,
            }
            for region in regions
        ],
        "places": [
            {
                "id": place.id,
                "country_id": country_id,
                "region_id": place.region_id,
                "name": place.name,
                "slug": place.slug,
                "short_description": place.short_description,
            }
            for place, country_id in places
        ],
    }
