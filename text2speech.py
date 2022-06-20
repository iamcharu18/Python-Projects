# pip install pyttsx3
# pip install pywin32

import pyttsx3

data = input("Enter text :\n")

engine = pyttsx3.init()
engine.say(data)
engine.runAndWait()
