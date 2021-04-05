
import asyncio
import socketio
import speech_recognition as sr
from gtts import gTTS
import os
#  import pyautogui as pgy
#  import subprocess

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print('connection established')

@sio.event
async def pi_do(data):
    print('message received with ', data)

@sio.event
async def disconnect():
    print('disconnected from server')


def sayCommand(newCommand): 
    print(newCommand)
    tts = gTTS(text=newCommand, lang='en-uk', slow='true')
    tts.save("data/command1.mp3")
    os.system("mpg123 -d 2 data/command1.mp3 &")

#  def googleSearch(command): 
#      sayCommand("Searching for, "+command)
#      os.system("google-chrome --new-window "+"\"http://www.google.com/search?q="+command+"\"")

async def listenForCommand(): 
    print("listening")
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)

        command = r.recognize_google(audio)
        print("Original command: "+command)
        temp = command.split(" ")
        print(temp)

        if (command.lower() == "on"): 
            sio.emit("send_message", {"data": "on"})

        #  if temp[0].lower() == "google": 
        #      googleSearch(command[6:])
        #  elif (command.lower() == "set current project"): 
        #      setCurrentProject()
    except Exception as e:
        print(e)



async def main():
    await sio.connect('http://localhost:5000')
    await sio.wait()
    await listenForCommand()


if __name__ == '__main__':
    asyncio.run(main())
#  sio.connect("localhost://localhost:5000")
#  sio.wait()

