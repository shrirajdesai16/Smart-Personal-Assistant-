import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import time
import tkinter as tk
from tkinter import ttk
from subprocess import call
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
import sys, webbrowser 
import requests
import calander
import demo

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        #e2.delete('1.0',"end-1c")
        print("Listening...")
        #speak("Listening! ")
        #e2.insert("1.0","Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source) 
        audio = r.listen(source,phrase_time_limit=5)

    try:
        #recog()
        print("Recognizing...")
        speak("Procesing")
        query = r.recognize_google(audio, language='en-in')
        
        print(f"User said: {query}\n")
        

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis. Please tell me how may I help you")



def weather_data(query):
	res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric');
	return res.json();


def print_weather(result,city):

	weather=str(result['main']['temp'])
	return(weather)

wishMe()

root = Tk()  # Main window 
f = Frame(root)
frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
root.title("Jarvis")
root.geometry("1080x720")
root.resizable(0,0)
canvas = Canvas(width=1080, height=320)
canvas.pack()
filename=('jarvis.png')
load = Image.open(filename)
load = load.resize((1080, 320), Image.ANTIALIAS)
render = ImageTk.PhotoImage(load)
img = Label(image=render)
img.image = render
#photo = PhotoImage(file='landscape.png')
load = Image.open(filename)
img.place(x=1, y=1)
#canvas.create_image(-80, -80, image=img, anchor=NW)

root.configure(background='black')
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)


id = StringVar()



def click( ):
		r = sr.Recognizer()
		

		with sr.Microphone() as source:

		    print("Listening...")
		    speak("Listening!")
		    
		    r.pause_threshold = 1
		    r.adjust_for_ambient_noise(source) 
		    audio = r.listen(source,phrase_time_limit=5)

		try:
		    global query
		    
		    print("Recognizing...")
		    speak("Wait For Some seconds. command being processed. ")
		    query = r.recognize_google(audio, language='en-in')
		
		    print(f"User said: {query}\n")
		except Exception as e:
		    speak("Say that again please...")
		    print("Say that again please...")  
		    query= "None"

		e1.insert('1.0',"USER SAID :-  "+str(query)+"\n")
		query=query.lower()
		#command processing
		if 'wikipedia' in query:
		    speak('Searching Wikipedia...')
		    query = query.replace("wikipedia", "")
		    results = wikipedia.summary(query, sentences=2)
		    speak("According to Wikipedia")
		    print(results)
		    speak(results)

		elif 'youtube' in query:
		    webbrowser.open("youtube.com")

		elif 'notepad' in query:
		    call(["notepad.exe"])


		elif 'calculator' in query:
		    call(["calc.exe"])


		elif 'calendar' in query:
		    calander.main()

		elif 'weather' in query:
			speak('city name.')
			city=takeCommand()
			query='q='+city;
			w_data=weather_data(query);
			temperature=print_weather(w_data, city)
			speak('Temperature is' +temperature + 'degree celsius')

		elif 'google' in query:
		    webbrowser.open("google.com")

		elif 'open stackoverflow' in query:
		    webbrowser.open("stackoverflow.com")   


		elif 'play music' in query:
		    music_dir = 'Music'
		    songs = os.listdir(music_dir)
		    print(songs)    
		    os.startfile(os.path.join(music_dir, songs[0]))

		elif 'the time' in query:
		    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
		    speak(f"Sir, the time is {strTime}")

		elif 'map' in query:
			speak('start location')
			from_loc=takeCommand()
			speak('destination')
			to_loc=takeCommand()
			webbrowser.open('https://www.google.com/maps/dir/'+from_loc +'/'+to_loc)

		else:
			respons= demo.ai_query(query)
			speak(f"{respons}")
			e1.insert('1.0',"Reply :-  "+str(respons)+"\n")



				


def clear_all():  # for clearing the entry widgets
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()


label1 = Label(root, text="Jarvis")
label1.config(font=('Italic', 18, 'bold'), justify=CENTER, background="Black", fg="white", anchor="center")
label1.pack(fill=X)


frame2.pack_forget()
frame3.pack_forget()

e1 = Text(frame1,height=15, width=70)
e1.grid(row=1, column=2, padx=10,pady=10)


button5 = Button(frame1, text="Speak",command=click)
button5.grid(row=9, column=2, pady=10,padx=10)


frame1.configure(background="#008080")
frame1.pack(pady=10)

frame2.configure(background="#008080")
frame2.pack(pady=10)




root.mainloop()
