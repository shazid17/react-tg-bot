# -*- coding: utf-8 -*-
# Reaction Bot - Free/Premium
# Install: pip install -U python-telegram-bot
# Run: python Reaction-bot.py

import logging
import random
import os

from telegram import (
    Update,
    ReactionTypeEmoji,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.error import TelegramError
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)

# নতুন BotFather Token এখানে বসাও
BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()

UPDATE_CHANNEL = "https://t.me/spdfairyappi"
OWNER_URL = "https://t.me/ShamimLeader"

REACTIONS = [
    "👍", "👎", "❤️", "🔥", "🥰", "👏", "😁",
    "🤔", "🤯", "😱", "🤬", "😢", "🎉", "🤩",
    "🤮", "💩", "🙏", "👌", "🕊", "🤡", "🥱",
    "🥴", "😍", "🐳", "❤️‍🔥", "🌚", "🌭", "💯",
    "🤣", "⚡️", "🍌", "🏆", "💔", "🤨", "😐",
    "🍓", "🍾", "💋", "😈", "😴", "😭", "🤓",
    "👻", "👨‍💻", "👀", "🎃", "🙈", "😇", "😨",
    "🤝", "✍️", "🤗", "🫡", "🎅", "🎄", "☃️",
    "💅", "🤪", "🗿", "🆒", "💘", "🙉", "🦄",
    "😘", "🙊", "😎", "👾", "🤷", "😡"
]

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger(name)


def main_menu():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "🆓 Free Plan", callback_data="free"
            ),
            InlineKeyboardButton(
                "♻️ Premium Plan", callback_data="premium"
            )
        ],
        [
            InlineKeyboardButton(
                "📢 Update Channel", url=UPDATE_CHANNEL
            ),
            InlineKeyboardButton(
                "👤 Owner", url=OWNER_URL
            )
        ],
        [
            InlineKeyboardButton(
                "📖 Help", callback_data="help"
            )
        ]
    ])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message
    user = update.effective_user

    if not message or not user:
        return

    welcome = (
        f"👋 স্বাগতম, {user.first_name or 'বন্ধু'}!\n\n"
        "🤖 আমি Auto Reaction Bot।\n\n"
        "✨ সুবিধাসমূহ:\n"
        "• গ্রুপে অটো রিঅ্যাকশন\n"
        "• চ্যানেল পোস্টে অটো রিঅ্যাকশন\n"
        "• বিভিন্ন ইমোজি থেকে র‍্যান্ডম রিঅ্যাকশন\n"
        "• Free ও Premium মেনু\n"
        "• Help ও Owner বাটন\n\n"
        "👇 নিচের মেনু থেকে একটি অপশন বেছে নিন।"
    )

    # ব্যবহারকারীর প্রোফাইল ছবি পাওয়া গেলে সেটি দেখাবে
    try:
        photos = await context.bot.get_user_profile_photos(
            user.id, limit=1
        )

        if photos.total_count and photos.photos:
            await message.reply_photo(
                photo=photos.photos[0][-1].file_id,
                caption=welcome,
                reply_markup=main_menu()
            )
            return

    except TelegramError as error:
        logger.warning("Profile photo unavailable: %s", error)

    await message.reply_text(
        welcome,
        reply_markup=main_menu()
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message

    if not message:
        return

    await message.reply_text(
        "📖 ব্যবহারবিধি\n\n"
        "১. বটকে গ্রুপে যোগ করুন।\n"
        "২. চ্যানেলে বটকে Admin করুন।\n"
        "৩. প্রয়োজনীয় Reaction Permission দিন।\n"
        "৪. নতুন পোস্টে বট রিঅ্যাক্ট করার চেষ্টা করবে।\n\n"
        "কমান্ড:\n"
        "/start - মূল মেনু\n"
        "/help - ব্যবহারবিধি\n"
        "/react 👍 - Reply করা মেসেজে রিঅ্যাকশন\n\n"
        "⚠️ Telegram-এর অনুমতি, API সীমা ও মেসেজ "
        "পৌঁছানোর ওপর রিঅ্যাকশন নির্ভর করে।",
        reply_markup=main_menu()
    )


async def menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    if not query:
        return

    await query.answer()
if query.data == "free":
        text = (
            "🆓 FREE PLAN\n\n"
            "✓ অটো রিঅ্যাকশন\n"
            "✓ র‍্যান্ডম ইমোজি\n"
            "✓ গ্রুপ ও চ্যানেলে রিঅ্যাকশনের চেষ্টা\n"
            "✓ Help সিস্টেম\n\n"
            "Telegram-এর অনুমতি প্রযোজ্য।"
        )

    elif query.data == "premium":
        text = (
            "💎 PREMIUM PLAN\n\n"
            "Premium পেমেন্ট ও সাবস্ক্রিপশন সিস্টেম "
            "এখনো যুক্ত করা হয়নি।\n\n"
            "যোগাযোগ: @ShamimLeader"
        )

    else:
        text = (
            "📖 বটকে গ্রুপে যোগ করুন অথবা চ্যানেলে Admin করুন। "
            "প্রয়োজনীয় অনুমতি থাকলে নতুন পোস্টে রিঅ্যাক্ট করবে।"
        )

    try:
        if query.message and query.message.photo:
            await query.edit_message_caption(
                caption=text,
                reply_markup=main_menu()
            )
        else:
            await query.edit_message_text(
                text=text,
                reply_markup=main_menu()
            )

    except TelegramError as error:
        logger.warning("Menu update failed: %s", error)


async def add_reaction(message):
    if not message:
        return

    if message.from_user and message.from_user.is_bot:
        return

    emoji = random.choice(REACTIONS)

    try:
        await message.set_reaction(
            reaction=[ReactionTypeEmoji(emoji=emoji)],
            is_big=False
        )

        logger.info(
            "Reaction %s added | Chat %s | Message %s",
            emoji, message.chat_id, message.message_id
        )

    except TelegramError as error:
        logger.warning(
            "Reaction failed | Chat %s | Message %s | %s",
            message.chat_id, message.message_id, error
        )


async def auto_react(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message

    if message:
        await add_reaction(message)


async def manual_react(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message

    if not message:
        return

    if not message.reply_to_message:
        await message.reply_text(
            "একটি মেসেজে Reply করে /react 👍 লিখুন।"
        )
        return

    emoji = context.args[0] if context.args else random.choice(REACTIONS)

    if emoji not in REACTIONS:
        await message.reply_text(
            "এই ইমোজিটি তালিকায় নেই। /help দেখুন।"
        )
        return

    try:
        await message.reply_to_message.set_reaction(
            reaction=[ReactionTypeEmoji(emoji=emoji)],
            is_big=False
        )
        await message.reply_text(f"✅ রিঅ্যাকশন: {emoji}")

    except TelegramError as error:
        await message.reply_text(
            f"❌ রিঅ্যাকশন দেওয়া যায়নি: {error}"
        )


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.error("Update error: %s", context.error)


def main():
    if not BOT_TOKEN:
        raise SystemExit(
            "ERROR: Render Environment-এ BOT_TOKEN সেট করো।"
        )

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("react", manual_react))
    app.add_handler(CallbackQueryHandler(menu_callback))

    # Telegram যে ধরনের মেসেজ বটকে পাঠাবে,
    # সেগুলোতে অটো রিঅ্যাকশন দেওয়ার চেষ্টা করবে।
    app.add_handler(
        MessageHandler(
            filters.ALL & ~filters.COMMAND,
            auto_react
        )
    )

    app.add_error_handler(error_handler)

    logger.info("Reaction Bot is starting...")

    app.run_polling(
        allowed_updates=Update.ALL_TYPES
    )


if name == "main":
    main()




