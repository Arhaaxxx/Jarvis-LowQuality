import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from playsound import playsound

listener = sr.Recognizer()
engine = pyttsx3.init()
c = 1

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            talk('Speak sire')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
    except:
        pass
    return command


def run_jarvis():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('The current time is ' + time)
    elif 'search for' in command:
        thing = command.replace('search', '')
        info = wikipedia.summary(thing, 3)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'initiate lockdown' in command:
        talk('Locking down building \n Loading turrets \n Preparing suit \n Lowering bullet resistant sheets \n playing Theme')
        pywhatkit.playonyt('Avengers theme')
        talk('Suit ready')
    elif 'close' in command:
        talk('Systems offline')
        c += 1
    else:
        talk('I didnt get what you mean')

while c == 1:
    run_jarvis()