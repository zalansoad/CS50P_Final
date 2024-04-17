import pyttsx3
import speech_recognition as sr

r = sr.Recognizer()
engine = pyttsx3.init()
wake_word = "hey Bob"
while True:
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(text)
        if wake_word.casefold() in text.casefold():
            print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
            engine.say("You said " + r.recognize_google(audio))
            engine.runAndWait()
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

