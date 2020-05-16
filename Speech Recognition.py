#speech recognition
import webbrowser
import subprocess
import speech_recognition as sr
from time import ctime

r = sr.Recognizer()

def respond(voice_data):
    if "what is your name" == voice_data:
        print(" My Name is Nishi..!")
    elif "what time is it" in voice_data or "what time is it now" in voice_data:
        print(ctime())
    elif "search" in voice_data :
        webbrowser.get().open("https://google.com/search?q="+voice_data)
    elif "open calculator" in voice_data or "calculator" in voice_data:
        subprocess.Popen('C:\\Windows\\System32\\calc.exe')
    elif "notepad" in voice_data or "open Notepad" in voice_data:
        subprocess.Popen('C:\\Windows\\System32\\notepad.exe')          
    elif "wordpad" in voice_data or "open WordPad" in voice_data:
        subprocess.Popen('C:\\Windows\\System32\\write.exe')                
    elif "search on web" in voice_data or "Google" in voice_data or "web" in voice_data or "search on Google" in voice_data:
        webbrowser.get().open("https://google.com")
    elif "write a mail" in voice_data:
        webbrowser.get().open("https://mail.google.com/mail/u/0/#inbox?compose=new")
    elif "check inbox" in voice_data or "check mails" in voice_data or "check mail" in voice_data:
        webbrowser.get().open("https://mail.google.com/mail/u/0/#inbox")
    elif "download" in voice_data or "install" in voice_data:
        webbrowser.get().open("https://google.com/search?q="+voice_data)
    else:
        pass
        
with sr.Microphone() as source :
        print("Speak Anything : ")
        audio = r.listen(source)
        voice_data = ""
        try:
            voice_data = r.recognize_google(audio)
            print("You said : {}".format(voice_data))
            respond(voice_data)
        except:
            print("Sorry Coudn't Recognize")
    
                    
            
        

    
    
