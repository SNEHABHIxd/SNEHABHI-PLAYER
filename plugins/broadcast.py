import asyncio
from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant

from abhishek.client.callsmusic import client as abhi
from abhishek.config import SUDO_USERS

@Client.on_message(filters.command(["gcast"]))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("`πππ°πππΈπ½πΆ π±ππΎπ°π³π²π°ππ ...`")
        if not message.reply_to_message:
            await wtf.edit("**__πΏπ»π΄π°ππ΄ ππ΄πΏπ»π ππΎ πΌππΆ ππΎ πππ°ππ π±ππΎπ°π³π²π°ππ...__**")
            return
        lmao = message.reply_to_message.text
        async for dialog in aditya.iter_dialogs():
            try:
                await aditya.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"`π±ππΎπ°π³π²π°πππΈπ½πΆ` \n\n**ππ΄π½π ππΎ:** `{sent}` ΖΙ¦Ιts \n**π΅π°πΈπ»π΄π³ πΈπ½:** {failed} chats")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await message.reply_text(f"`πΆπ²π°ππ πππ²π²π΄πππ΅ππ»π»π` \n\n**ππ΄π½π ππΎ:** `{sent}` ΖΙ¦Ιts \n**π΅π°πΈπ»π΄π³ πΈπ½:** {failed} ΖΙ¦Ιts")
