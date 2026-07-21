from telegram import Update
from telegram.ext import ContextTypes

from keyboards import join_keyboard, main_menu
from config import CHANNEL_USERNAME
from database import add_user


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user

    add_user(
        user.id,
        user.first_name,
        user.username
    )

    member = await context.bot.get_chat_member(
        CHANNEL_USERNAME,
        user.id
    )

    if member.status in [
        "member",
        "administrator",
        "creator"
    ]:

        await update.message.reply_text(
            "🎉 خوش اومدی!\n\nیکی از گزینه‌های زیر را انتخاب کن.",
            reply_markup=main_menu()
        )

    else:

        await update.message.reply_text(
            "❌ برای استفاده از ربات ابتدا عضو کانال شوید.",
            reply_markup=join_keyboard()
        )
