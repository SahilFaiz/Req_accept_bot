# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters, Client, errors, enums
from pyrogram.errors import UserNotParticipant
from pyrogram.errors.exceptions.flood_420 import FloodWait
from database import add_user, add_group, all_users, all_groups, users, remove_user, clear_all_data  # Assuming you have a function clear_all_data to clear DB
from configs import cfg
import random, asyncio
import os

app = Client(
    "approver",
    api_id=cfg.API_ID,
    api_hash=cfg.API_HASH,
    bot_token=cfg.BOT_TOKEN
)

# GIF links
gif = [
    'https://te.legra.ph/file/a1b3d4a7b5fce249902f7.mp4',
    'https://te.legra.ph/file/0c855143a4039108df602.mp4',
    'https://te.legra.ph/file/d7f3f18a92e6f7add8fcd.mp4',
    'https://te.legra.ph/file/9e334112ee3a4000c4164.mp4',
    'https://te.legra.ph/file/652fc39ae6295272699c6.mp4',
    'https://te.legra.ph/file/702ca8761c3fd9c1b91e8.mp4',
    'https://te.legra.ph/file/a1b3d4a7b5fce249902f7.mp4',
    'https://te.legra.ph/file/d7f3f18a92e6f7add8fcd.mp4',
    'https://te.legra.ph/file/0c855143a4039108df602.mp4',
    'https://te.legra.ph/file/9e334112ee3a4000c4164.mp4',
    'https://te.legra.ph/file/702ca8761c3fd9c1b91e8.mp4'
]

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_chat_join_request(filters.group | filters.channel & ~filters.private)
async def approve(_, m: Message):
    op = m.chat
    kk = m.from_user
    try:
        add_group(m.chat.id)
        await app.approve_chat_join_request(op.id, kk.id)
        add_user(kk.id)
    except errors.PeerIdInvalid as e:
        print("User isn't start bot (means group)")
    except Exception as err:
        print(str(err))    

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Start ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("start"))
async def op(_, m: Message):
    try:
        await app.get_chat_member(cfg.CHID, m.from_user.id)
        if m.chat.type == enums.ChatType.PRIVATE:
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🗯 Channel", url="https://t.me/amongusshe"),
                        InlineKeyboardButton("💬 Support", url="https://t.me/amongusshe")
                    ], [
                        InlineKeyboardButton("➕ Add me to your Chat ➕", url="https://t.me/vjmasterblastbot?startgroup")
                    ]
                ]
            )
            add_user(m.from_user.id)
            await m.reply_photo("https://i.ibb.co/LPJ1Jt2/Screenshot-2024-05-13-072256.png", caption="**🦊 Hello {}!\nI'm an auto approve [Admin Join Requests]({}) Bot.\nI can approve users in Groups/Channels. Add me to your chat and promote me to admin with add members permission.\n\n__Powered By : @amongusshe __**".format(m.from_user.mention, "https://t.me/telegram/153"), reply_markup=keyboard)

        elif m.chat.type == enums.ChatType.GROUP or enums.ChatType.SUPERGROUP:
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("💁‍♂️ Start me private 💁‍♂️", url="https://t.me/vjmasterblastbot?startgroup")
                    ]
                ]
            )
            add_group(m.chat.id)
            await m.reply_text("**🦊 Hello {}!\nWrite me in private for more details**".format(m.from_user.first_name), reply_markup=keyboard)
        print(m.from_user.first_name + " started your bot!")
    except UserNotParticipant:
        key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🍀 Check Again 🍀", "chk")
                ]
            ]
        )
        await m.reply_text("**⚠️Access Denied!⚠️\n\nPlease join @{} to use me. If you joined, click 'Check Again' to confirm.**".format(cfg.FSUB), reply_markup=key)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Get Database Command ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("getdb") & filters.user(cfg.SUDO))
async def send_database(_, m: Message):
    db_file = "database.db"  # Specify your database file path here
    if os.path.exists(db_file):
        await m.reply_document(db_file, caption="📁 Here is the current database file.")
    else:
        await m.reply_text("❌ Database file not found!")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Clear Database Command ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("cleardb") & filters.user(cfg.SUDO))
async def clear_database(_, m: Message):
    try:
        clear_all_data()  # Assuming this function clears the entire database
        await m.reply_text("✅ Database cleared successfully!")
    except Exception as e:
        await m.reply_text(f"❌ Failed to clear database: {e}")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Rest of the code (Broadcast, fcast, etc.) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# The rest of the code remains the same...

print("I'm Alive Now!")
app.run()
