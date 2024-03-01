"""create table

Revision ID: 0031f66b4e3d
Revises: 
Create Date: 2024-03-01 14:47:58.420490

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0031f66b4e3d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('Student',sa.Column('id',sa.Integer, primary_key=True),
                           sa.Column('name ', sa.String(20)),
                           sa.Column('age',sa.Integer))


def downgrade() -> None:
    pass
