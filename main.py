import speech_recognition as sr

r= sr.Recognizer()

with sr.Microphone() as src :
    print('I\'m listening to you...')
    audio_input = r.listen(src)
    text_data = r.recognize_google(audio_input)
    print('You said: {}'.format(text_data))