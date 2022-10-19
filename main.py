import asyncio
from pytgcalls import idle
from driver.veez import call_py, bot, user


async def start_bot():
    await bot.start()
    print("[ɴᴀɪɴᴀ]: ɴᴀɪɴᴀ ᴍᴜꜱɪᴄ ʙᴏᴛ ᴀɴᴅ ᴀꜱꜱɪꜱᴛᴀɴᴛ ꜱᴛᴀʀᴛᴇᴅ !!")
    await call_py.start()
    print("[ɴᴀɪɴᴀ]: ᴘʏ-ᴛɢᴄᴀʟʟꜱ ꜱᴛᴀʀᴛᴇᴅ !!")
    await user.join_chat("lobe_ju")
    await user.join_chat("oye_golgappu")
    await idle()
    print("[ɴᴀɪɴᴀ]: ᴜꜰꜰ ꜱᴛᴏᴘɪɴɢ ʙᴏᴛ & ᴜʙᴏᴛ")
    await bot.stop()

loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
