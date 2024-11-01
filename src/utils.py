import os
from typing import Optional
from .logger import setup_logger

logger = setup_logger(__name__)

def ensure_dir(directory: str) -> bool:
    """Create directory if it doesn't exist."""
    try:
        os.makedirs(directory, exist_ok=True)
        return True
    except Exception as e:
        logger.error(f"Failed to create directory {directory}: {e}")
        return False

def clean_audio_files(directory: str, max_age_hours: float = 24) -> None:
    """Clean up old audio files."""
    try:
        for file in os.listdir(directory):
            if file.endswith('.mp3') or file.endswith('.wav'):
                file_path = os.path.join(directory, file)
                if is_file_old(file_path, max_age_hours):
                    os.remove(file_path)
    except Exception as e:
        logger.error(f"Failed to clean audio files: {e}")

def is_file_old(file_path: str, max_age_hours: float) -> bool:
    """Check if file is older than max_age_hours."""
    try:
        age = (time.time() - os.path.getmtime(file_path)) / 3600
        return age > max_age_hours
    except Exception:
        return False