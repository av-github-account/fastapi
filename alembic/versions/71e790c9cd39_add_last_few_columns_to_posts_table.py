"""add last few columns to posts table

Revision ID: 71e790c9cd39
Revises: 486d8549bc7b
Create Date: 2025-02-11 21:47:45.900426

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '71e790c9cd39'
down_revision: Union[str, None] = '486d8549bc7b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', 
                  sa.Column('published', 
                            sa.Boolean(), 
                            nullable=False, 
                            server_default='True'),)
    op.add_column('posts', 
                  sa.Column('created_at',
                            sa.TIMESTAMP(timezone=True), 
                            nullable=False, 
                            server_default=sa.text('now()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
