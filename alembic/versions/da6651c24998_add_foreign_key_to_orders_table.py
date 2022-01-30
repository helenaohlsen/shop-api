"""Add foreign key to orders table

Revision ID: da6651c24998
Revises: cf8c122dfe52
Create Date: 2022-01-30 14:32:29.111471

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "da6651c24998"
down_revision = "cf8c122dfe52"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("orders", sa.Column("customer_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "fk_order_customer",
        source_table="orders",
        referent_table="customers",
        local_cols=["customer_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )


def downgrade():
    op.drop_constraint("fk_order_customer", table_name="orders")
    op.drop_column("orders", "customer_id")
    pass
