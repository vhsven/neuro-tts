from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()
with open("neuro-fysio1-audio-30-32.mp3", "rb") as audio_file:
    transcription = client.audio.transcriptions.create(
        model="gpt-4o-transcribe",
        file=audio_file
    )

    print(transcription.text)