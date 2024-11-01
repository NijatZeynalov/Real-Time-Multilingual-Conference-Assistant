from typing import Dict, Any
import os
from dotenv import load_dotenv
from .logger import setup_logger

logger = setup_logger(__name__)


class ConfigManager:
    def __init__(self):
        load_dotenv()
        self.config = {
            'GOOGLE_CLOUD_API_KEY': os.getenv('GOOGLE_CLOUD_API_KEY'),
            'DEFAULT_LANGUAGE': os.getenv('DEFAULT_LANGUAGE', 'en-US'),
            'TARGET_LANGUAGES': os.getenv('TARGET_LANGUAGES', 'es,fr,de').split(','),
            'CHUNK_SIZE': int(os.getenv('CHUNK_SIZE', '1024')),
            'CACHE_DIR': os.getenv('CACHE_DIR', 'cache')
        }

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)
