"""Add tables, user and specializacion area

Revision ID: 10d2dc75342d
Revises: 0821cd9f8195
Create Date: 2024-05-16 20:24:54.456974

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "10d2dc75342d"
down_revision: Union[str, None] = "0821cd9f8195"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "specialization_areas",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_specialization_areas_id"), "specialization_areas", ["id"], unique=False)
    op.create_table(
        "users",
        sa.Column("uuid", sa.Uuid(), nullable=False),
        sa.Column("first_name", sa.String(length=255), nullable=False),
        sa.Column("last_name", sa.String(length=255), nullable=False),
        sa.Column("birth_date", sa.Date(), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("hashed_password", sa.String(length=255), nullable=False),
        sa.Column("specialization_area_id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(
            ["specialization_area_id"],
            ["specialization_areas.id"],
        ),
        sa.PrimaryKeyConstraint("uuid"),
        sa.UniqueConstraint("email"),
    )
    op.create_index(op.f("ix_users_uuid"), "users", ["uuid"], unique=False)

    specializations = [
        dict(id=1, title="Desarrollo web"),
        dict(id=2, title="Ciberseguridad"),
        dict(id=3, title="Inteligencia Artificial"),
        dict(id=4, title="Desarrollo mobile"),
        dict(id=5, title="Inglés"),
        dict(id=6, title="Redes y telecomunicaciones"),
    ]

    specialization_areas = sa.sql.table(
        "specialization_areas",
        sa.sql.column("id", sa.Integer()),
        sa.sql.column("title", sa.String(length=255)),
    )

    for specialization in specializations:
        op.bulk_insert(specialization_areas, [specialization])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_users_uuid"), table_name="users")
    op.drop_table("users")
    op.drop_index(op.f("ix_specialization_areas_id"), table_name="specialization_areas")
    op.drop_table("specialization_areas")
    # ### end Alembic commands ###