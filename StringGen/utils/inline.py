from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import SUPPORT_CHAT

keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="🐣 ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ 🐣", callback_data="gensession")],
        [
            InlineKeyboardButton(text="📢 ᴜᴘᴅᴀᴛᴇꜱ", url=SUPPORT_CHAT),
            InlineKeyboardButton(text="💸 ᴅᴇᴠ", url="https://telegram.me/Mr_RoleXG"),
        ],
    ]
)

gen_key = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="🔮 ᴩʏʀᴏɢʀᴀᴍ v1", callback_data="pyrogram1")],
        [InlineKeyboardButton(text="🔮 ᴩʏʀᴏɢʀᴀᴍ v2", callback_data="pyrogram")],
        [InlineKeyboardButton(text="🔮 ᴛᴇʟᴇᴛʜᴏɴ", callback_data="telethon")],
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="ᴛʀʏ ᴀɢᴀɪɴ", callback_data="gensession")]]
)
