#update the paths according to your system in the open commands

import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


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

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music in spotify' in query:
            SongPath = r"C:\Users\MOHIT DASH\OneDrive\Desktop\Spotify.lnk"
            os.startfile(SongPath)
                
            

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = r"C:\Users\MOHIT DASH\OneDrive\Desktop\Visual Studio Code.lnk"
            os.startfile(codePath)
        elif 'open word' in query:
            wordPath=r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk"
            os.startfile(wordPath)

        elif 'open excel' in query:
            excelPath=r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk"
            os.startfile(excelPath)

        elif 'open ppt' in query:
            pptPath=r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk"
            os.startfile(pptPath)

        elif 'hello' in query:
            speak("Hello, I am happy meeting you")
        

        elif 'thanks' in query:
            speak("It is a pleasure helping you")

        elif 'open github' in query:
            webbrowser.open("www.github.com")
           
        elif 'deactivate' in query:
                speak ("Deactivating")
                print("Deactivating...")
                quit()
        
        elif 'open maps' or 'open google maps' in query:
            speak("opening maps")
            print("Opening maps...")
            webbrowser.open(r'www.google.com/maps')
