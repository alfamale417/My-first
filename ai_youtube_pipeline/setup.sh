#!/bin/bash
set -e

cd "$(dirname "$0")/.."

python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
pip install -r ai_youtube_pipeline/requirements.txt

if ! [ -f ai_youtube_pipeline/.env ]; then
  cp ai_youtube_pipeline/.env.example ai_youtube_pipeline/.env
fi

if ! [ -f ai_youtube_pipeline/credentials.json ]; then
  echo "" 
echo "IMPORTANT: Place your Google OAuth client JSON file here:" 
echo "  ai_youtube_pipeline/credentials.json" 
echo "" 
echo "After that, run:" 
echo "  source .venv/bin/activate" 
echo "  python ai_youtube_pipeline/run_pipeline.py --topic \"AI tools for creators\" --title \"5 AI tools every creator should use\" --description \"AI tools for creators in 2026\"" 
else
  echo "Setup complete. You can now run the pipeline."
fi
