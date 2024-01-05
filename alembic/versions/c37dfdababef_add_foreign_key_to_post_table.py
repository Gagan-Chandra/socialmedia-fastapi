"""add foreign key to post table

Revision ID: c37dfdababef
Revises: 600dab78dc17
Create Date: 2024-01-05 12:20:45.859966

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c37dfdababef'
down_revision: Union[str, None] = '600dab78dc17'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
