import os
from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, filters, ContextTypes
from openai import OpenAI
from pathlib import Path
from config import API_KEY, bot_token

client = OpenAI(api_key=API_KEY)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Welcome! Please send me a text to convert it to speech, or send me an audio message to convert it to text.')

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )
    speech_file_path = Path(__file__).parent / "output_voice.mp3"
    response.stream_to_file(speech_file_path)
    with open(speech_file_path, 'rb') as voice:
        await update.message.reply_voice(voice=voice)
    os.remove(speech_file_path)

async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    file_id = update.message.voice.file_id
    print(file_id)
    file = await context.bot.get_file(file_id)
    file_path = file.file_path
    print(file_path)

    # Now download the file using the URL
    await file.download(file_path)
    try:
        with open(file_path, "rb") as audio_file:
            transcript = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                language="en"
            )
            await update.message.reply_text("Transcription: " + transcript['text'])
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {e}")
    finally:
        os.remove(downloaded_file)

def main():
    application = Application.builder().token(bot_token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    application.add_handler(MessageHandler(filters.VOICE, handle_voice))

    application.run_polling()

if __name__ == '__main__':
    main()
