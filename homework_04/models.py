"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""
import logging
import os

from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession, async_scoped_session, create_async_engine
from sqlalchemy.orm import declarative_base, declared_attr, sessionmaker, relationship
from asyncio import current_task


class Base:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True, nullable=False)


PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:tvmix333@localhost/postgres"

async_engine = create_async_engine(PG_CONN_URI)
Decl_base = declarative_base(bind=async_engine, cls=Base)
async_session_factory = sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)


class _AsyncSession:
    def __init__(self):
        self.session = async_scoped_session(session_factory=async_session_factory, scopefunc=current_task)

    async def __aenter__(self):
        return self.session

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        try:
            await self.session.commit()
        except IntegrityError as e:
            logging.error(e)
            await self.session.rollback()
        finally:
            await self.session.remove()


class User(Decl_base):
    name = Column(String(50), nullable=False, default="", server_default="")
    username = Column(String(50), nullable=False, default="", server_default="")
    email = Column(String(100), nullable=False, default="", server_default="", unique=True)

    post = relationship("Post", back_populates="user", uselist=False)

    def __init__(self, name, username, email, **kwargs):
        self.name = name
        self.username = username
        self.email = email

    def __str__(self):
        return f"id: {self.id}, name: {self.name}, username: {self.username}, email: {self.email}"

    def __repr__(self):
        return str(self)


class Post(Decl_base):
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    title = Column(String(120), nullable=False, default="", server_default="")
    body = Column(Text, nullable=False, default="", server_default="")

    user = relationship("User", back_populates="post", uselist=False)

    def __init__(self, userId, title, body, **kwargs):
        self.user_id = userId
        self.title = title
        self.body = body

    def __str__(self):
        return f"id: {self.id}, user_id: {self.user_id}, title: {self.title}, body: {self.body}"

    def __repr__(self):
        return str(self)
