# pip install python-telegram-bot

import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name
    eto_text = f"драсте {user} вас приветствует супер бот"
    await update.message.reply_text(eto_text)
#  Обработчик текстовых сообщений
async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f"вы написали {text}")

# Оброботчик ошибок 
async def error_hand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Ошибка")
    if update and update.effective_message:
        await update.message.reply_text("произошла ошибка")


TOKEN = "7834105429:AAHdc0YMtIzGlXSedIz7ArhIijMlZ2tHdEg" # его можно получить через бота botfather

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler)) # оброботчик сообщений 

    app.add_error_handler(error_hand) # оброботчик ошибок
    print("тик")
    print("Удачно!")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()