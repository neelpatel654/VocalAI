# pip install pyttsx3 gradio

import pyttsx3
import gradio as gr

# Initialize the TTS engine
engine = pyttsx3.init()

# Function to convert text to speech


def text_to_speech(text):
    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech (optional)
    engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0) (optional)

    # Save speech to an audio file
    audio_file = "output_speech1.mp3"
    engine.save_to_file(text, audio_file)
    engine.runAndWait()

    return audio_file


# Create and launch the Gradio interface
gr.Interface(
    title='Text-to-Speech Conversion',
    fn=text_to_speech,
    inputs=gr.Textbox(label="Enter text"),
    outputs=gr.Audio(label="Generated Speech"),
    live=True
).launch()
