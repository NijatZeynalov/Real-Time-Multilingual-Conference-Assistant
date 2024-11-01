from pathlib import Path
from typing import List, Optional
from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    """Application settings and configuration."""

    # API Settings
    GOOGLE_CLOUD_API_KEY: str = Field(
        ...,
        description="Google Cloud API key"
    )
    GOOGLE_APPLICATION_CREDENTIALS: Path = Field(
        ...,
        description="Path to Google Cloud credentials JSON"
    )

    # Speech Recognition
    DEFAULT_LANGUAGE: str = Field(
        default="en-US",
        description="Default speech recognition language"
    )
    CHUNK_SIZE: int = Field(
        default=1024,
        description="Audio chunk size for processing"
    )
    ENERGY_THRESHOLD: int = Field(
        default=300,
        description="Energy level for speech detection"
    )
    RECORD_TIMEOUT: int = Field(
        default=5,
        description="Recording timeout in seconds"
    )
    PHRASE_TIMEOUT: int = Field(
        default=3,
        description="Phrase timeout in seconds"
    )

    # Translation
    TARGET_LANGUAGES: List[str] = Field(
        default=["es", "fr", "de", "zh", "ja"],
        description="Target languages for translation"
    )
    MAX_TEXT_LENGTH: int = Field(
        default=5000,
        description="Maximum text length for translation"
    )
    TRANSLATION_TIMEOUT: int = Field(
        default=10,
        description="Translation timeout in seconds"
    )

    # Audio
    AUDIO_FORMAT: str = Field(
        default="wav",
        description="Audio file format"
    )
    SAMPLE_RATE: int = Field(
        default=16000,
        description="Audio sample rate"
    )
    CHANNELS: int = Field(
        default=1,
        description="Number of audio channels"
    )
    AUDIO_CHUNK_SIZE: int = Field(
        default=1024,
        description="Audio processing chunk size"
    )

    # Storage
    CACHE_DIR: Path = Field(
        default=Path("cache"),
        description="Cache directory path"
    )
    MAX_CACHE_SIZE_MB: int = Field(
        default=500,
        description="Maximum cache size in MB"
    )
    CACHE_EXPIRY_HOURS: int = Field(
        default=24,
        description="Cache expiry time in hours"
    )

    # Logging
    LOG_LEVEL: str = Field(
        default="INFO",
        description="Logging level"
    )
    LOG_FILE: Path = Field(
        default=Path("logs/conference_assistant.log"),
        description="Log file path"
    )
    MAX_LOG_SIZE_MB: int = Field(
        default=100,
        description="Maximum log file size in MB"
    )
    BACKUP_COUNT: int = Field(
        default=5,
        description="Number of log backup files"
    )

    # Session
    SESSION_SAVE_INTERVAL: int = Field(
        default=300,
        description="Session save interval in seconds"
    )
    DEFAULT_SESSION_FILE: Path = Field(
        default=Path("session.json"),
        description="Default session file path"
    )

    class Config:
        env_file = ".env"
        case_sensitive = True

    def setup_directories(self):
        """Create necessary directories."""
        self.CACHE_DIR.mkdir(parents=True, exist_ok=True)
        self.LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

# Initialize settings
settings = Settings()
settings.setup_directories()