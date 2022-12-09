from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, Text

from .database import db

if TYPE_CHECKING:
    from flask_sqlalchemy.query import Query


class Post(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(1000), unique=False, nullable=False)
    body = Column(Text, nullable=False, default="")

    if TYPE_CHECKING:
        query: Query