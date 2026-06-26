from datetime import datetime

from sqlalchemy import (
    BigInteger,
    Boolean,
    DateTime,
    Integer,
    String,
    Text,
)

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.db import Base


class WatchedChat(Base):
    __tablename__ = "watched_chats"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    telegram_chat_id: Mapped[int] = mapped_column(
        BigInteger,
        unique=True,
        nullable=False,
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )


class Manager(Base):
    __tablename__ = "managers"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    telegram_id: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )


class Client(Base):
    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    telegram_user_id: Mapped[int] = mapped_column(
        BigInteger,
        unique=True,
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        default="",
    )

    username: Mapped[str] = mapped_column(
        String(255),
        default="",
    )

    manager_id: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    telegram_message_id: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    telegram_chat_id: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    telegram_user_id: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    client_name: Mapped[str] = mapped_column(
        String(255),
        default="",
    )

    text: Mapped[str] = mapped_column(
        Text,
        default="",
    )

    summary: Mapped[str] = mapped_column(
        Text,
        default="",
    )

    category: Mapped[str] = mapped_column(
        String(100),
        default="other",
    )

    priority: Mapped[str] = mapped_column(
        String(30),
        default="medium",
    )

    suggested_reply: Mapped[str] = mapped_column(
        Text,
        default="",
    )

    manager_required: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    answered: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    reminder_sent: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    answered_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )