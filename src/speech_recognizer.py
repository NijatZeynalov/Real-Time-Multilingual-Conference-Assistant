import speech_recognition as sr
from typing import Optional, Callable
import threading
from .logger import setup_logger

logger = setup_logger(__name__)


class SpeechRecognizer:
    def __init__(self, language: str = 'en-US', chunk_size: int = 1024):
        self.recognizer = sr.Recognizer()
        self.language = language
        self.chunk_size = chunk_size
        self.is_active = False
        self.mic = None

    def start_recognition(self, callback: Callable):
        try:
            self.mic = sr.Microphone(chunk_size=self.chunk_size)
            self.is_active = True

            with self.mic as source:
                self.recognizer.adjust_for_ambient_noise(source)

            threading.Thread(target=self._recognition_loop, args=(callback,), daemon=True).start()
            logger.info("Speech recognition started")

        except Exception as e:
            logger.error(f"Failed to start speech recognition: {e}")

    def _recognition_loop(self, callback: Callable):
        while self.is_active:
            try:
                with self.mic as source:
                    audio = self.recognizer.listen(source)
                text = self.recognizer.recognize_google(audio, language=self.language)
                callback(text, self.language)
            except Exception as e:
                logger.error(f"Recognition error: {e}")

    def stop_recognition(self):
        self.is_active = False
        logger.info("Speech recognition stopped")
