import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Команда /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привет! Я твой бот для расписания сомелье.")

# Команда /schedule (пока заглушка)
def schedule(update: Update, context: CallbackContext):
    update.message.reply_text("Здесь будет расписание сомелье.")

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("schedule", schedule))

# Запуск бота
updater.start_polling()
updater.idle()
