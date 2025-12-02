from telegram.ext import CommandHandler

def register_handler(update, context):
    update.message.reply_text("Регистрация пока не активна")
