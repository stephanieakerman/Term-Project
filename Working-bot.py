from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from config import bot_token
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('How are you? My name is Hassan.')

def main():
    # Replace 'YOUR_TOKEN' with the token you received from BotFather
    bot_token
    application = Application.builder().token(bot_token).build()

    # Add command handler for the start command
    application.add_handler(CommandHandler("start", start))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
