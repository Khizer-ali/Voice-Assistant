import json
import webbrowser
import pyttsx3
import datetime
import speech_recognition
import wikipedia
import requests
import os

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

author = "Sir"
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(f"Good morning {author}")
    elif hour >= 12 and hour < 18:
        speak(f"Good afternoon {author}")
    else:
        speak(f"Good evening {author}")

    speak(f"Hello I am Jarvis, how can I help you?")

def takecommand():
    '''
    Take microphone input from the user and return string
    '''
    r = speech_recognition.Recognizer()

    with speech_recognition.Microphone(device_index=0) as source:
        print("Listening.....")
        r.pause_threshold = 1.5
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=10, phrase_time_limit=10)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query} \n")
        speak(query)
    except Exception as e:
        print("Sorry, say that again....")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()

    # Set Chrome as the default browser
    # Replace with the path to your Chrome executable
    chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

    if 1:
        query = takecommand().lower()

        if 'wikipedia' in query and 'who' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open google' in query:
            webbrowser.get('chrome').open("https://www.google.com/")

        elif 'browser' in query:
            speak("What should I search?")
            um = takecommand().lower()
            webbrowser.get('chrome').open(f"https://www.google.com/search?q={um}")

        elif 'open youtube' in query:
            webbrowser.get('chrome').open("https://www.youtube.com/")
