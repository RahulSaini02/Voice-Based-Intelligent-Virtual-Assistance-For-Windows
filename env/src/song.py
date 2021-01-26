from lyrics_extractor import SongLyrics
from dotenv import load_dotenv
import os

load_dotenv()

def getLyrics(audio):
    api_key = os.getenv("GCS_API_KEY")
    engine_id = os.getenv("GCS_ENGINE_ID")
    extract_lyrics = SongLyrics(api_key,engine_id)
    data = extract_lyrics.get_lyrics(audio)
    print(data.get('lyrics'))




