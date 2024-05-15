# WBVA - Wikipedia-based Voice Assistant
#### Video Demo:  <https://youtu.be/Lr78sIYDWRs>
#### Description:
With the help of the Wikipedia-based Voice Assistant you can easily make Wikipedia queries using your microphone. Furthermore, you can also search for the weather temperature worldwide without a keystroke. Lastly, you can ask the assistant to flip a coin if you need help in hard decisions.

The assistant is always running in the background and is preprogrammed to wake up to the "Hey {name}" wake word. The name of the assistant is provided as command line argument.

For example, you could use the assistant the following way:
To start the program type in: "python project.py Lucy"
Then using your microphone ask something like "Hey Lucy, what do you know about Harry Potter?"
Lucy will look for an article about Harry Potter on Wikipedia and read out loud the first 2 sentences.
You can also ask Lucy the following: "Hey Lucy, what is the temperature in New York?"
Lucy will tell you the temperature in Celsius.
Additionally, you can also ask the assistant to flip a coin: "Hey Lucy, flip a coin."
Lucy will tell you the result afterwards.
You can stop the voice assistant by saying "Stop the program."

**Please note that the program only runs on Windows, since WSL does not support audio devices. Although there are workarounds to use the program in WSL, for the best experience run it on Windows**

# Table of Contents

1. [Files and their Function](#files-and-their-function)
   1.1. [project.py](#projectpy)
   1.2. [test_project.py](#test_projectpy)
   1.3. [requirements.txt](#requirementstxt)
2. [The main program: project.py](#the-main-program-projectpy)
   2.1. [main()](#main)
   2.2. [recognise(r, engine, wake, stop, name)](#recogniser-engine-wake-stop-name)
   2.3. [extract_word(text, name)](#extract_wordtext-name)
   2.4. [text_to_speech(engine, s)](#text_to_speechengine-s)
   2.5. [wiki(text)](#wikitext)
   2.6. [getweather(city)](#getweathercity)

   2.7. [flip_coin()](#flip_coin)


## Files and their function.

### project.py
This file stores the program, the Wikipedia based virtual assistant.

### test_project.py
The key functions of the project.py file are tested in this file. In this file the following functions are tested: wiki, extract_word, getweather, and flip_coin.

### requirements.txt
In this folder all the necessary libraries are listed which need to be installed before running the program.

## The main program: project.py

### main()
The program takes one command line argument, the name of the assistant. If the length of the command line argument does not equal to 2 (file name, assistant name) the program exits.

In main, the imported libraries’ most important functions are initialized first.
The project uses the speech_recognition library to recognise the input. With a while loop the microphone is set to be always active.
Pyttsx3 library is used to convert text to speech in order to hear the response of the virtual assistant.
The voice of the assistant can be changed by altering the voice_id variable with an appropriate windows voice route. Please also note that the UK voice pack needs to be installed in the Windows Narrator settings in order to use Hazel as the voice, otherwise the program will default to another voice that is accessible in your system.

In main, the wake_word and the stop_word are also initialised. After the program starts, the microphone will capture everything, however, only those queries will be processed that are followed by the "Hey {name}" wake phrase or if the sentence contains "stop the program" that will break the while true loop and stops the program.

Finally, main calls the recognise function with all the necessary parameters in order to start capturing the voices.

### recognise(r, engine, wake, stop, name)
This function creates an instance for the microphone object of the speech recognition library and initiates a while true loop to always capture what is said by the user.
Audio is captured by using the listen() method of the recognizer instance and Google Speech Recognition is used to convert the speech to text.
If the text contains the wake word plus phrases like "what is /what's the temperature in" etc. the extract_word function extracts the city name from the text and sends it to the getweather function which comes from the python_weather library. The response is then sent to the text_to_speech function.
Else if the text contains the wake word plus "flip a coin", the flip_coin function is called, that uses the random module to return either tail or head which is then sent to the text_to_speech function.
Finally, if any other question is asked like "who is", "what is", "what do you know about" etc. the wiki function is called after extracting the matter of the question and a wiki search is made which result is processed by the text_to_speech function afterwards.
Since this section is in a try block, whenever there is an issue capturing what the user says, there are exceptions informing the user what went wrong while capturing sound and using the Google Speech Recognition method.

### extract_word(text, name)
This function takes two parameters, the name and the text that is returned by Google. After, the text is cleared from punctuation marks, regex is used to capture the question and the matter of the question. For example, if the question is "What is a car?" the function will return "car".

### text_to_speech(engine, s)
Using the pyttsx3, engine.say(s) will convert the text to sound and will use the voice that is defined in the voice_id variable.

### wiki(text)
The wiki function will use the text that is returned by the extract_word function and will look for the first Wikipedia article and return the first 2 sentences of it. If nothing is found, then “I could not find anything about it" is returned to the text_to_speech function.

### getweather(city)
Using the python_weather library this function checks the temperature in a city that is returned by the extract_word function. In case of python_weather.errors.Error, the function returns "Sorry I didn't understand the city clearly."

### flip_coin()
Using the random module, the function returns either head or tail.

