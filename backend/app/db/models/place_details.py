from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base


class PlaceDetails(Base):
    __tablename__ = "place_details"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    place_id: Mapped[int] = mapped_column(
        ForeignKey("places.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
    )

    entry_fee: Mapped[str | None] = mapped_column(String(200))
    opening_hours: Mapped[str | None] = mapped_column(String(300))
    best_time: Mapped[str | None] = mapped_column(String(300))
    duration: Mapped[str | None] = mapped_column(String(200))
    how_to_reach: Mapped[str | None] = mapped_column(Text)
    facilities: Mapped[str | None] = mapped_column(Text)
    ticket_url: Mapped[str | None] = mapped_column(String(500))

    place = relationship("Place", back_populates="details")
