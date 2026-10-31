import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))


@dataclass
class Settings:
    openai_api_key: str = os.getenv('OPENAI_API_KEY', '')
    youtube_client_secrets_file: str = os.getenv('YOUTUBE_CLIENT_SECRETS_FILE', 'credentials.json')
    youtube_credentials_file: str = os.getenv('YOUTUBE_CREDENTIALS_FILE', 'credentials_token.json')
    video_output_dir: str = os.getenv('VIDEO_OUTPUT_DIR', 'videos')
    video_title: str = os.getenv('VIDEO_TITLE', 'AI Creator Video')
    video_description: str = os.getenv('VIDEO_DESCRIPTION', 'AI automation and creator growth video')
    topic: str = os.getenv('TOPIC', 'AI automation tips')
    video_language: str = os.getenv('VIDEO_LANGUAGE', 'en')
    upload_privacy: str = os.getenv('UPLOAD_PRIVACY', 'private')


SETTINGS = Settings()
