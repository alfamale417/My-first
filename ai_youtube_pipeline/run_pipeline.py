import os
import pickle
from pathlib import Path

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

from config import SETTINGS

SCOPES = ['https://www.googleapis.com/auth/youtube.upload']


def get_authenticated_service():
    creds = None
    token_path = SETTINGS.youtube_credentials_file

    if os.path.exists(token_path):
        with open(token_path, 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                SETTINGS.youtube_client_secrets_file,
                SCOPES,
            )
            creds = flow.run_local_server(port=0)

        with open(token_path, 'wb') as token:
            pickle.dump(creds, token)

    return build('youtube', 'v3', credentials=creds)


def upload_video(video_path: str, title: str, description: str, privacy_status: str = 'private'):
    service = get_authenticated_service()

    body = {
        'snippet': {
            'title': title,
            'description': description,
            'tags': ['AI', 'YouTube', 'creator', 'automation', 'growth'],
            'categoryId': '22',
        },
        'status': {
            'privacyStatus': privacy_status,
            'selfDeclaredMadeForKids': False,
        },
    }

    media = MediaFileUpload(video_path, chunksize=-1, resumable=True)
    request = service.videos().insert(
        part=','.join(body.keys()),
        body=body,
        media_body=media,
    )

    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f'Upload progress: {int(status.progress() * 100)}%')

    print(f"Video uploaded successfully: {response['id']}")
    return response


if __name__ == '__main__':
    sample = os.path.join(SETTINGS.video_output_dir, 'sample_video.mp4')
    if os.path.exists(sample):
        upload_video(sample, SETTINGS.video_title, SETTINGS.video_description, SETTINGS.upload_privacy)
    else:
        print('No video file found. Generate one first.')
