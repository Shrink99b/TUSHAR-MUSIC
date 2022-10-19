# Copyright (C) 2021 By VeezMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🥀 ʜᴇʏ ʙᴀʙʏ, ᴛʜɪs ɪs {BOT_NAME}, 🖤


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


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **Basic Guide for using this bot:**

1.) **First, add me to your group.**
2.) **Then, promote me as administrator and give all permissions except Anonymous Admin.**
3.) **After promoting me, type /reload in group to refresh the admin data.**
3.) **Add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.**
4.) **Turn on the video chat first before start to play video/music.**
5.) **Sometimes, reloading the bot by using /reload command can help you to fix some problem.**

📌 **If the userbot not joined to video chat, make sure if the video chat already turned on, or type /userbotleave then type /userbotjoin again.**

💡 **If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🍂 **ʜᴇʏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» **ᴘʀᴇꜱꜱ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ʀᴇᴀᴅ ᴛʜᴇ ᴇxᴘʟᴀɪɴᴀᴛɪᴏɴ ᴀɴᴅ ꜱᴇᴇ ᴛʜᴇ ʟɪꜱᴛ ᴏꜰ ᴀᴡᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ !**

🍑 ᴘᴏᴡᴇʀᴇᴅ ʙʏ {BOT_NAME} """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ʙᴀꜱɪᴄ ᴄᴏᴍᴍᴀɴᴅ", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("ᴀᴅᴍɪɴ", callback_data="cbadmin"),
                    InlineKeyboardButton("ꜱᴜᴅᴏ", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("◁", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🍻 ʜᴇʀᴇ ɪꜱ ᴛʜᴇ ʙᴀꜱɪᴄ ᴄᴏᴍᴍᴀɴᴅꜱ:

» /play - ᴛᴏ ᴘʟᴀʏ ᴍᴜꜱɪᴄ ᴏɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ
» /stream - ᴛᴏ ꜱᴛʀᴇᴀᴍ ᴛʜᴇ ʏᴛ ʟɪᴠᴇ/ʀᴀᴅɪᴏ ʟɪᴠᴇ ᴍᴜꜱɪᴄ
» /vplay - ᴛᴏ ᴘʟᴀʏ ᴠɪᴅᴇᴏ ꜱᴏɴɢ ʙᴀʙʏ
» /vstream - ᴛᴏ  ᴘʟᴀʏ ᴠɪᴅᴇᴏ ꜰʀᴏᴍ ʏᴛ ʟɪᴠᴇ/m3u8
» /playlist - ꜱʜᴏᴡ ᴛʜᴇ ᴘʟᴀʏʟɪꜱᴛ
» /video - ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ ꜰʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ
» /song - ᴅᴏᴡɴʟᴏᴀᴅ ꜱᴏɴɢ ꜰʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ
» /lyric - ꜱᴄʀᴀᴘ ᴛʜᴇ ꜱᴏɴɢ ʟʏʀɪᴄꜱ
» /search - ꜱᴇᴀʀᴄʜ ᴀ ʏᴛ ᴠɪᴅᴇᴏ ʟɪɴᴋ ʙᴀʙʏ

» /ping - ꜱʜᴏᴡ ᴛʜᴇ ʙᴏᴛ ᴘɪɴɢ ꜱᴛᴀᴛᴜꜱ
» /uptime - ꜱʜᴏᴡ ᴛʜᴇ ʙᴏᴛ ᴜᴘᴛɪᴍᴇ ꜱᴛᴀᴛᴜꜱ

🍑 ᴘᴏᴡᴇʀᴇᴅ ʙʏ {BOT_NAME} """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("◁", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🍻 ʜᴇʀᴇ ɪꜱ ᴛʜᴇ ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅꜱ:

» /pause - ᴘᴀᴜꜱᴇ ᴛʜᴇ ꜱᴛʀᴇᴀᴍ
» /resume - ʀᴇꜱᴜᴍᴇ ᴛʜᴇ ꜱᴛʀᴇᴀᴍ
» /skip - ꜱᴡɪᴛᴄʜ ᴛᴏ ɴᴇxᴛ ꜱᴛʀᴇᴀᴍ
» /stop - ꜱᴛᴏᴘ ᴛʜᴇ ꜱᴛʀᴇᴀᴍɪɴɢ
» /vmute - ᴍᴜᴛᴇ ᴀꜱꜱɪꜱᴛᴀɴᴛ
» /vunmute - ᴜɴᴍᴜᴛᴇ ᴀꜱꜱɪꜱᴛᴀɴᴛ
» /volume `1-200` - ᴀᴅᴊᴜꜱᴛ ᴠᴏʟᴜᴍᴇ ᴏꜰ ᴍᴜꜱɪᴄ
» /reload - ʀᴇʟᴏᴀᴅ ᴀɴᴅ ʀᴇꜰʀᴇꜱʜ ᴛʜᴇ ʙᴏᴛ ʙᴀʙʏ
» /userbotjoin - ɪɴᴠɪᴛᴇ ᴛʜᴇ ᴜꜱᴇʀʙᴏᴛ ᴛᴏ ᴊᴏɪɴ ɢʀᴏᴜᴘ
» /userbotleave - ᴛᴏ ʟᴇᴀᴠᴇ ᴜꜱᴇʀʙᴏᴛ ꜰʀᴏᴍ ᴄʜᴀᴛ

🍑 ᴘᴏᴡᴇʀᴇᴅ ʙʏ {BOT_NAME} """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("◁", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🍻 ʜᴇʀᴇ ɪꜱ ᴛʜᴇ ꜱᴜᴅᴏ ᴄᴏᴍᴍᴀɴᴅꜱ:

» /rmw - ᴄʟᴇᴀɴ ᴀʟʟ ʀᴀᴡ ꜰɪʟᴇꜱ
» /rmd - ᴄʟᴇᴀɴ ᴀʟʟ ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ꜰɪʟᴇꜱ
» /update - ᴜᴘᴅᴀᴛᴇ ʏᴏᴜʀ ʙᴏᴛ ᴛᴏ ʟᴀᴛᴇꜱᴛ ᴠᴇʀꜱɪᴏɴ
» /restart - ʀᴇꜱᴛᴀʀᴛ ᴜʀ ʙᴏᴛ ʙᴀʙʏ
» /leaveall - ᴏʀᴅᴇʀ ᴜꜱᴇʀʙᴏᴛ ᴛᴏ ʟᴇᴀᴠᴇ ᴀʟʟ ᴄʜᴀᴛꜱ

🍑 ᴘᴏᴡᴇʀᴇᴅ ʙʏ {BOT_NAME} """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("◁", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **settings of** {query.message.chat.title}\n\n⏸ : pause stream\n▶️ : resume stream\n🔇 : mute userbot\n🔊 : unmute userbot\n⏹ : stop stream",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("🗑 Close", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    await query.message.delete()
