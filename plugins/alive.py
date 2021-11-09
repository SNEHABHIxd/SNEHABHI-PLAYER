import asyncio
from time import time
from datetime import datetime
from abhishek.config import BOT_USERNAME
from abhishek.snehabhi.filters import command
from abhishek.snehabhi.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/c6e1041c6c9a12913f57a.png",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
💥 𝙷𝙴𝙻𝙻𝙾 𝙸'𝙼 𝚂𝙽𝙴𝙷𝙰𝙱𝙷𝙸 𝙼𝚄𝚂𝙸𝙲 𝙿𝙻𝙰𝚈𝙴𝚁.....
𝙿𝙻𝙰𝚈 𝙼𝚄𝚂𝙸𝙲 𝙵𝙾𝚁 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙶𝚁𝙾𝚄𝙿𝚂 𝙰𝙽𝙳 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ...
┏━━━━━━━━━━━━━━━━━┓
┣★ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁 𝙺𝙸𝙽𝙶 : [𝙼𝚁. 𝙰𝙱𝙷𝙸𝚂𝙷𝙴𝙺](https://t.me/SNEHABHI_KING)
┣★ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁 𝚀𝚄𝙴𝙴𝙽 : [𝚂𝙽𝙴𝙷𝚄 𝚀𝚄𝙴𝙴𝙽](https://t.me/ABHI_IZ_MINE)
┣★ 𝚄𝙿𝙳𝙰𝚃𝙴𝚂 : [𝚂𝙽𝙴𝙷𝙰𝙱𝙷𝙸 𝚄𝙿𝙳𝙰𝚃𝙴𝚂](https://t.me/adityaserver)
┣★ 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 : [𝚂𝙽𝙴𝙷𝙰𝙱𝙷𝙸 𝚂𝚄𝙿𝙿𝙾𝚁𝚃](https://t.me/adityadiscus)
┣★ 𝚁𝙴𝙿𝙾 › : [𝚂𝙽𝙴𝙷𝙰𝙱𝙷𝙸 𝚁𝙴𝙿𝙾](https://github.com/SNEHABHIxd/SNEHABHI-PLAYER)
┗━━━━━━━━━━━━━━━━━┛
💞 𝙸𝙵 𝚈𝙾𝚄 𝙷𝙰𝚅𝙴 𝙵𝙰𝙲𝙴𝙳 𝙰𝙽𝚈 𝙸𝚂𝚂𝚄𝙴
𝙳𝙼 𝚃𝙾 𝙼𝚈 [𝙾𝚆𝙽𝙴𝚁](https://t.me/ABHI_IZ_MINE) ...
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ 𝙶𝚁𝙾𝚄𝙿 𝙼𝙴 𝙳𝙰𝙻𝙳𝙾 𝙳𝙴𝙺𝙷𝙾 𝙼𝚃 ➕", url=f"https://t.me/SNEHABHI_BOT?startgroup=true")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "snehabhi"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/bc6ecaac6eb57cb10342c.png",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 𝙹𝙾𝙸𝙽 𝚂𝙽𝙴𝙷𝙰𝙱𝙷𝙸 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 💞", url=f"https://t.me/SNEHABHI_SERVER")
                ,
                        "💥 𝙹𝙾𝙸𝙽 𝚂𝙽𝙴𝙷𝙰𝙱𝙷𝙸 𝚄𝙿𝙳𝙰𝚃𝙴𝚂 💞", url=f"https://t.me/SNEHABHI_UPDATES")
                ],[
                  
                   InlineKeyboardButton(
                       " 𝙲𝚁𝙴𝙰𝚃𝙾𝚁 𝚀𝚄𝙴𝙴𝙽 ", url=f"https://t.me/ABHI_IZ_MINE")
                ],[
                  InlineKeyboardButton(
                      " 𝙲𝚁𝙴𝙰𝚃𝙾𝚁 𝙺𝙸𝙽𝙶 ", url=f"https://t.me/SNEHABHI_KING")
                ],[
                  InlineKeyboardButton(
                     "𝙹𝙾𝙸𝙽 𝙼𝙰𝚂𝚃𝙸 𝙶𝚁𝙾𝚄𝙿",url=f"https://t.me/LIVE_LIFE_LIKE")
            ]
            ]
        ),
    )


@Client.on_message(command(["repo", "#repo", "@repo", "/repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/5c1bd95f066aad81df745.png",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 𝙲𝙻𝙸𝙲𝙺 𝙷𝙴𝚁𝙴 𝙾𝙿 𝙱𝙾𝚃𝚉 𝚁𝙴𝙿𝙾 💞", url=f"https://github.com/SNEHABHIxd/SNEHABHI-PLAYER")
                ]
            ]
        ),
    )
