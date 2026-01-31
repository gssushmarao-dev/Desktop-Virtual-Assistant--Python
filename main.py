import pyttsx3
import speech_recognition as sr
import datetime

# Initialize the speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()



def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("How can I help you today?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print("You said: " + command)
    except sr.UnknownValueError:
        print("Sorry, I didn't get that. Can you repeat?")
        return "None"
    return command

if __name__ == "__main__":
    wish_me()
    while True:
        command = take_command().lower()
        if 'exit' in command:
            speak("Goodbye!")
            break


