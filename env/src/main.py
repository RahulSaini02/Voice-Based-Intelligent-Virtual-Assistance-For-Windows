# Import Libraries
import datetime
import warnings
import calendar
import winsound
import random
import os
import webbrowser
import smtplib
import requests
import json
import sys
from urllib.request import urlopen
import speech_recognition as sr  # pip install speechRecognition
from gtts import gTTS  # pip install gTTS
import wikipedia  # pip install wikipedia
import pyttsx3  # pip install pyttsx3
import wolframalpha  # pip install wolframalpha
from selenium import webdriver  # pip install selenium
from selenium.webdriver.common.keys import Keys

# Import Files
from date import getDate
from PresentTime import getTime
from weather import getWeather
from headlines import getHeadlines
from news import getNews
from song import getLyrics
from reminder import makeRemainder
from text import getText
from SnakeGame import SnakeGame
from RockPaperScissors import RockPaperScissors


# Ignore warning messages
warnings.filterwarnings('ignore')

# Voice Engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# A function for virtual assistance responds
def speak(audio):
    # Convert text to speech
    engine.say(audio)
    engine.runAndWait()
    print(audio)

# Function to wish
def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning!')

    elif hour >= 12 and hour < 18:
        speak('Good Afternoon!')

    else:
        speak('Good Evening!')

    speak('How can I help you!')

# Record Audio and return as string
def takeCommand():
    # Record the audio
    r = sr.Recognizer()

    # Open Microphone and record audio
    with sr.Microphone() as source:
        print('listening...!')
        r.pause_threshold = 0.8
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    command = ''

    # Using google speech recoginition
    try:
        print('Recognizing..')
        query = r.recognize_google(audio, language='en-in')
        query.lower()
        print(f"You said: {query}\n")

    except Exception as e:
        speak('Say that again please...')
        return "None"

    return query.lower()

# Main
if __name__ == "__main__":
    greet()
    while True:
        query = takeCommand().lower()
        response = ''

        # Logic for executing tasks
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            wiki = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(wiki)

        elif 'search' in query:
            query = query.replace("search", "")
            wiki = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(wiki)

        elif 'who are you' in query:
            speak('Im Friday your voice assistant') 

        elif 'open' in query:
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            if 'youtube' in query:
                webbrowser.get(chrome_path).open('youtube.com')
            elif 'gmail' in query:
                webbrowser.get(chrome_path).open('mail.google.com')

            elif 'facebook' in query:
                webbrowser.get(chrome_path).open("facebook.com")

            elif 'google' in query:
                webbrowser.get(chrome_path).open("google.co.in")

            elif 'whatsapp' in query:
                webbrowser.get(chrome_path).open("web.whatsapp.com")

            elif 'geeks for geeks' in query:
                webbrowser.get(chrome_path).open("geeksforgeeks.org")
                
            elif 'vs code' in query or 'visual studio code' in query or 'vscode' in query or 'code' in query:
                # app_path = "C:\\Users\\saini\\AppData\\Local\\Programs\\Microsoft VSC\\Code.exe"
                # os.startfile(app_path)
                os.system('code')
            
            elif 'notepad' in query:
                os.system('notepad')

        elif 'play music' in query:
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            song_num = random.randint(0,len(songs))
            os.startfile(os.path.join(music_dir, songs[song_num]))

        elif 'date' in query:
            get_date = getDate()
            response = response +' '+get_date
            speak(response)

        # Check is user said about time
        elif 'time' in query:
            get_time = getTime()
            response = response +' '+get_time
            speak(response)


        elif 'weather' in query:
            get_weather = getWeather()
            speak(get_weather)


        elif 'news' in query:
            speak('about what news do you want to know')
            q = takeCommand().lower()
            get_news = getNews(q)
            for i in get_news:
                speak(i)

        elif 'headlines' in query:
            get_headlines = getHeadlines()
            speak('Today headlines are')
            for i in get_headlines:
                speak(i)

        elif 'lyrics' in query:
            query = query.replace('lyrics', '')
            song = getLyrics(query)
            print(song)

        elif 'sing a song' in query:
            speak('which song do you want me to sing')
            song_name = takeCommand().lower()
            song = getLyrics(song_name)
            speak(song)

        elif 'make a reminder' in query or 'reminder' in query or 'set a reminder' in query or 'set reminder' in query:
            speak('What is the reminder?')
            content = takeCommand().lower()
            speak('When do you want to be reminded?')
            time = takeCommand().lower()
            remind = makeRemainder(content, time)
            speak('Okay!' + remind)

        elif 'read text' in query:
            txt = getText()
            speak(txt)

        elif 'play a game' in query or 'play game' in query:
            speak(
                'what game do you want to play? (1)Snake Game or (2)Rock-Paper-Scissors')
            choice = takeCommand().lower()
            if 'snake game' in choice or '1' in choice or 'one' in choice:
                play_game = SnakeGame()
                
            elif 'rock paper scissors' in choice or '2' in choice or 'two' in choice:
                play_game = RockPaperScissors()

        elif 'snake game' in query:
                play_game = SnakeGame()

        elif 'rock paper scissors' in query:
                play_game = RockPaperScissors()

        elif 'shutdown pc' in query:
            os.system("shutdown /s /t 1")

        elif 'restart pc' in query:
            os.system("shutdown /r /t 1")

        # Exit
        elif 'stop' in query:
            speak('Friday is shutting down!')
            sys.exit()