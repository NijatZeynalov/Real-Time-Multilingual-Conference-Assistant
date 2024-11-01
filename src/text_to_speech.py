from gtts import gTTS
import tempfile
import os
from typing import Optional
from .logger import setup_logger

logger = setup_logger(__name__)

class TextToSpeech:
    def __init__(self, cache_dir: Optional[str] = None):
        self.cache_dir = cache_dir or tempfile.gettempdir()

    def synthesize(self, text: str, lang: str) -> Optional[str]:
        try:
            tts = gTTS(text=text, lang=lang)
            output_file = os.path.join(self.cache_dir, f'speech_{hash(text)}.mp3')
            tts.save(output_file)
            return output_file
        except Exception as e:
            logger.error(f"TTS error: {e}")
            return None