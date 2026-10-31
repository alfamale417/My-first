import os
import re
from typing import Optional

import openai

from config import SETTINGS


def generate_script(topic: str, title: Optional[str] = None) -> str:
    if SETTINGS.openai_api_key:
        openai.api_key = SETTINGS.openai_api_key
        prompt = (
            f"Write an engaging YouTube video script about: {topic}. "
            "Use an energetic, clear, and professional style. "
            "Include a hook, three strong points, and a closing CTA. "
            "Keep it under 500 words."
        )
        response = openai.chat.completions.create(
            model='gpt-4o-mini',
            messages=[{'role': 'user', 'content': prompt}],
            temperature=0.8,
            max_tokens=600,
        )
        text = response.choices[0].message.content.strip()
        return re.sub(r'\n+', ' ', text)

    return (
        f"Hook: If you want to grow faster with {topic}, this is the system you need. "
        f"First, choose a clear niche and make your message simple. "
        f"Second, use AI tools to speed up research, scripting, editing, and posting. "
        f"Third, publish consistently and test what brings the most attention. "
        f"The real growth comes from combining value, speed, and consistency. "
        f"If you want more ideas like this, follow this channel and keep creating."
    )


if __name__ == '__main__':
    topic = SETTINGS.topic
    script = generate_script(topic, SETTINGS.video_title)
    print(script)
