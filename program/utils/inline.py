""" inline section button """

from pyrogram.types import (
  CallbackQuery,
  InlineKeyboardButton,
  InlineKeyboardMarkup,
  Message,
)


def stream_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="• ꜱᴜᴘᴘᴏʀᴛ •", url=f"https://telegram.me/Lobe_ju"),
      InlineKeyboardButton(text="• ᴜᴘᴅᴀᴛᴇ •", url=f"https://telegram.me/oye_golgappu"),
    ],
    [
      InlineKeyboardButton(text="• ᴄʟᴏꜱᴇ •", callback_data=f'cls'),
    ],
  ]
  return buttons


close_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "🗑 Close", callback_data="cls"
      )
    ]
  ]
)


ping_ig = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="sᴜᴩᴩᴏʀᴛ",
                    url=f"https://t.me/lobe_ju"
                ),
                InlineKeyboardButton(
                    text="ᴄʟᴏꜱᴇ", callback_data="cls"
                )
            ]
        ]
    )

