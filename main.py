from time import ctime
from random import randint,random
from gtts import gTTS
import speech_recognition as sr
import webbrowser as wb
import playsound as player
import os


r= sr.Recognizer()
bot_name = 'Sara'

def record_audio(ask = None):
    with sr.Microphone() as src :
        if ask is not None:
            speak(ask)
        audio_input = r.listen(src)
        text_data = ''
        try:
            text_data = r.recognize_google(audio_input)
        except sr.UnknownValueError as e1:
            print(e1.with_traceback())
            speak('Oups, i didn\'t hear you corectly :( ...')
        except sr.RequestError as e2:
            print(e2.with_traceback())
            speak('Sorry, the service is currently down')
        return text_data

def respond(data):
    if 'What is your name'.lower() in data.lower():
        speak('My name is {}'.format(bot_name))
    elif 'What time is it'.lower() in data.lower():
        speak(ctime())
    #searching for something in google
    elif 'Search'.lower() in data.lower():
        q = record_audio('What do you want to search for')
        google_search_url = 'https://www.google.com/search?q={}'.format(q)
        wb.get().open(google_search_url)
        speak('Here is what i found about {}'.format(q))
    elif 'Find location'.lower() in data.lower():
        l = record_audio('What is the place you want to locate')
        google_search_url = 'https://www.google.com/maps/place/{}/&amp'.format(l)
        wb.get().open(google_search_url)
        speak('Here is the location of {}'.format(l))
    elif 'exit'.lower() or 'bye'.lower() or 'goodbye'.lower() in data.lower():
        #say goodbye randomly each time
        farwell_expressions = ['See you later', 'Ok, goodbye', 'ByeBye']
        n = randint(0,len(farwell_expressions)-1)
        speak(farwell_expressions[n])
        exit()
    else:
        speak('You said: {}'.format(text_data))

def speak(sentence):
    text_to_speech = gTTS(text=sentence, lang='en')
    r = randint(1,100000000)
    audio_file = 'aud-{}.mp3'.format(r)
    text_to_speech.save(audio_file)
    player.playsound(audio_file)
    print(sentence)
    os.remove(audio_file)

speak('Listening...')

while True:

    text_data = record_audio()
    respond(text_data)
