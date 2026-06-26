import asyncio

from telethon import TelegramClient
from telethon.tl.types import Chat, Channel

from config import Config
from app.database.repository import Repository


repo = Repository()


async def load_dialogs():

    client = TelegramClient(
        Config.SESSION_NAME,
        Config.API_ID,
        Config.API_HASH,
    )

    await client.connect()

    dialogs = await client.get_dialogs()

    result = []

    for dialog in dialogs:

        entity = dialog.entity

        if not isinstance(entity, (Chat, Channel)):
            continue

        if getattr(entity, "broadcast", False):
            continue

        db_chat = repo.get_chat(dialog.id)

        result.append(
            {
                "id": dialog.id,
                "title": dialog.name,
                "active": db_chat.active if db_chat else False,
            }
        )

    await client.disconnect()

    result.sort(
        key=lambda x: (
            not x["active"],
            x["title"].lower(),
        )
    )

    return result


def chats_menu():

    while True:

        dialogs = asyncio.run(load_dialogs())

        print()
        print("=" * 80)
        print("УПРАВЛЕНИЕ ЧАТАМИ")
        print("=" * 80)
        print()

        for index, chat in enumerate(dialogs, start=1):

            status = "✅" if chat["active"] else "❌"

            print(
                f"{index:>2}. {status}  {chat['title']}"
            )

        print()
        print("ENTER - назад")
        print()

        cmd = input("> ").strip()

        if cmd == "":
            return

        if not cmd.isdigit():
            continue

        idx = int(cmd) - 1

        if idx < 0 or idx >= len(dialogs):
            continue

        selected = dialogs[idx]

        if selected["active"]:

            answer = input(
                f'Отключить "{selected["title"]}"? (y/n): '
            ).lower()

            if answer == "y":

                repo.deactivate_chat(
                    selected["id"]
                )

        else:

            answer = input(
                f'Подключить "{selected["title"]}"? (y/n): '
            ).lower()

            if answer != "y":
                continue

            if repo.chat_exists(selected["id"]):

                repo.activate_chat(
                    selected["id"]
                )

            else:

                repo.add_chat(
                    telegram_chat_id=selected["id"],
                    title=selected["title"],
                )

        print()
        print("Готово.")
        input("ENTER...")