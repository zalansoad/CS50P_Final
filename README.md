# WBVA - Wikipedia-Based Voice Assistant
#### Video Demo:  <URL HERE>
#### Description:
With the help of the Wikipedia-based Voice Assistant you can easily make wikipedia queriey using your microphone. Furthermore, search for the weather temperature worldwide without a keystroke. Lasltly, you can ask the assistant to flip a coin if you would like to ask the virtual assistant to help you in decission making.

The assistant is always running in the background and is preprogrammed to wake up to the "Hey {name}" wakeword. The name of the assistant is provided as a command line argument.

For example you could use the assistant the following way:
To start the program type in: "python project.py Lucy"
Then using your microphone ask something like "Hey Lucy, what do you know about Harry Potter?"
Lucy will look for an article about Harry Potter on the Wikipedia and read out loud the first 3 senteces.
You can also ask Lucy the following: "Hey Lucy, what is the temperature in New York?"
Lucy will tell you the temperature in Celsius.
Additionally, you can also ask the assistan to flip a coin: "Hey Lucy, flip a coin."
Lucy will tell you the result afterwars.
You can stop the vioce assistant by saying "Stop the program."

**Please note that the program only runs on Windows, since WSL does not support audio devices. Although there are workarounds using the program in WSL, for the best experience run it on Windows**

# Table of Contents

1. [Files and their Function](#files-and-their-function)
   1.1. [project.py](#projectpy)
   1.2. [test_project.py](#test_projectpy)
   1.3. [requirements.txt](#requirementstxt)
2. [The main program: project.py](#the-main-program-projectpy)


## Files and their function.

### project.py
This file stores the program, the mainly Wikipedia based virtual assistant.
### test_project.py
The key function of the project.py file are tested in this file. In this file the following functions are teste: wiki, extract_word, getweather, and flip_coin.
### requirements.txt
In this folder all the necessary libraries are listed which need to be installed before running the program.

## The main program: project.py
The program takes one command line argument, the name of the assistant. If the lenght of the command line argument does not equal to 2 (file name, assistant name) the program exits.