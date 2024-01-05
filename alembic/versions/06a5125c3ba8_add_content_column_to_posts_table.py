"""add content column to posts table

Revision ID: 06a5125c3ba8
Revises: 4dc2cafd9121
Create Date: 2024-01-05 12:00:11.638075

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '06a5125c3ba8'
down_revision: Union[str, None] = '4dc2cafd9121'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
