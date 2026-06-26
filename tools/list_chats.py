import asyncio

from telethon import TelegramClient

from config import Config


async def main():

    client = TelegramClient(
        Config.SESSION_NAME,
        Config.API_ID,
        Config.API_HASH,
    )

    await client.connect()

    dialogs = await client.get_dialogs()

    print()

    for dialog in dialogs:

        print("=" * 70)
        print(f"Название : {dialog.name}")
        print(f"ID        : {dialog.id}")
        print(f"Тип       : {type(dialog.entity).__name__}")

    await client.disconnect()


asyncio.run(main())