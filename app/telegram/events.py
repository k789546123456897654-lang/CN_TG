from app.telegram.router import MessageRouter

router = MessageRouter()


async def handle_new_message(event):

    await router.process(event)