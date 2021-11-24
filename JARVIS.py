import pyttsx3
import speech_recognition as sr
import wikipedia
from ecapture import ecapture as ec
import os
import time
import subprocess
import _json
import requests
import wolframalpha
import datetime

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):

    engine.say(audio) 

    engine.runAndWait() 

def wishMe():

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")    

    speak("I am Jarvis.How may I help you?")
if __name__=="__main__" :
    wishMe()
    

 


