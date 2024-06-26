"""Add title to content table

Revision ID: adaf0887295d
Revises: 10d2dc75342d
Create Date: 2024-05-20 10:18:18.347624

"""

import re
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "adaf0887295d"
down_revision: Union[str, None] = "10d2dc75342d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("contents", sa.Column("title", sa.String(length=255)))
    query = """
SELECT id, array_to_string(
  (string_to_array(
    regexp_replace(html_text, E'\n.*$', ''),
    ' '
  ))[1:3],
  ' '
) as title FROM contents;
    """
    query = sa.text(query)
    conn = op.get_bind()
    result = conn.execute(query)

    for _id, text in result:
        title = re.sub(r"(.)\1+", r"\1", text)
        title = title.replace("#", "").strip()
        op.execute(
            f"UPDATE contents SET title = '{title}' WHERE id = {int(_id)}",
        )
    op.alter_column("contents", "title", nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("contents", "title")
    # ### end Alembic commands ###
