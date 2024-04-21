from pathlib import Path
from openai import OpenAI
from config import API_KEY

client = OpenAI(api_key=API_KEY)

speech_file_path = Path(__file__).parent / "Hello_Voice.mp3"

response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="Today is a wonderful day to build something people love!"
)

response.stream_to_file(speech_file_path)








