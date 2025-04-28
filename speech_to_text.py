# Install dependencies (uncomment if running this script manually for the first time)
# !pip install git+https://github.com/openai/whisper.git -q
# !pip install gradio -q

import whisper
import gradio as gr

# Load the Whisper model
model = whisper.load_model("base")


def transcribe(audio):
    # Load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(audio)
    audio = whisper.pad_or_trim(audio)

    # Make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # Detect the spoken language
    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")

    # Decode the audio
    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)

    return result.text


# Create and launch the Gradio interface
gr.Interface(
    title='OpenAI Whisper ASR Gradio Web UI',
    fn=transcribe,
    inputs=gr.Audio(type="filepath", label="Record your voice"),
    outputs=gr.Textbox(label="Transcription"),
    live=True
).launch()
