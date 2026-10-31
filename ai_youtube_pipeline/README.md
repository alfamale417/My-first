# AI YouTube Channel Automation Starter

This project turns a topic into a faceless AI-generated YouTube video and uploads it to your channel using the YouTube Data API.

## What it does
- generates a script for a video topic
- creates a voiceover using AI TTS
- renders an MP4 with subtitles/background
- uploads the result to YouTube

## Prerequisites
- Python 3.10+
- A Google Cloud project with YouTube Data API enabled
- OAuth client credentials JSON file from Google Cloud
- Optional: OpenAI API key for better script generation

## Folder structure
- `ai_youtube_pipeline/`
  - `README.md`
  - `requirements.txt`
  - `.env.example`
  - `config.py`
  - `generate_video.py`
  - `upload_youtube.py`
  - `run_pipeline.py`

## Quick start

1. Open a terminal in the repo root.
2. Install dependencies:

   ```bash
   pip install -r ai_youtube_pipeline/requirements.txt
   ```

3. Copy the example environment file:

   ```bash
   cp ai_youtube_pipeline/.env.example ai_youtube_pipeline/.env
   ```

4. Edit `ai_youtube_pipeline/.env` and fill in your values.
5. Create your Google OAuth credentials JSON in Google Cloud and point to it.
6. Run:

   ```bash
   python ai_youtube_pipeline/run_pipeline.py --topic "AI tools for creators" --title "5 AI tools every creator should use" --description "AI tools for creators in 2026"
   ```

7. The script will generate a video, render it to MP4, and upload it to your YouTube channel.

## Important note
This is a technical starter system. It does not guarantee YouTube monetization. Monetization still depends on your channel meeting YouTube eligibility rules.

## Example env file
Look at `.env.example` for the required keys.
