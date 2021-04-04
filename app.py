
import speech_recognition as sr
from gtts import gTTS
import os
#  import pyautogui as pgy
#  import subprocess


def sayCommand(newCommand): 
    print(newCommand)
    tts = gTTS(text=newCommand, lang='en-uk', slow='true')
    tts.save("data/command1.mp3")
    os.system("mpg123 -d 2 data/command1.mp3 &")

#  def googleSearch(command): 
#      sayCommand("Searching for, "+command)
#      os.system("google-chrome --new-window "+"\"http://www.google.com/search?q="+command+"\"")


#  Listening
while (1): 
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)

        command = r.recognize_google(audio)
        print("Original command: "+command)
        temp = command.split(" ")
        print(temp)

        if temp[0].lower() == "google": 
            googleSearch(command[6:])
        elif (command.lower() == "set current project"): 
            setCurrentProject()
    except Exception as e:
        print(e)

