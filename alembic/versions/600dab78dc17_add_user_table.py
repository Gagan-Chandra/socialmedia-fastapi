"""add user table

Revision ID: 600dab78dc17
Revises: 06a5125c3ba8
Create Date: 2024-01-05 12:09:10.998754

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '600dab78dc17'
down_revision: Union[str, None] = '06a5125c3ba8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('users',
                        sa.Column('id',sa.Integer(),nullable=False),
                        sa.Column('email',sa.String(),nullable=False),
                        sa.Column('password',sa.String(),nullable=False),
                        sa.Column('created_at',sa.TIMESTAMP(timezone=True),
                                    server_default=sa.text('now()'),nullable=False),
                        sa.PrimaryKeyConstraint('id'),
                        sa.UniqueConstraint('email'))
    pass


def downgrade():
    op.drop_table('users')
    pass
