import asyncio
from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant

from abhishek.Client.callsmusic import client as abhi
from abhishek.config import SUDO_USERS

@Client.on_message(filters.command(["gcast"]))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("`𝚂𝚃𝙰𝚁𝚃𝙸𝙽𝙶 𝙱𝚁𝙾𝙰𝙳𝙲𝙰𝚂𝚃 ...`")
        if not message.reply_to_message:
            await wtf.edit("**__𝙿𝙻𝙴𝙰𝚂𝙴 𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙼𝚂𝙶 𝚃𝙾 𝚂𝚃𝙰𝚁𝚃 𝙱𝚁𝙾𝙰𝙳𝙲𝙰𝚂𝚃...__**")
            return
        lmao = message.reply_to_message.text
        async for dialog in aditya.iter_dialogs():
            try:
                await aditya.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"`𝙱𝚁𝙾𝙰𝙳𝙲𝙰𝚂𝚃𝙸𝙽𝙶` \n\n**𝚂𝙴𝙽𝚃 𝚃𝙾:** `{sent}` Ƈɦɑts \n**𝙵𝙰𝙸𝙻𝙴𝙳 𝙸𝙽:** {failed} chats")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await message.reply_text(f"`𝙶𝙲𝙰𝚂𝚃 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈` \n\n**𝚂𝙴𝙽𝚃 𝚃𝙾:** `{sent}` Ƈɦɑts \n**𝙵𝙰𝙸𝙻𝙴𝙳 𝙸𝙽:** {failed} Ƈɦɑts")
