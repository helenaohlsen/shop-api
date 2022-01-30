"""Create orders table

Revision ID: cf8c122dfe52
Revises: 7d4d5612b26d
Create Date: 2022-01-30 14:23:09.198352

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "cf8c122dfe52"
down_revision = "7d4d5612b26d"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "orders",
        sa.Column("id", sa.Integer(), primary_key=True, unique=True, autoincrement=True),
        sa.Column("item", sa.String(25), nullable=False),
        sa.Column("quantity", sa.Integer(), nullable=False),
    )


def downgrade():
    op.drop_table("orders")
