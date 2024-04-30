import pyttsx3
import speech_recognition as sr
import wikipedia
import string
import re

def main():
    r = sr.Recognizer()
    engine = pyttsx3.init()  
    voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0"
    engine.setProperty('voice', voice_id)
    name = "Lucy"
    wake_word = f"hey {name}"
    stop_word = "stop the program"
    welcome = f"Welcome, I am {name} your personal assistant."
    text_to_speech(engine, welcome)
    recognise(r, engine, wake_word, stop_word, name.lower())
    
def recognise(r, engine, wake, stop, name):
    with sr.Microphone() as source:
        while True:
            print("Say something!")
            audio = r.listen(source)    
            try:
                text = r.recognize_google(audio).lower()
                if wake.casefold() in text.casefold():
                    print(text)
                    print("Searching Wikipedia...")
                    text_to_speech(engine, wiki(extract_word(text, name)))
                elif stop.casefold() in text.casefold():
                    text_to_speech(engine, "Shutting down. Bye.")
                    break
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

def extract_word(text, name):

    cleaned_text = text.translate(str.maketrans('', '', string.punctuation))

    match = re.search(rf"(hey {name} whats a|hey {name} whats an|hey {name} what are|hey {name} who is|hey {name} who was|hey {name} tell me about|hey {name} what do you know about|hey {name} what is a|hey {name} what is an)\s+(.*)", cleaned_text)
    if match:

        return match.group(2).strip()
    else:
        return None

def text_to_speech(engine, s):
    
    print(s)
    engine.say(s)
    engine.runAndWait()

def wiki(text):
    try:
        title = (wikipedia.search(text, results=1))[0]
        return (wikipedia.summary(title, sentences=2, auto_suggest=False, redirect=True))
    except (IndexError, wikipedia.exceptions.WikipediaException):
        return "I could not find anything about it"

if __name__ == "__main__":
    main()