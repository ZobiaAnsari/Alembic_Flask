"""add col

Revision ID: dbc75c9ad22d
Revises: 0031f66b4e3d
Create Date: 2024-03-01 16:12:57.509868

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dbc75c9ad22d'
down_revision: Union[str, None] = '0031f66b4e3d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('Student', sa.Column('email',sa.String(30)))


def downgrade() -> None:
    op.drop_column('Student','email')
