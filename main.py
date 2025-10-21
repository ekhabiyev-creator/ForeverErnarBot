import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("Environment variable BOT_TOKEN is not set. Set it to your bot token.")

PDF_KZ = "https://disk.yandex.kz/i/NFxkMlOet-35cw"
PDF_RU = "https://disk.yandex.kz/i/qVxolrwZqxEI4Q"
WHATSAPP = "https://wa.me/77786576929"
REF_LINK = "https://flpkaz.com/ref/007004130661"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📘 Каталог", callback_data="catalog")],
        [InlineKeyboardButton("💼 Заработок с пользой", callback_data="earn")],
        [InlineKeyboardButton("📋 Регистрация", url=REF_LINK)],
        [InlineKeyboardButton("📞 Байланыс / Связаться", url=WHATSAPP)],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    text = (
        "🌿 Сәлем! / Привет!\n"
        "Мен Ернармын, Forever Living серіктесімін 💚\n"
        "Я — партнёр компании Forever Living Products.\n\n"
        "Мұнда сіз табыс пен денсаулықты біріктіре аласыз 🌱\n"
        "Здесь можно зарабатывать с пользой для здоровья 🌿\n\n"
        "Таңдаңыз / Выберите:"
    )

    if update.message:  # если команда /start
        await update.message.reply_text(text, reply_markup=reply_markup)
    elif update.callback_query:  # если кнопка "Назад"
        await update.callback_query.edit_message_text(text, reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "catalog":
        keyboard = [
            [InlineKeyboardButton("🇰🇿 Қазақша", url=PDF_KZ)],
            [InlineKeyboardButton("🇷🇺 Русский", url=PDF_RU)],
            [InlineKeyboardButton("⬅️ Назад", callback_data="back")],
        ]
        await query.edit_message_text("Тілді таңдаңыз / Выберите язык:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == "earn":
        text = (
            "💼 *Заработок с пользой!*\n\n"
            "Вы можете стать партнёром Forever Living и получать доход, рекомендуя продукцию 🌿\n"
            "Подробнее — через кнопку регистрации 👇"
        )
        keyboard = [
            [InlineKeyboardButton("📋 Регистрация", url=REF_LINK)],
            [InlineKeyboardButton("⬅️ Назад", callback_data="back")],
        ]
        await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif data == "back":
        # Возврат в главное меню
        await start(update, context)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    print("🤖 ForeverErnarBot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()
