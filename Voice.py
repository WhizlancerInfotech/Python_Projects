import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source)
    text = recognizer.recognize_google(audio)
    print("You said:", text)
    engine.say("You said " + text)
    engine.runAndWait()
