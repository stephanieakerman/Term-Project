import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from openai import OpenAI
from pathlib import Path
from config import API_KEY, bot_token

client = OpenAI(api_key=API_KEY)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Welcome! I can convert text to speech and speech to text. Send /text_to_speech <text> to convert text to speech, or send an audio message to convert speech to text.')

async def text_to_speech(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = " ".join(context.args)
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )
    speech_file_path = Path(__file__).parent / "output_voice.mp3"
    response.stream_to_file(speech_file_path)
    await update.message.reply_voice(voice=open(speech_file_path, 'rb'))

async def speech_to_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    file_id = update.message.voice.file_id
    file_path = await context.bot.get_file(file_id)
    downloaded_file = file_path.download()
    try:
        with open(downloaded_file, "rb") as audio_file:
            transcript = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                language="en"
            )
            await update.message.reply_text("Transcription: " + transcript.text)
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {e}")

def main():
    bot_token = "7110128418:AAFV-gIVQjdk0Vubm2aWy-Gpd01UIble5aU"
    application = Application.builder().token(bot_token).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("text_to_speech", text_to_speech))
    application.add_handler(CommandHandler("speech_to_text", speech_to_text))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
