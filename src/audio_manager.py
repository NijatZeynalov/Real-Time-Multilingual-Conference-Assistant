import pyaudio
import wave
from typing import Optional
import threading
from .logger import setup_logger

logger = setup_logger(__name__)


class AudioManager:
    def __init__(self):
        self.pyaudio = pyaudio.PyAudio()
        self.stream = None
        self.is_playing = False

    def play_audio(self, file_path: str):
        try:
            threading.Thread(target=self._play_file, args=(file_path,), daemon=True).start()
        except Exception as e:
            logger.error(f"Audio playback error: {e}")

    def _play_file(self, file_path: str):
        try:
            with wave.open(file_path, 'rb') as wave_file:
                self.stream = self.pyaudio.open(
                    format=self.pyaudio.get_format_from_width(wave_file.getsampwidth()),
                    channels=wave_file.getnchannels(),
                    rate=wave_file.getframerate(),
                    output=True
                )

                data = wave_file.readframes(1024)
                while data and self.is_playing:
                    self.stream.write(data)
                    data = wave_file.readframes(1024)

        except Exception as e:
            logger.error(f"Audio file playback error: {e}")
        finally:
            if self.stream:
                self.stream.stop_stream()
                self.stream.close()