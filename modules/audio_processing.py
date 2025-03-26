import speech_recognition as sr
import streamlit as st

def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_file) as source:
            audio_data = recognizer.record(source)
        return recognizer.recognize_google(audio_data)
    except sr.UnknownValueError:
        st.error("Could not transcribe audio. Please upload a clearer file.")
        return None
    except sr.RequestError as e:
        st.error(f"Request error: {e}")
        return None
