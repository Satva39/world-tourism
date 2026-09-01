from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm import relationship

from app.db.database import Base

if TYPE_CHECKING:
    from app.db.models.region import Region
    from app.db.models.place_category import PlaceCategory


class Place(Base):
    __tablename__ = "places"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    region_id: Mapped[int] = mapped_column(
        ForeignKey("regions.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(160),
        nullable=False,
    )

    slug: Mapped[str] = mapped_column(
        String(180),
        nullable=False,
        index=True,
    )

    short_description: Mapped[str | None] = mapped_column(
        String(300),
        nullable=True,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    latitude: Mapped[float | None] = mapped_column(
        nullable=True,
    )

    longitude: Mapped[float | None] = mapped_column(
        nullable=True,
    )

    is_featured: Mapped[bool] = mapped_column(
        default=False,
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        default=True,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    place_categories: Mapped[list["PlaceCategory"]] = relationship(
        secondary="place_category_links",
        back_populates="places",
    )

    region: Mapped["Region"] = relationship(
        back_populates="places",
    )

    images = relationship(
        "PlaceImage",
        back_populates="place",
        cascade="all, delete-orphan",
        order_by="PlaceImage.sort_order",
    )

    details = relationship(
        "PlaceDetails",
        back_populates="place",
        uselist=False,
        cascade="all, delete-orphan",
    )
