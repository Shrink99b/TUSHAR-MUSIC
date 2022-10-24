import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQBdX45O32U4_s0IkqdVCr0WQrc21IGsZYsKrNLrFxrN5tzyv2bx-bywP9EVNESKOAIhGOfnIxtSx2YsRQeSnlNhblX8bgnUClf62-b_mHNtUmF33OUMTQs2ZHF90SGtCW5Y-qPM6sebc12fxO-mFMumEqfV1EFNPcSz99YqvfK2RF1NG7I-TjUdGRH_38a-srIp3L29KeumijcyosBcDiiiI6L1w9jvMAesPVBsdv6egF7sDMxPiu7ybODfWeHzdpajOtxPe-IPfEuURTG7Yuq3USmvwiXaYf8t1shOou2K_u1tJmVrIpSKUPotU2P36xmqZqnG5EM_MJVA7eiBNuqZAAAAAUKJOPcA")
BOT_TOKEN = getenv("BOT_TOKEN", "5704225630:AAG-jZu3ytLA3FoiGLU7URoUKTauatyoyiQ")
BOT_NAME = getenv("BOT_NAME", "🎼🥀🫧˹Gαввαя ✘ ʙᴏᴛ ˼🫧🥀 🎼")
API_ID = int(getenv("API_ID", "15890322"))
API_HASH = getenv("API_HASH", "be46a37d46470b49b6eb77e05fe20014")
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://Devarora0987:#Dev12345@cluster0.razivtc.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "GABBAR_DAD_KAAL")
ALIVE_NAME = getenv("ALIVE_NAME", "Gαввαя ✘")
BOT_USERNAME = getenv("BOT_USERNAME", "GABBARMUSICBOT_OP_BOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "ll_LEGENDX_MR_GABBAR_ll")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "ll_OFFICIAL_LEGENDBOY_ll")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ll_ll_LegendHacker_IN_ll_ll")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5783419520").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/6db887251dd539777da8c.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "4908"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/DEVELOPER-XD/GABBAR-X-FIX-BOT")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/6db887251dd539777da8c.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/6db887251dd539777da8c.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/6db887251dd539777da8c.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/6db887251dd539777da8c.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/6db887251dd539777da8c.jpg")
