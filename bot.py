import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

# Создаём приложение бота
app = ApplicationBuilder().token(BOT_TOKEN).build()

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я твой бот для расписания сомелье.")

# Команда /schedule
async def schedule(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Здесь будет расписание сомелье.")

# Регистрируем команды
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("schedule", schedule))

# Запуск бота
app.run_polling()
