import streamlit as st
from gtts import gTTS

def text_to_speech(text, language='en'):
    """Converts text to speech and plays the audio."""
    speech = gTTS(text=text, lang=language)
    with st.spinner("Generating audio..."):
        speech.save("output.mp3")
    st.audio("output.mp3", format="audio/mpeg")

def text_to_speech_tab():
    st.title("Text-to-Speech")
    text_input = st.text_input("Enter text to convert to speech:")
    language_select = st.selectbox("Select language:", ("en", "es", "fr", "de", "it", "ja"))  # Example languages
    if st.button("Convert to Speech"):
        text_to_speech(text_input, language=language_select)

if __name__ == "__main__":
    text_to_speech_tab()
