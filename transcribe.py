import sounddevice as sd
import soundfile as sf
import whisper

DURATION = 30  # seconds
SAMPLE_RATE = 44100
OUTPUT_PATH = "recordings/sample.wav"

def record_audio():
    print("Recording for 30 seconds...")
    recording = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1)
    sd.wait()
    sf.write(OUTPUT_PATH, recording, SAMPLE_RATE)
    print(f"Audio saved to {OUTPUT_PATH}")

def transcribe_audio():
    import subprocess
    import os

    print("Transcribing using whisper.cpp...")
    model_path = "models/ggml-base.bin"
    input_path = OUTPUT_PATH

    try:
        whisper_cpp_path = "/opt/homebrew/bin/whisper-cpp"
        output_dir = "transcripts"
        os.makedirs(output_dir, exist_ok=True)
        output_base = os.path.join(output_dir, "sample")  # base name without extension

        subprocess.run([
            whisper_cpp_path,
            input_path,
            "-l", "en",
            "-m", model_path,
            "-otxt",
            "-of", output_base
        ], check=True)
        print(f"Transcription complete. Check '{output_base}.txt' for the output.")
    except subprocess.CalledProcessError as e:
        print("Whisper.cpp transcription failed:", e)

if __name__ == "__main__":
    record_audio()
    transcribe_audio()