from telegram.ext import CommandHandler

def schedule_handler(update, context):
    update.message.reply_text("Здесь будет расписание")
