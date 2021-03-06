
#  import asyncio
#  import socketio
import speech_recognition as sr
#  from gtts import gTTS
import os
import requests

#  URL = "http://0.0.0.0:5000/"
URL = 'http://doranelle.kevinhsu.net:5000/'

def sayCommand(newCommand): 
    print(newCommand)
    tts = gTTS(text=newCommand, lang='en-uk', slow='true')
    tts.save("data/command1.mp3")
    os.system("mpg123 -d 2 data/command1.mp3 &")

#  def googleSearch(command): 
#      sayCommand("Searching for, "+command)
#      os.system("google-chrome --new-window "+"\"http://www.google.com/search?q="+command+"\"")



while(1): 
    print("listening")
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)

        command = r.recognize_google(audio)
        print("Original command: "+command)
        #  temp = command.split(" ")
        #  print(temp)

        processedCommand = command.lower()
        print("processedCommand: " + processedCommand)

        if (processedCommand == "open mask"): 
            #  sio.emit("send_message", {"data": "on"})
            print("sending message 'open mask' to server")
            res = requests.post(URL + "voice_command", json={'message': "open mask" })
        elif (processedCommand == "down"): 
            #  sio.emit("send_message", {"data": "on"})
            print("sending message 'down' to server")
            res = requests.post(URL + "voice_command", json={'message': "close mask" })


        #  if temp[0].lower() == "google": 
        #      googleSearch(command[6:])
        #  elif (command.lower() == "set current project"): 
        #      setCurrentProject()
    except Exception as e:
        print(e)

