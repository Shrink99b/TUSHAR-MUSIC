import asyncio
import psutil

from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from program import __version__
from program.utils.inline import ping_ig
from driver.veez import user
from driver.filters import command, other_filters
from driver.database.dbchat import add_served_chat, is_served_chat
from pyrogram import Client, filters, __version__ as pyrover
from pyrogram.errors import FloodWait, MessageNotModified
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ChatJoinRequest

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""🥀 ʜᴇʏ  {message.from_user.mention()} ,

ᴛʜɪs ɪs {BOT_NAME}, 🖤
๏ ᴀ ғᴀsᴛ ᴀɴᴅ ᴩᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ᴩʟᴀʏᴇʀ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ᴀɴᴅ ᴜꜱᴇꜰᴜʟʟ ғᴇᴀᴛᴜʀᴇs.
๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴩ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs.
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥺 ᴀᴅᴅ ᴍᴇ ᴇʟꜱᴇ ʏᴏᴜ ɢᴇʏ 🥺",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "❄️ ꜱᴜᴘᴘᴏʀᴛ ❄️", url=f"https://t.me/lobe_ju"
                    ),
                    InlineKeyboardButton(
                        "✨ ᴜᴘᴅᴀᴛᴇꜱ ✨", url=f"https://t.me/oye_golgappu"
                    ),
                ],
                [
                    InlineKeyboardButton("💔 ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅꜱ 💔", callback_data="cbcmds"),
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


async def naina_ping():
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    fallen = f"""
✨ ᴜᴩᴛɪᴍᴇ : {uptime}
☁ ᴄᴩᴜ : {cpu}%
❄ ʀᴀᴍ : {mem}%
❤️‍🔥 ᴅɪsᴋ : {disk}%"""
    return fallen

@Client.on_message(filters.command(["ping", "alive", f"ping@{BOT_USERNAME}"]))
async def ping(_, message):
    hmm = await message.reply_photo(
        photo=f"https://te.legra.ph/file/96272a6bcbf5c3b32d6fd.jpg",
        caption="**» ᴩɪɴɢɪɴɢ ʙᴀʙʏ...**",
    )
    hehe = await naina_ping()
    start = datetime.now()
    end = datetime.now()
    resp = (end - start).microseconds / 1000
    await hmm.edit_text(
        f"**» ᴩᴏɴɢ ʙᴀʙʏ !**\n`☁ {resp}`ᴍs\n\n<b><u>{BOT_NAME} sʏsᴛᴇᴍ sᴛᴀᴛs :</u></b>{hehe}",
        reply_markup=ping_ig,
    )

@Client.on_chat_join_request()
async def approve_join_chat(c: Client, m: ChatJoinRequest):
    if not m.from_user:
        return
    try:
        await c.approve_chat_join_request(m.chat.id, m.from_user.id)
    except FloodWait as e:
        await asyncio.sleep(e.x + 2)
        await c.approve_chat_join_request(m.chat.id, m.from_user.id)


@Client.on_message(filters.new_chat_members)
async def new_chat(c: Client, m: Message):
    chat_id = m.chat.id
    if await is_served_chat(chat_id):
        pass
    else:
        await add_served_chat(chat_id)
    ass_uname = (await user.get_me()).username
    bot_id = (await c.get_me()).id
    for member in m.new_chat_members:
        if member.id == bot_id:
            return await m.reply(
                "❤️ Thanks for adding me to the **Group** !\n\n"
                "Appoint me as administrator in the **Group**, otherwise I will not be able to work properly, and don't forget to type `/userbotjoin` for invite the assistant.\n\n"
                "Once done, then type `/reload`",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("📣 Channel", url=f"https://t.me/{UPDATES_CHANNEL}"),
                            InlineKeyboardButton("💭 Support", url=f"https://t.me/{GROUP_SUPPORT}")
                        ],
                        [
                            InlineKeyboardButton("👤 Assistant", url=f"https://t.me/{ass_uname}")
                        ]
                    ]
                )
            )


chat_watcher_group = 5
