import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)
alexa.say('How can i help you')
alexa.runAndWait()

try:
    with sr.Microphone() as source:
        print('Listening....')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command:
            print(command)

except:
    pass