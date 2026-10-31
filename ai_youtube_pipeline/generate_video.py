import os
import tempfile
from pathlib import Path

from typing import List

from gtts import gTTS
from moviepy.editor import AudioFileClip, ColorClip, CompositeVideoClip, TextClip, concatenate_videoclips

from config import SETTINGS


def split_script_into_chunks(script: str, max_chars: int = 120) -> List[str]:
    words = script.split()
    chunks: List[str] = []
    current = []
    current_len = 0

    for word in words:
        if current_len + len(word) + 1 > max_chars and current:
            chunks.append(' '.join(current))
            current = [word]
            current_len = len(word)
        else:
            current.append(word)
            current_len += len(word) + 1

    if current:
        chunks.append(' '.join(current))

    return chunks


def build_voiceover(script: str, output_mp3: str) -> str:
    tts = gTTS(text=script, lang=SETTINGS.video_language or 'en', slow=False)
    tts.save(output_mp3)
    return output_mp3


def render_video(script: str, output_mp4: str) -> str:
    os.makedirs(SETTINGS.video_output_dir, exist_ok=True)
    temp_dir = tempfile.mkdtemp(prefix='video_')
    voice_path = os.path.join(temp_dir, 'voice.mp3')
    voice_path = build_voiceover(script, voice_path)

    duration = max(3.0, min(35.0, len(script.split()) * 0.38))

    bg = ColorClip((1280, 720), color=(22, 13, 35), duration=duration)
    title = TextClip(
        SETTINGS.video_title,
        fontsize=46,
        color='white',
        font='DejaVu-Sans-Bold',
        method='label',
    ).set_position(('center', 120)).set_duration(duration)

    script_chunks = split_script_into_chunks(script)
    text_clips = []
    y = 260
    for idx, chunk in enumerate(script_chunks[:4]):
        tc = TextClip(
            chunk,
            fontsize=26,
            color='white',
            font='DejaVu-Sans',
            method='label',
            bg_color=None,
            size=(1000, None),
            align='center',
        ).set_position(('center', y)).set_duration(duration)
        text_clips.append(tc)
        y += 120

    final = CompositeVideoClip([bg, title, *text_clips], size=(1280, 720))

    audio = AudioFileClip(voice_path)
    final = final.set_audio(audio)
    final.write_videofile(output_mp4, fps=24, codec='libx264', audio_codec='aac', verbose=False, logger=None)

    return output_mp4


if __name__ == '__main__':
    script = (
        "AI is helping creators produce more content faster. "
        "This video shows how to use smart tools to speed up scripting, editing, and publishing."
    )
    output = os.path.join(SETTINGS.video_output_dir, 'sample_video.mp4')
    render_video(script, output)
    print(f'Video created: {output}')
