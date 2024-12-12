import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import wikipedia
import webbrowser
import smtplib
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    
    speak("I am jarvis sir, Please tell me how may i help you")

def takeCommand():
    #it take microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 
        audio = r.listen(source)

    try:
        print("recognizing...")
        query = r.recognize_google(audio, language = "en-in")
        print("User said: ",query)

    except Exception as e:
        #print(e)
        print("say that again please...")
        return "None"
    return query

def sendEmail(to,content):
     server = smtplib.SMTP('smtp.gmail.com',587)
     server.ehlo()
     server.starttls()
     server.login('yourgemail.com','yourpassword')
     server.sendmail('yourmail@gmail.com',to,content)
     server.close()
if __name__ == "__main__":
    wishMe()
    if 1:
        query = takeCommand().lower()
        #logic for executing task
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 1)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query: 
                webbrowser.open("youtube.com")
        
        elif 'open google' in query: 
                webbrowser.open("google.com")
        
        elif 'open gpt' in query: 
                webbrowser.open("chatgpt.com")
        #elif 'play music' in query: 
            # add directory here
        elif 'the time' in query: 
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")   
        elif 'open code' in query: 
                codepath = "C:\\Users\\Ankit Panwar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codepath)
        elif 'mail' in query: 
            try:
                 speak("what should i say?")
                 content = takeCommand()
                 to = "anymail.com"
                 sendEmail(to,content)
                 speak("Email has been sent")
            except Exception as e:
                 print(e)
                 speak("sorry i am not able to send this email")
