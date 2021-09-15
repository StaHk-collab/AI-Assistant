import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib
import pyautogui
import psutil
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Tony Sir. Please tell me how can I help you")

def takeCommand():
    #it takes microphone input from the user and returns string output

    r=sr.Recognizer()
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

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('hkmahapatra24@gmail.com', 'Enter the password')
    server.sendmail('hkmahapatra24@gmail.com', to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\WELCOME\\Documents\\PROJECTS\\Python Projects\\AI Assistant\\ss.png")

def cpu():
    usage = str(psutil.cpu_percent()) # type cast
    speak('CPU is at'+ usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent )

def jokes():
    speak(pyjokes.get_joke())


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
    # Logic for executing tasks based on queries
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'offline' in query:
            speak("Tony switching to offline mode!!")
            quit()

        elif 'play music' in query:
            music_dir = 'music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0])) 

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir , the time is {strTime}")

        elif 'open vscode' in query:
            codePath = "C:\\Users\\harekrushna\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                speak("What should I say??")
                content = takeCommand()
                to = "harekrushnamahapatra67@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend , I am not able to send this email!!")
        
        elif 'remember that' in query:
            speak("What should I remember?")
            data = takeCommand()
            speak("You said me to remember that"+data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()

        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak("You said me to remember that"+remember.read())

        elif 'screenshot' in query:
            screenshot()
            speak("Screenshot of the current screen is taken!")

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            jokes()




