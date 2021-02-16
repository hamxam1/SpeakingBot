import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")

    else:
        speak("Good Evening Sir")
        
    speak("Hi I am H2, How can i help you sir?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing ...")
        query=r.recognize_google(audio,language='en-in')
        print("You said: "+ query)
    except Exception as e:
        print(e)
        print("Speak in English Again")
        return "None"

    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your@email.com','yourpassword')
    server.sendmail('your@email.com',to,content)
    server.close()

if __name__ == "__main__":
    # speak("Hello! My name is ")
    wishMe()
    

    while True:
        query= takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak('According to wikipedia')
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        
        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'play music' in query:
            dir='C:/Users/HP/Desktop/Music'
            songs = os.listdir(dir)
            os.startfile(os.path.join(dir,songs[0]))
        elif 'the time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak("The current time is "+ time)
        elif 'send email' in query:
            try:
                speak("What should I write in email?")
                content = takeCommand()
                to = "towhomyouwanttosend"
                sendEmail(to,content)
                speak("Email has been sent sir.")
            except Exception as e:
                speak("Sorry sir there is some probelm. I can't send the email.")
        elif 'terminate' in query:
            speak("See you soon sir.")
            exit()
        
        elif 'thank you' in query:
            speak("I am always here for you sir.")

        elif 'what can you do for me' in query:
            speak("I can search something in wikipedia, open youtube, open google, play music,tell you the current time, send email to your brother and so on.")
