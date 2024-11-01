from googletrans import Translator as GoogleTranslator
from typing import List
from .logger import setup_logger

logger = setup_logger(__name__)

class Translator:
    def __init__(self):
        self.translator = GoogleTranslator()
        self.supported_languages = {'en', 'es', 'fr', 'de', 'zh', 'ja', 'ko', 'ru'}

    def translate(self, text: str, src: str, target_languages: List[str]) -> dict:
        try:
            translations = {}
            for lang in target_languages:
                if lang in self.supported_languages:
                    result = self.translator.translate(text, src=src, dest=lang)
                    translations[lang] = result.text
            return translations
        except Exception as e:
            logger.error(f"Translation error: {e}")
            return {}