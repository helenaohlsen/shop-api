"""Create customers table

Revision ID: 7d4d5612b26d
Revises: 
Create Date: 2022-01-30 14:16:02.251492

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "7d4d5612b26d"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "customers",
        sa.Column("id", sa.Integer(), primary_key=True, unique=True),
        sa.Column("name", sa.String(30), nullable=False),
        sa.Column("address", sa.String(50), nullable=False),
    )


def downgrade():
    op.drop_table("customers")
