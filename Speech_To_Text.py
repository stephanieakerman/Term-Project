from config import API_KEY
from openai import OpenAI

client = OpenAI(api_key=API_KEY)

# The file for the audio
file_path = "Hello_Voice.mp3"

def transcribe_audio(file_path):
    try:
        with open(file_path, "rb") as audio_file:
            transcript = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                language="en"
            )
            return transcript.text
    except Exception as e:
        return f"An error occurred: {e}"

# Result
transcription = transcribe_audio(file_path)
print("Transcription:")
print(transcription)
