from pyrogram import Client
from pytgcalls import PyTgCalls



from abhishek.config import API_HASH, API_ID, STRING_SESSION

from abhishek.client.queues import queues

client = Client(STRING_SESSION, API_ID, API_HASH)
pytgcalls = PyTgCalls(client)


@pytgcalls.on_stream_end()

def on_stream_end(chat_id: int) -> None:
    queues.task_done(chat_id)

    if queues.is_empty(chat_id):
        await pytgcalls.leave_group_call(chat_id)
    else:
        pytgcalls.change_stream(
            chat_id, queues.get(chat_id)["file"])
            
        


run = pytgcalls.start
