import pyttsx3 #python -m pip install pyttsx3 #python -m pip install speechRecognition
import datetime
import wikipedia #python -m pip install wikipedia
import webbrowser
import pyaudio as sr
import os #comes prebuilt
import smtplib #python -m pip install smptlib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait() #makes speech audible in the system


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!"

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir!")

    else:
        speak("Good Evening sir!")

    speak("I am Jarvis! I hope you are doing well! How may I help you?")

def takeCommand():
    #Taking microphone input and returning output as string

    r = pyaudio.Recognizer()
    with pyaudio.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = pyaudio.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Sir, Could you repeat that please?")
        return "None"
    return query

def sendEmail(to, content): #using smptlib properties to send emails
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

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
            speak("According to Wikipedia,")
            print(results)
            speak(results) #printing and speaking the results

        elif 'open youtube' in query:
            webbrowser.open("youtube.com") #using webbrowser package to open websites(including wikipedia)

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            music_dir = "" #add file path/address between the doublt quotes to play songs
            songs = os.listdir(music_dir)
            print(songs) #print all the songs in the file
            os.startfile(os.path.join(music_dir, songs[0])) #staring to play the songs

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") #using datetime package for telling time if the user asks
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query: #if I want to open my code files
            codePath = "" #add path between the double quotes(can change anytime)
            os.startfile(codePath)

        elif 'email to shesh' in query:
            try:
                speak("What exactly should I write, sir?")
                content = takeCommand() #taking input from the user for the content of the email
                to ="rbkshesh@gmail.com" #the email id
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Really sorry sir, but I  am not able to send this email") #if it faces any problem
