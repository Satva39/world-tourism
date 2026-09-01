from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db.models.country import Country
from app.db.models.region import Region
from app.api.schemas.country import CountryResponse
from app.api.schemas.region import RegionResponse

router = APIRouter(
    prefix="/countries",
    tags=["Countries"],
)


@router.get("/", response_model=list[CountryResponse])
def get_countries(
    db: Session = Depends(get_db),
):
    countries = db.scalars(select(Country).order_by(Country.name)).all()

    return countries


@router.get("/{country_id}", response_model=CountryResponse)
def get_country(
    country_id: int,
    db: Session = Depends(get_db),
):
    country = db.scalar(select(Country).where(Country.id == country_id))

    if country is None:
        raise HTTPException(
            status_code=404,
            detail="Country not found",
        )

    return country

@router.get("/{country_id}/regions")
def get_country_regions(
    country_id: int,
    db: Session = Depends(get_db),
):
    country = db.query(Country).filter(Country.id == country_id).first()

    if not country:
        raise HTTPException(
            status_code=404,
            detail="Country not found",
        )

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
