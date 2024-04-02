import streamlit as st
import pyttsx3
import speech_recognition as sr

def text_to_speech(text, rate):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Speak now...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            st.error("Sorry, I couldn't understand the audio.")
            return None
        except sr.RequestError as e:
            st.error(f"Could not request results from speech recognition service; {e}")
            return None

def main():
    st.title("Text to Speech and Speech to Text App")
    
    st.sidebar.header("Select Mode")
    mode = st.sidebar.radio("Choose Mode", ("Text to Speech", "Speech to Text"))

    if mode == "Text to Speech":
        st.write("Enter the text you want to convert to speech:")
        text_input = st.text_area("Input Text")

        rate = st.slider("Select Speech Rate", min_value=100, max_value=300, step=10, value=200)

        if st.button("Convert to Speech"):
            if text_input:
                text_to_speech(text_input, rate)
                st.success("Speech generated successfully!")
            else:
                st.warning("Please enter some text to convert.")
    elif mode == "Speech to Text":
        st.write("Click the button below and start speaking:")
        if st.button("Start Recording"):
            text = speech_to_text()
            if text:
                st.success("Speech converted to text:")
                st.write(text)

if __name__ == "__main__":
    main()
