from sqlalchemy import select

from app.db.database import SessionLocal
from app.db.models.country import Country
from app.db.models.region import Region

from app.db.seed.india import INDIA, INDIA_REGIONS


def seed_india() -> None:
    db = SessionLocal()

    try:
        # Find India
        country = db.scalar(select(Country).where(Country.slug == INDIA["slug"]))

        # Create India if it doesn't exist
        if country is None:
            country = Country(
                name=INDIA["name"],
                slug=INDIA["slug"],
                iso_code=INDIA["iso_code"],
            )

            db.add(country)
            db.flush()

            print("Created country: India")
        else:
            print("Country already exists: India")

        # Add States and Union Territories
        created = 0
        skipped = 0

        for region_data in INDIA_REGIONS:
            region = db.scalar(
                select(Region).where(
                    Region.slug == region_data["slug"],
                    Region.country_id == country.id,
                )
            )

            if region is not None:
                skipped += 1
                continue

            region = Region(
                country_id=country.id,
                name=region_data["name"],
                slug=region_data["slug"],
                region_type=region_data["region_type"],
            )

            db.add(region)
            created += 1

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    seed_india()
