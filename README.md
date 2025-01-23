# Real-Time Multilingual Conference Assistant

A real-time speech-to-text and translation tool that provides live multilingual transcription and translation during international conferences. The system supports multiple languages, real-time audio processing, and session management.

## Features

### Speech Processing
- Real-time speech recognition using Google Cloud Speech-to-Text
- Automatic language detection
- Noise reduction and audio enhancement
- Continuous speech monitoring

### Translation
- Real-time translation using Google Cloud Translate
- Support for multiple target languages
- Batch translation optimization
- Language auto-detection

### Audio Output
- Text-to-Speech synthesis using Google TTS
- Multi-channel audio output
- Audio caching for improved performance
- Dynamic audio stream management

### Session Management
- Real-time session tracking
- Translation history
- JSON-based session storage
- Automatic session backup

## Installation

1. Clone the repository:


2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your Google Cloud API credentials
```

## Prerequisites

- Python 3.8+
- Google Cloud Account with enabled APIs:
  - Speech-to-Text
  - Cloud Translate
  - Text-to-Speech
- PyAudio dependencies:
  - Linux: `sudo apt-get install python3-pyaudio`
  - Windows: Install through pip
  - macOS: `brew install portaudio`

## Configuration

Edit `.env` file with your settings:
```env
GOOGLE_CLOUD_API_KEY=your_api_key
DEFAULT_LANGUAGE=en-US
TARGET_LANGUAGES=es,fr,de
```

Key configuration options:
- Speech recognition parameters
- Target languages
- Audio settings
- Cache configuration
- Logging preferences

## 💻 Usage

### Basic Usage
```python
from conference_assistant.src.main import ConferenceAssistant

# Initialize assistant
assistant = ConferenceAssistant(['es', 'fr', 'de'])

# Start real-time processing
assistant.start()

# Stop processing
assistant.stop()
```

### Custom Configuration
```python
from conference_assistant.src.config_manager import ConfigManager

config = ConfigManager()
assistant = ConferenceAssistant(
    target_languages=['es', 'fr'],
    config=config
)
```

### Session Management
```python
# Load previous session
assistant.session_manager.load_session('previous_session.json')

# Save current session
assistant.session_manager.save_session('current_session.json')
```

## 📊 Project Structure
```
conference_assistant/
├── src/
│   ├── speech_recognizer.py   # Speech recognition
│   ├── translator.py          # Translation service
│   ├── text_to_speech.py      # TTS functionality
│   ├── audio_manager.py       # Audio processing
│   ├── session_manager.py     # Session handling
│   ├── config_manager.py      # Configuration
│   ├── utils.py              # Utilities
│   ├── logger.py             # Logging
│   └── main.py               # Main application
├── tests/                    # Test files
├── data/                     # Data storage
└── logs/                     # Log files
```

## API Reference

### SpeechRecognizer
```python
recognizer = SpeechRecognizer(language='en-US')
recognizer.start_recognition(callback_function)
recognizer.stop_recognition()
```

### Translator
```python
translator = Translator()
translations = translator.translate(
    text="Hello",
    src="en",
    target_languages=["es", "fr"]
)
```

### TextToSpeech
```python
tts = TextToSpeech()
audio_file = tts.synthesize(
    text="Hello",
    lang="en"
)
```

## Error Handling

The system includes comprehensive error handling:
- Audio device errors
- API timeouts
- Network issues
- Invalid language codes
- Session management errors

## Logging

Logs are stored in the `logs` directory:
- Error tracking
- Session history
- Performance metrics
- API usage statistics

