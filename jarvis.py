import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("Hello i'am jarvis may i help you?")




def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listenning.....")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognition..")
            query = r.recognize_google(audio,language='en')
            print(f"user said {query}\n")

        except Exception as e:
            print("Say that Again")
            return "None"

        return query




def SendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("unaisnizamani598@gmail.com","anoshaniz")
    server.sendmail("unaisnizamani598@gmail.com",to,content)
    server.close()





if __name__ == '__main__':
  wishme()
  while True:
    query = TakeCommand().lower()

    if 'wikipedia' in query:
        speak("Searching Wikipedia....")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences=2)
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")


    elif 'open google' in query:
        webbrowser.open("google.com")


    elif 'open stack overflow' in query:
        webbrowser.open("stackoverflow.com")

    elif 'who are you' in query:
        speak("Sir,i'm robot and my owner is unais")

    elif 'play music' in query:
        speak("Playing Music")
        music_dir = "E:\\music"
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[0]))


    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Sir,The Time is {strTime}")
        speak(strTime)

    elif 'open code' in query:
        CodePath = "C:\\Users\\anonymous\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(CodePath)

    elif 'send email to' in query:
        try:
            speak("What Should i Say?")
            print("What Should i Say?")
            content = TakeCommand()
            content = TakeCommand()
            to = "unaisniz21@gmail.com"
            SendEmail(to,content)
            speak("Sir,Email has been sent!")


        except Exception as e:
            print(e)
            speak("Sorry Unais i'am not able send email at the moment")
