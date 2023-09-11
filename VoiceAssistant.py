import speech_recognition as sr

def listen_to_audio():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for audio...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_sphinx(audio)  # Use the Sphinx recognizer for offline use
        return text
    except sr.UnknownValueError:
        return "Sorry, I could not understand the audio."
    except sr.RequestError:
        return "Sorry, I encountered an error while trying to process the audio."

def main():
    text = listen_to_audio()

    print(f"Recognized Text: {text}")

if __name__ == "__main__":
    main()
