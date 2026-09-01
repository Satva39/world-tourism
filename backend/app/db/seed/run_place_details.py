from sqlalchemy import select

from app.db.database import SessionLocal
from app.db.models.place import Place
from app.db.models.place_details import PlaceDetails
from app.db.seed.place_details import PLACE_DETAILS

BATCH_SIZE = 50


def seed_place_details() -> None:
    created = 0
    skipped = 0

    # Load all places once.
    db = SessionLocal()

    try:
        places = dict(db.execute(select(Place.slug, Place.id)).all())

        existing_details = {
            place_id
            for place_id in db.execute(select(PlaceDetails.place_id)).scalars().all()
        }

    finally:
        db.close()

    # Process details in batches.
    for batch_start in range(0, len(PLACE_DETAILS), BATCH_SIZE):
        batch = PLACE_DETAILS[batch_start : batch_start + BATCH_SIZE]

        db = SessionLocal()

        try:
            details_to_create = []

            for data in batch:
                place_id = places.get(data["place_slug"])

                if place_id is None:
                    print(f"Warning: Place not found: " f"{data['place_slug']}")
                    skipped += 1
                    continue

                if place_id in existing_details:
                    skipped += 1
                    continue

                details_to_create.append(
                    PlaceDetails(
                        place_id=place_id,
                        entry_fee=data.get("entry_fee"),
                        opening_hours=data.get("opening_hours"),
                        best_time=data.get("best_time"),
                        duration=data.get("duration"),
                        how_to_reach=data.get("how_to_reach"),
                        facilities=data.get("facilities"),
                        ticket_url=data.get("ticket_url"),
                    )
                )

                existing_details.add(place_id)

            if details_to_create:
                db.add_all(details_to_create)
                db.commit()

                created += len(details_to_create)

        except Exception:
            db.rollback()
            raise

        finally:
            db.close()

        processed = min(
            batch_start + BATCH_SIZE,
            len(PLACE_DETAILS),
        )

        print(f"Processed {processed}/{len(PLACE_DETAILS)} " f"place details...")

    print()
    print("Place details seed completed.")
    print(f"Details created: {created}")
    print(f"Details skipped: {skipped}")
    print(f"Total processed: {created + skipped}")


if __name__ == "__main__":
    seed_place_details()
