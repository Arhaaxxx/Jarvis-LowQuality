import os
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
c = 1

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            talk('Speak sir')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            if 'jack' in command:
                command = command.replace('jack', '')
                print(command)
            else:
                command = '...'
    except:
        pass
    return command

def take_number():
    try:
        with sr.Microphone() as source:
            talk('Number Please')
            voice = listener.listen(source)
            number = listener.recognize_google(voice)
            number = number.lower()
            print(number)
    except:
        pass
    return number

def take_message():
    try:
        with sr.Microphone() as source:
            talk('Message Please')
            voice = listener.listen(source)
            message = listener.recognize_google(voice)
            message = message.lower()
            print(message)
    except:
        pass
    return message

def run_jarvis():
    command = take_command()
    print(command)
    if command:

        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%H:%M')
            print(time)
            talk('The current time is ' + time)
        elif 'search for' in command:
            thing = command.replace('search for', '')
            info = wikipedia.summary(thing, 3)
            print(info)
            talk(info)
        elif 'google' in command:
            whatever = command.replace('google', '')
            info = pywhatkit.misc.search(whatever)
            print(info)
            talk(info)
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        elif 'initiate lockdown' in command:
            talk('Locking down building \n Loading turrets \n Preparing suit \n Lowering bullet resistant sheets \n playing Theme')
            pywhatkit.playonyt('Avengers theme')
            engine.runAndWait()
            talk('Suit ready')
        elif 'virtual mouse' in command:
            talk('Virtual mouse activated')
            os.system('mouse.py')
            talk('Virtual mouse deactivated')
        elif 'h u' in command:
            talk('HUD online')
            os.system('HUD.py')
            talk('HUD offline')
        elif 'close' in command:
            talk('Systems offline')
            c += 1
        elif 'message' in command:
            number = take_number()
            if 'mom' in number:
                message = take_message()
                pywhatkit.sendwhatmsg_instantly('+X XXXXXXXXXX', message, wait_time=15)
            elif 'dad' in number:
                message = take_message()
                pywhatkit.sendwhatmsg_instantly('+X XXXXXXXXXX', message, wait_time=15)
            elif 'me' in number:
                message = take_message()
                pywhatkit.sendwhatmsg_instantly('+X XXXXXXXXXX', message, wait_time=15)
        else:
            talk('I didnt get what you mean')
    else:
        pass
while c == 1:
    run_jarvis()