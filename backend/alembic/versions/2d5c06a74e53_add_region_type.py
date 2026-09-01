"""add region type

Revision ID: 2d5c06a74e53
Revises: 5401c02f199b
Create Date: 2026-08-26

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "2d5c06a74e53"
down_revision: Union[str, Sequence[str], None] = "5401c02f199b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "regions",
        sa.Column(
            "type",
            sa.String(length=20),
            nullable=False,
        ),
    )


def downgrade() -> None:
    op.drop_column("regions", "type")
