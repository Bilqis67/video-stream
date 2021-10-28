import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "𝐂𝐥𝐨𝐯𝐞𝐫 𝐕𝐢𝐝𝐞𝐨 𝐒𝐭𝐫𝐞𝐚𝐦")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "psycholy9")
ALIVE_NAME = getenv("ALIVE_NAME", "Choky")
BOT_USERNAME = getenv("BOT_USERNAME", "clovervideostreambot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "𝓑𝓵𝓪𝓬𝓴 𝓒𝓵𝓸𝓿𝓮𝓻")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "anjingsinijoin")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "GalleryClover")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/92674c567ef7eb72521d2.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/9aa0eb8e4703e6a1d94d7.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/84568c753c738d7cfed46.png")
