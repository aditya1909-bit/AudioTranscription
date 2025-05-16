# AudioTranscription

AudioTranscription is a simple command-line tool that records audio from your system microphone and transcribes it into text using the whisper.cpp C++ implementation of OpenAI’s Whisper model. This repository contains everything needed to capture, process, and output a text transcript of a short audio clip.

## 📄 Features

- Records a fixed-duration audio clip (default: 30 seconds) from your microphone.
- Saves the audio as a WAV file in the `recordings/` directory.
- Transcribes audio using the efficient whisper.cpp binary.
- Outputs the transcript as a text file in the `transcripts/` directory.

## 🛠️ Technologies Used

- Python 3.11+
- sounddevice (audio capture)
- soundfile (audio file I/O)
- whisper.cpp (C++ Whisper implementation)
- numpy (audio data handling)

## 📦 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/AudioTranscription.git
   cd AudioTranscription
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # On Windows use `.venv\Scripts\activate`
   ```

3. **Install Python dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install whisper.cpp (system dependency):**

   ```bash
   brew install whisper-cpp   # macOS (Homebrew)
   # or appropriate package manager on your system
   ```

## ⬇️ Download the Whisper Model

Before running the transcription, you need to download the pre-trained Whisper model binary:

1. Create a `models/` directory in the project root (if it doesn’t exist):
   ```bash
   mkdir -p models
   ```
2. Download the “base” model and save it as `models/ggml-base.bin`:
   ```bash
   # Example using curl:
   curl -L https://huggingface.co/ggerganov/whisper.cpp/resolve/main/models/ggml-base.bin \
     -o models/ggml-base.bin
   ```
   Or download manually from:
   https://huggingface.co/ggerganov/whisper.cpp/resolve/main/models/ggml-base.bin

## 📂 File Structure

```
AudioTranscription/
├── transcribe.py           # Main script for recording and transcription
├── recordings/
│   └── sample.wav          # Recorded audio clip
├── transcripts/
│   └── sample.txt          # Transcribed text output
├── models/
│   └── ggml-base.bin       # Whisper model binary
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## ▶️ Usage

1. **Record and transcribe:**

   ```bash
   python transcribe.py
   ```

2. The script will:
   - Record a 30-second audio clip and save it as `recordings/sample.wav`.
   - Invoke `whisper.cpp` to transcribe the clip.
   - Save the transcript to `transcripts/sample.txt`.

3. **Adjust parameters:**
   - To change recording duration, edit the `DURATION` constant in `transcribe.py`.
   - To use a different model, place the `.bin` file in `models/` and update the path in the script.

## 🧪 Sample Output

```
Patient is reporting normal vital signs. The procedure will proceed without complications...
```

## 📝 Notes

- Ensure your microphone permissions are enabled for Python.
- If you encounter issues finding the `whisper` binary, verify its installation and update the path in `transcribe.py`.
- For large audio files or production use, consider using GPU-supported versions of Whisper.

## 👤 Author

Aditya Dutta
