from typing import List
from .speech_recognizer import SpeechRecognizer
from .translator import Translator
from .text_to_speech import TextToSpeech
from .audio_manager import AudioManager
from .session_manager import SessionManager
from .config_manager import ConfigManager
from .logger import setup_logger

logger = setup_logger(__name__)


class ConferenceAssistant:
    def __init__(self, target_languages: List[str]):
        self.config = ConfigManager()
        self.recognizer = SpeechRecognizer(
            language=self.config.get('DEFAULT_LANGUAGE')
        )
        self.translator = Translator()
        self.tts = TextToSpeech(self.config.get('CACHE_DIR'))
        self.audio_manager = AudioManager()
        self.session_manager = SessionManager()
        self.target_languages = target_languages

    def start(self):
        try:
            logger.info("Starting Conference Assistant")
            self.recognizer.start_recognition(self._handle_speech)
        except Exception as e:
            logger.error(f"Failed to start Conference Assistant: {e}")

    def stop(self):
        try:
            logger.info("Stopping Conference Assistant")
            self.recognizer.stop_recognition()
            self.session_manager.save_session('session.json')
        except Exception as e:
            logger.error(f"Failed to stop Conference Assistant: {e}")

    def _handle_speech(self, text: str, source_lang: str):
        try:
            # Translate
            translations = self.translator.translate(
                text, source_lang, self.target_languages
            )

            # Save to session
            self.session_manager.add_translation(text, translations, "Speaker")

            # Generate speech for translations
            for lang, translated_text in translations.items():
                audio_file = self.tts.synthesize(translated_text, lang)
                if audio_file:
                    self.audio_manager.play_audio(audio_file)

        except Exception as e:
            logger.error(f"Failed to handle speech: {e}")


if __name__ == "__main__":
    assistant = ConferenceAssistant(['es', 'fr', 'de'])
    assistant.start()