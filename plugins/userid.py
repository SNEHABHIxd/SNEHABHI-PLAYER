from pyrogram import Client
from pyrogram.types import Message

from abhishek import config
from abhishek.snehabhi.filters import command
from abhishek.snehabhi.get_file_id import get_file_id


@Client.on_message(command(["id", f"id@{BOT_USERNAME}"]))
async def showid(_, message: Message):
    chat_type = message.chat.type

    if chat_type == "private":
        user_id = message.chat.id
        await message.reply_text(f"<code>{user_id}</code>")

    elif chat_type in ["group", "supergroup"]:
        _id = ""
        _id += "<b>𝙶𝚁𝙾𝚄𝙿 𝙸𝙳</b>: " f"<code>{message.chat.id}</code>\n"
        if message.reply_to_message:
            _id += (
                "<b>Replied 𝚄𝚂𝙴𝚁 𝙸𝙳</b>: "
                f"<code>{message.reply_to_message.from_user.id}</code>\n"
            )
            file_info = get_file_id(message.reply_to_message)
        else:
            _id += "<b>𝚄𝚂𝙴𝚁 𝙸𝙳</b>: " f"<code>{message.from_user.id}</code>\n"
            file_info = get_file_id(message)
        if file_info:
            _id += (
                f"<b>{file_info.message_type}</b>: "
                f"<code>{file_info.file_id}</code>\n"
            )
        await message.reply_text(_id)
