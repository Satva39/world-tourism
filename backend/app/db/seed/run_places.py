from sqlalchemy import select

from app.db.database import SessionLocal
from app.db.models.place import Place
from app.db.models.region import Region

from app.db.seed.places import PLACES

BATCH_SIZE = 50


def seed_places() -> None:
    created = 0
    skipped = 0

    # Load regions and existing places once.
    db = SessionLocal()

    try:
        regions = dict(db.execute(select(Region.slug, Region.id)).all())

        existing_places = {
            (region_id, slug)
            for slug, region_id in db.execute(select(Place.slug, Place.region_id)).all()
        }

    finally:
        db.close()

    # Process places in small independent transactions.
    for batch_start in range(0, len(PLACES), BATCH_SIZE):
        batch = PLACES[batch_start : batch_start + BATCH_SIZE]

        db = SessionLocal()

        try:
            places_to_create = []

            for place_data in batch:
                region_id = regions.get(place_data["region_slug"])

                if region_id is None:
                    print(
                        f"Skipped {place_data['name']}: "
                        f"region '{place_data['region_slug']}' not found"
                    )
                    skipped += 1
                    continue

                place_key = (
                    region_id,
                    place_data["slug"],
                )

                if place_key in existing_places:
                    skipped += 1
                    continue

                places_to_create.append(
                    Place(
                        region_id=region_id,
                        name=place_data["name"],
                        slug=place_data["slug"],
                        short_description=place_data["short_description"],
                        description=place_data["description"],
                        latitude=place_data["latitude"],
                        longitude=place_data["longitude"],
                        is_featured=place_data["is_featured"],
                        is_active=True,
                    )
                )

                existing_places.add(place_key)

            if places_to_create:
                db.add_all(places_to_create)
                db.commit()

                created += len(places_to_create)

        except Exception:
            db.rollback()
            raise

        finally:
            db.close()

        processed = min(
            batch_start + BATCH_SIZE,
            len(PLACES),
        )

        print(f"Processed {processed}/{len(PLACES)} places...")

    print()
    print("Place seed completed.")
    print(f"Places created: {created}")
    print(f"Places skipped: {skipped}")
    print(f"Total processed: {created + skipped}")


if __name__ == "__main__":
    seed_places()
