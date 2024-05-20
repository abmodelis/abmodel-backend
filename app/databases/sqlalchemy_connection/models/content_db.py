from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.databases.sqlalchemy_connection.base import Base


class ContentDb(Base):
    __tablename__ = "contents"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    title: Mapped[str] = mapped_column(String(255))
    html_text: Mapped[str] = mapped_column(Text)
    media_path: Mapped[str] = mapped_column(String(255))
    unit_id: Mapped[int] = mapped_column(ForeignKey("units.id"))
    unit: Mapped[Optional["UnitDB"]] = relationship(back_populates="contents", lazy="noload")

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), insert_default=func.CURRENT_TIMESTAMP())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), insert_default=func.CURRENT_TIMESTAMP())

    def __repr__(self):
        return f"<Content(id={self.id},\n\
                   \ttitle={self.title},\n\
                   \thtml_text={self.html_text},\n\
                   \tmedia_path={self.media_path},\n\
                   \tunit_id={self.unit_id},\n\
                   \tcreated_at={self.created_at},\n\
                   \tupdated_at={self.updated_at})>"


from .unit_db import UnitDB
