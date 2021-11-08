import os
from os import getenv
from dotenv import load_dotenv
from abhishek.snehabhi.uptools import fetch_heroku_git_url


if os.path.exists("local.env"):
    load_dotenv("local.env")
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_ID = int(getenv("OWNER_ID", "2070154667"))
OWNER_USERNAME = getenv("OWNER_USERNAME", "snehabhi_king")
BOT_USERNAME = getenv("BOT_USERNAME", "snehabhi_bot")
BOT_TOKEN = getenv("BOT_TOKEN", "token")
BG_IMAGE = getenv("BG_IMAGE", "https://te.legra.ph/file/5c1bd95f066aad81df745.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("SESSION_NAME", "session")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2070154667").split()))
DATABASE_URL = os.environ.get("DATABASE_URL")
