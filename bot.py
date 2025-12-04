import logging
import asyncio
from dotenv import load_dotenv
import os

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

# Загружаем .env
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Логирование
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


# Команды -------------------------------------------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Бот работает. Готов к работе с расписанием.")


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Команды бота:\n/start — проверить, что бот жив\n/help — помощь")


# Главная функция запуска ---------------------------------------

async def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))

    await application.run_polling()


if __name__ == "__main__":
    asyncio.run(main())
