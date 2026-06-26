from datetime import datetime

from sqlalchemy import select

from app.database.db import get_session
from app.database.models import (
    Client,
    Manager,
    Message,
    WatchedChat,
)


class Repository:

    # =====================================================
    # CHATS
    # =====================================================

    def get_chat(self, telegram_chat_id: int):

        session = get_session()

        try:

            stmt = select(WatchedChat).where(
                WatchedChat.telegram_chat_id == telegram_chat_id
            )

            return session.execute(stmt).scalar_one_or_none()

        finally:
            session.close()

    def get_all_chats(self):

        session = get_session()

        try:

            stmt = (
                select(WatchedChat)
                .order_by(WatchedChat.title)
            )

            return session.execute(stmt).scalars().all()

        finally:
            session.close()

    def get_active_chats(self):

        session = get_session()

        try:

            stmt = (
                select(WatchedChat)
                .where(WatchedChat.active.is_(True))
                .order_by(WatchedChat.title)
            )

            return session.execute(stmt).scalars().all()

        finally:
            session.close()

    def add_chat(
        self,
        telegram_chat_id: int,
        title: str,
    ):

        session = get_session()

        try:

            chat = self.get_chat(telegram_chat_id)

            if chat:

                chat = session.merge(chat)
                chat.title = title
                chat.active = True

                session.commit()

                return chat

            chat = WatchedChat(
                telegram_chat_id=telegram_chat_id,
                title=title,
                active=True,
            )

            session.add(chat)

            session.commit()

            session.refresh(chat)

            return chat

        finally:
            session.close()

    def activate_chat(self, telegram_chat_id: int):

        session = get_session()

        try:

            stmt = select(WatchedChat).where(
                WatchedChat.telegram_chat_id == telegram_chat_id
            )

            chat = session.execute(stmt).scalar_one_or_none()

            if chat:

                chat.active = True
                session.commit()

                return True

            return False

        finally:
            session.close()

    def deactivate_chat(self, telegram_chat_id: int):

        session = get_session()

        try:

            stmt = select(WatchedChat).where(
                WatchedChat.telegram_chat_id == telegram_chat_id
            )

            chat = session.execute(stmt).scalar_one_or_none()

            if chat:

                chat.active = False
                session.commit()

                return True

            return False

        finally:
            session.close()

    def chat_exists(self, telegram_chat_id: int):

        return self.get_chat(telegram_chat_id) is not None