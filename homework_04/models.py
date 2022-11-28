"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""
import os
from sqlalchemy import (
    create_engine,
    Column,
    String,
    Text,
    Integer,
    ForeignKey,
)
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
    declared_attr,
)
from sqlalchemy.orm import relationship

from homework_04 import config

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or config.DB_ASYNC_URL


async_engine: AsyncEngine = create_async_engine(
    url=PG_CONN_URI,
)

Session = sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class Base:
    @declared_attr
    def __tablename__(cls):
        # users
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return str(self)


engine = create_engine(url=config.DB_URL, echo=config.DB_ECHO)
Base = declarative_base(bind=engine, cls=Base)


# class User(Base):
class User(Base):
    name = Column(String(100), unique=False, nullable=False)
    username = Column(String(20), unique=True, nullable=False)
    email = Column(String(100), unique=True, default="")

    posts = relationship("Post", back_populates="user", uselist=True)

    def __str__(self):
        return f"User(id={self.id}, username={self.username!r})"


class Post(Base):
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String(1000), unique=False, nullable=False)
    body = Column(Text, nullable=False, default="")

    user = relationship("User", back_populates="posts", uselist=False)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, title={self.title!r}, body={self.body!r})"

    def __repr__(self):
        return str(self)
