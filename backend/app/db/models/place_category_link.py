from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class PlaceCategoryLink(Base):
    __tablename__ = "place_category_links"

    place_id: Mapped[int] = mapped_column(
        ForeignKey("places.id", ondelete="CASCADE"),
        primary_key=True,
    )

    category_id: Mapped[int] = mapped_column(
        ForeignKey("place_categories.id", ondelete="CASCADE"),
        primary_key=True,
    )
