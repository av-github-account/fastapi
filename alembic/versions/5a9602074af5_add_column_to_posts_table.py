"""add column to posts table

Revision ID: 5a9602074af5
Revises: ca8de8e76558
Create Date: 2025-02-11 20:32:34.863097

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "5a9602074af5"
down_revision: Union[str, None] = "ca8de8e76558"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
