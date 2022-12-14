from obs import obs
from word import word
from file import file
from date import date       
from video import video     
from vscode import code   
from folder import folder  
from chrome import chrome   
from discord import discord 
from website import website 
from currenttime import time
from say import texttospeech 
from cmdline import commandline
from powerpoint import powerpoint
from search import getSerpResults
from calculator import calculator
from greetinguser import greet_user

#Calling Greeting Function from greetinguser.py
greet_user()

#Active for while loop
active = True

#Counter for while loop
counter = 0

#Features inside Jarvis
features = {"calculator", "cmd", "discord", "search", "chrome", "code", "video", "website", "date", "time", "folder", "file", "word",
            "obs", "powerpoint"}

#While loop
while active:
    counter += 1

    #IF statement for counter
    if counter > 1:
        texttospeech("Is there anything else I can assist you with today?")
        repeat = input("Is there anything else I can assist you with today: ").lower()

        #IF statement for no repeat
        if "no" in repeat:
            texttospeech("Have an awesome day!")
            break

    texttospeech("How can I assist you today?")
    userChoice = input("How can I assist you today: ").lower()

    #IF statement for features
    if "features" in userChoice:
        texttospeech("The features I have available are")
        texttospeech(features)
        print(features)
        continue

    #ELIF statement for cmd
    elif "calculator" in userChoice:
        texttospeech("Sure sir opening calculator now!")
        calculator()
        continue

    #ELIF statement for cmd
    elif "cmd" in userChoice:
        texttospeech("Certainly sir opening command line now!")
        commandline()
        continue

    #ELIF statement for discord
    elif "discord" in userChoice:
        texttospeech("Absolutely sir opening discord now!")
        discord()
        continue

    #ELIF statement for search
    elif "search" in userChoice:
        texttospeech("Sure sir, what information do you require?")
        requirement = input("What information do you require: ")
        texttospeech("I hope this website is useful!")
        getSerpResults(requirement)
        continue

    #ELIF statement for chrome
    elif "chrome" in userChoice:
        texttospeech("Certainly sir opening google chrome now!")
        chrome()
        continue

    #ELIF statement for code
    elif "code" in userChoice:
        texttospeech("Opening VS Code now sir!")
        code()
        continue

    #ELIF statement for video
    elif "video" in userChoice:
        texttospeech("Sure sir")
        video()
        continue

    #ELIF statement for website
    elif "website" in userChoice:
        texttospeech("Sure sir")
        website()
        continue

    #ELIF statement for date
    elif "date" in userChoice:
        texttospeech("The current date is")
        date()
        continue

    #ELIF statement for time
    elif "time" in userChoice:
        texttospeech("The current time is")
        time()
        continue

    #ELIF statement for folder
    elif "folder" in userChoice:
        texttospeech("Sure sir")
        folder()
        continue

    #ELIF statement for file
    elif "file" in userChoice:
        texttospeech("Absolutely sir")
        file()
        continue

    #ELIF statement for word
    elif "word" in userChoice:
        texttospeech("Opening word document now")
        word()
        continue

    #ELIF statement for obs
    elif "obs" in userChoice:
        texttospeech("Opening up obs now sir")
        obs()
        continue

    #ELIF statement for powerpoint
    elif "powerpoint" in userChoice:
        texttospeech("Opening up powerpoint now")
        powerpoint()
        continue

    #ELSE statement
    else:
        texttospeech("Sorry sir I do not have that feature available at the moment")
        continue
