from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base

if TYPE_CHECKING:
    from app.db.models.country import Country
    from app.db.models.place import Place


class Region(Base):
    __tablename__ = "regions"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    country_id: Mapped[int] = mapped_column(
        ForeignKey("countries.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(120),
        nullable=False,
    )

    slug: Mapped[str] = mapped_column(
        String(140),
        nullable=False,
        index=True,
    )

    region_type: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )
    
    capital: Mapped[str | None] = mapped_column(
        String(120),
        nullable=True,
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

    country: Mapped["Country"] = relationship(
        back_populates="regions",
    )

    places: Mapped[list["Place"]] = relationship(
        back_populates="region",
        cascade="all, delete-orphan",
    )
