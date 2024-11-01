from typing import Dict, List, Optional
from datetime import datetime
import json
from .logger import setup_logger

logger = setup_logger(__name__)


class SessionManager:
    def __init__(self, session_id: Optional[str] = None):
        self.session_id = session_id or datetime.now().strftime("%Y%m%d_%H%M%S")
        self.translations: Dict[str, List[dict]] = {}

    def add_translation(self, original_text: str, translations: dict, speaker: str):
        entry = {
            'timestamp': datetime.now().isoformat(),
            'speaker': speaker,
            'original': original_text,
            'translations': translations
        }
        self.translations.setdefault(self.session_id, []).append(entry)

    def save_session(self, file_path: str):
        try:
            with open(file_path, 'w') as f:
                json.dump(self.translations, f, indent=2)
            logger.info(f"Session saved to {file_path}")
        except Exception as e:
            logger.error(f"Failed to save session: {e}")

    def load_session(self, file_path: str):
        try:
            with open(file_path, 'r') as f:
                self.translations = json.load(f)
            logger.info(f"Session loaded from {file_path}")
        except Exception as e:
            logger.error(f"Failed to load session: {e}")