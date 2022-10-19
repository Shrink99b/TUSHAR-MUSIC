from cache.admins import admins
from driver.veez import call_py, bot
from pyrogram import Client, filters
from driver.design.thumbnail import thumb
from driver.design.chatname import CHAT_TITLE
from driver.queues import QUEUE, clear_queue
from driver.filters import command, other_filters
from driver.decorators import authorized_users_only
from driver.utils import skip_current_song, skip_item
from program.utils.inline import (
    stream_markup,
    close_mark,
)
from config import BOT_USERNAME, GROUP_SUPPORT, IMG_5, UPDATES_CHANNEL
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)


@Client.on_message(command(["reload", f"reload@{BOT_USERNAME}"]) & other_filters)
@authorized_users_only
async def update_admin(client, message):
    global admins
    new_admins = []
    new_ads = await client.get_chat_members(message.chat.id, filter="administrators")
    for u in new_ads:
        new_admins.append(u.user.id)
    admins[message.chat.id] = new_admins
    await message.reply_text(
        "**» ᴀᴅᴍɪɴ ᴄᴀᴄʜᴇ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ʀᴇꜰʀᴇꜱʜᴇᴅ ʙᴀʙʏ**"
    )


@Client.on_message(command(["skip", f"skip@{BOT_USERNAME}", "vskip"]) & other_filters)
@authorized_users_only
async def skip(c: Client, m: Message):
    await m.delete()
    user_id = m.from_user.id
    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await c.send_message(chat_id, "» ɴᴏᴛʜɪɴɢ ɪꜱ ᴄᴜʀʀᴇɴᴛʟʏ ᴘʟᴀʏɪɴɢ .")
        elif op == 1:
            await c.send_message(chat_id, "» ᴛʜᴇʀᴇ ɪꜱ ɴᴏ ᴍᴏʀᴇ ᴍᴜꜱɪᴄ ɪɴ ϙᴜᴇᴜᴇ ʙᴀʙʏ.")
        elif op == 2:
            await c.send_message(chat_id, "» ᴄʟᴇᴀʀɪɴɢ ᴛʜᴇ **ϙᴜᴇᴜᴇꜱ**\n\n**• ᴜꜱᴇʀʙᴏᴛ** ʟᴇᴀᴠɪɴɢ ᴠᴄ ʙᴀʙʏ.")
        else:
            buttons = stream_markup(user_id)
            requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
            thumbnail = f"{IMG_5}"
            title = f"{op[0]}"
            userid = m.from_user.id
            gcname = m.chat.title
            ctitle = await CHAT_TITLE(gcname)
            image = await thumb(thumbnail, title, userid, ctitle)
            await c.send_photo(
                chat_id,
                reply_markup=InlineKeyboardMarkup(buttons),
                caption=f"➻ ᴛʀᴀᴄᴋ ꜱᴋɪᴘᴘᴇᴅ ʙᴀʙʏ \n❄️ **ɴᴀᴍᴇ:** [{op[0]}]({op[1]})\n☁️ **ᴄʜᴀᴛ:** `{chat_id}`\n✨ **ʀᴇϙᴜᴇꜱᴛᴇᴅ ʙʏ:** {requester}",
            )
    else:
        skip = m.text.split(None, 1)[1]
        OP = "❄️ **ʀᴇᴍᴏᴠᴇᴅ ꜱᴏɴɢ ꜰʀᴏᴍ ϙᴜᴇᴜᴇᴅ:**"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x == 0:
                    pass
                else:
                    hm = await skip_item(chat_id, x)
                    if hm == 0:
                        pass
                    else:
                        OP = OP + "\n" + f"**#{x}** - {hm}"
            await m.reply(OP)


@Client.on_message(
    command(["stop", f"stop@{BOT_USERNAME}", "end", f"end@{BOT_USERNAME}", "vstop"])
    & other_filters
)
@authorized_users_only
async def stop(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await m.reply("» ᴜꜱᴇʀʙᴏᴛ ᴅɪꜱᴄᴏɴɴᴇᴄᴛᴇᴅ ꜰʀᴏᴍ ᴛʜᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ.")
        except Exception as e:
            await m.reply(f"🚫 **error:**\n\n`{e}`")
    else:
        await m.reply("» **ɴᴏᴛʜɪɴɢ ɪꜱ ᴄᴜʀʀᴇɴᴛʟʏ ꜱᴛʀᴇᴀᴍɪɴɢ ʙᴀʙʏ**")


@Client.on_message(
    command(["pause", f"pause@{BOT_USERNAME}", "vpause"]) & other_filters
)
@authorized_users_only
async def pause(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await m.reply(
                "» **ᴛʀᴇᴀᴄᴋ ᴘᴀᴜꜱᴇᴅ ʙᴀʙʏ. 🥺**"
            )
        except Exception as e:
            await m.reply(f"🚫 **ᴇʀʀᴏʀ:**\n\n`{e}`")
    else:
        await m.reply("» **ɴᴏᴛʜɪɴɢ ɪꜱ ꜱᴛʀᴇᴀᴍɪɴɢ ʙᴀʙʏ**")


@Client.on_message(
    command(["resume", f"resume@{BOT_USERNAME}", "vresume"]) & other_filters
)
@authorized_users_only
async def resume(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await m.reply(
                "» **ᴛʀᴀᴄᴋ ʀᴇꜱᴜᴍᴇᴅ ʙᴀʙʏ. ✨**"
            )
        except Exception as e:
            await m.reply(f"🚫 **ᴇʀʀᴏʀ:**\n\n`{e}`")
    else:
        await m.reply("» **ɴᴏᴛʜɪɴɢ ɪꜱ ᴘʟᴀʏɪɴɢ ʙᴀʙʏ**")


@Client.on_message(
    command(["mute", f"mute@{BOT_USERNAME}", "vmute"]) & other_filters
)
@authorized_users_only
async def mute(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.mute_stream(chat_id)
            await m.reply(
                "» **ᴀꜱꜱɪꜱᴛᴀɴᴛ ᴍᴜᴛᴇᴅ ʙᴀʙʏ. 🥺**"
            )
        except Exception as e:
            await m.reply(f"🚫 **ᴇʀʀᴏʀ:**\n\n`{e}`")
    else:
        await m.reply("» **ɴᴏᴛʜɪɴɢ ɪꜱ ᴘʟᴀʏɪɴɢ ʙᴀʙʏ**")


@Client.on_message(
    command(["unmute", f"unmute@{BOT_USERNAME}", "vunmute"]) & other_filters
)
@authorized_users_only
async def unmute(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.unmute_stream(chat_id)
            await m.reply(
                "» **ᴀꜱꜱɪꜱᴛᴀɴᴛ ᴜɴᴍᴜᴛᴇᴅ ʙᴀʙʏ. ✨**"
            )
        except Exception as e:
            await m.reply(f"🚫 **ᴇʀʀᴏʀ:**\n\n`{e}`")
    else:
        await m.reply("» **ɴᴏᴛʜɪɴɢ ɪꜱ ᴘʟᴀʏɪɴɢ ʙᴀʙʏ**")


@Client.on_message(
    command(["volume", f"volume@{BOT_USERNAME}", "vol"]) & other_filters
)
@authorized_users_only
async def change_volume(client, m: Message):
    range = m.command[1]
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.change_volume_call(chat_id, volume=int(range))
            await m.reply(
                f"» **ᴠᴏʟᴜᴍᴇ ꜱᴇᴛ ᴛᴏ** `{range}`%"
            )
        except Exception as e:
            await m.reply(f"🚫 **ᴇʀʀᴏʀ:**\n\n`{e}`")
    else:
        await m.reply("» **ɴᴏᴛʜɪɴɢ ɪꜱ ᴘʟᴀʏɪɴɢ ʙᴀʙʏ**")
