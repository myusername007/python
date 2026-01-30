"""added is_active to users

Revision ID: c1ee16523cb0
Revises: 8567e465dccd
Create Date: 2026-01-30 18:53:29.184130

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c1ee16523cb0'
down_revision: Union[str, Sequence[str], None] = '8567e465dccd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Крок 1: Додай колонку як nullable з default
    op.add_column('users', sa.Column('is_active', sa.Boolean(), nullable=True, server_default='true'))
    
    # Крок 2: Оновіть всі існуючі записи
    op.execute("UPDATE users SET is_active = true WHERE is_active IS NULL")
    
    # Крок 3: Зміни на NOT NULL
    op.alter_column('users', 'is_active', nullable=False, server_default='true')


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users', 'is_active')
