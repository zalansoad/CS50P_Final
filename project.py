import pyttsx3
import speech_recognition as sr
import wikipedia
import string
import re

#setx OPENAI_API_KEY "sk-proj-PtvckSpuvie2xWq4tHVST3BlbkFJuxLGCkPg1QiOl2CrIBba"
def main():
    r = sr.Recognizer()
    engine = pyttsx3.init()  
    wake_word = "hey Bob"
    stop_word = "stop the program"
    
    recognise(r, engine, wake_word, stop_word)
    
def recognise(r, engine, wake, stop):
    with sr.Microphone() as source:
        while True:
            print("Say something!")
            audio = r.listen(source)    
            try:
                text = r.recognize_google(audio)
                if wake.casefold() in text.casefold():
                    print("Searching Wikipedia...")
                    text_to_speech(engine, wiki(extract_word(text)))
                elif stop.casefold() in text.casefold():
                    break
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

def extract_word(text):

    cleaned_text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    match = re.search(r"(hey bob what's a|hey bob what's an|hey bob what are|hey bob who is|hey bob who was|hey bob tell me about|hey bob what do you know about|hey bob what is a|hey bob what is an)\s*(.*)", cleaned_text)
    if match:
        return match.group(2).strip()
    else:
        return None

def text_to_speech(engine, s):
    
    print(s)
    engine.say(s)
    engine.runAndWait()

def wiki(text):
    title = (wikipedia.search(text, results=1))[0]
    return (wikipedia.summary(title, sentences=2, auto_suggest=False, redirect=True))

if __name__ == "__main__":
    main()