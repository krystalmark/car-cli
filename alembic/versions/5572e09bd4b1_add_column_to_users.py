"""add_column_to_users

Revision ID: 5572e09bd4b1
Revises: 
Create Date: 2023-09-07 12:40:16.241991

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5572e09bd4b1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('new_column', sa.String(length=50), nullable=True))

    pass


def downgrade() -> None:
    pass
