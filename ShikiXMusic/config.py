from os import getenv

que = {}
STRING_SESSION = getenv("STRING_SESSION", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ShikiXupdates")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/dcfdf612e499eef0e0b1f.png")
admins = {}
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "Shiki_Assistant")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "ShikiSupportChat")
PROJECT_NAME = getenv("PROJECT_NAME", "ShikiXMusic v0.1")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/Awesome-Gtash/ShikiXMusic")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
