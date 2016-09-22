# coding=UTF-8  #declare utf-8 encoding type for degree symbol
import datetime
now = datetime.datetime.now()  # import datetime and get current day
import subprocess   # import os function for opening python script
try:    # rule to be able to use the program on both python 2 and python 3
    from Tkinter import *  # try to import tkinter for python 2
except ImportError:  # if error when importing for python 2
    from tkinter import *  # import tkinter for python 3
from GuessingGame import startGuessing  # import Guessing Game python file

EasterEggs = ['Darth', 'Chew', 'Chicken', 'Doughnut',
              'Falcon', 'Food', 'Ice Cream', 'R2-D2', 'Storm', 'Toast', ]
EasterEggsLower = [element.lower() for element in EasterEggs]


def killTk(*args):  # kill def
    root.destroy()  # close tkinter window


def ee(egg):   # easter egg def
    global Label, text, image, imageTemp   # define globals
    image.grid_remove()  # remove previous widgets
    text.grid_remove()
    text = Label(root, text="You found an easter egg!\nTry to find them all!",
                 fg="#2ECC71", font=("", 17, "bold", "italic"))  # set text
    text.grid(row=4, column=1, columnspan=2, padx=17, pady=(0, 0))    # call text
    imageTemp = PhotoImage(file="pictures/" + egg + ".gif")   # set image
    image = Label(root, image=imageTemp)    # assign image to label
    image.grid(row=6, column=1, columnspan=2, padx=7, pady=7)  # call label with image
    temp()


def option(mode):   # define what happens depending on user input
    global Label, text, image, imageTemp   # assign globals to variables used
    image.grid_remove()  # clear image
    text.grid_remove()  # clear output text
    text = Label(root, text="The current weather today on " + now.strftime("%A") + " is '" + mode +
                 "' \nwith a cloud percentage of " + wValue + "%.", fg="#44423C", font=("", 16, "bold", "italic"))
    text.grid(row=4, column=1, columnspan=2, pady=(17, 0))    # print text in tkinter window
    imageTemp = PhotoImage(file="pictures/" + mode + ".gif")    # choose iamge
    image = Label(root, image=imageTemp)    # assign image
    image.grid(row=6, column=1, columnspan=2, padx=7, pady=7)  # call image
    temp()


def error(mode):    # define what happens when user does not input correctly
    global Label, text, image, imageTemp   # assign globals
    image.grid_remove()  # remove image
    text.grid_remove()  # remove output text
    text = Label(root, text="sorry, '" + mode + "' is not an option. \nTry entering a number between 1 and 100.",
                 fg="#EC3826", font="Helvetica 15 bold italic")
    text.grid(row=4, column=1, columnspan=2, padx=17, pady=(17, 0))    # print text in tkinter window
    imageTemp = PhotoImage(file="pictures/error.gif")    # choose iamge
    image = Label(root, image=imageTemp)    # assign image
    image.grid(row=6, column=1, columnspan=2, pady=7, padx=7)  # call image
    temp()


def weather(*args):  # if statements and def's depending on user input
    global wValue
    wValue = weatherValue.get()  # set variable to entry box input
    if wValue.isdigit() and int(wValue) <= 20:
        option("clear")  # jump to def with unique assign
    elif wValue.isdigit() and int(wValue) <= 40:
        option("shower")    # ''
    elif wValue.isdigit() and int(wValue) <= 60:
        option("slightly cloudy")   # ''
    elif wValue.isdigit() and int(wValue) <= 90:
        option("cloudy")    # ''
    elif wValue.isdigit() and int(wValue) <= 100:
        option("overcast")  # ''
    elif wValue == 'Guessing Game':
        image.grid_remove()
        startGuessing()
        # subprocess.call('python GuessingGame.py', shell=True)    # start
        # guessing game python script
    elif wValue in EasterEggs or wValue in EasterEggsLower:
        ee(wValue)
    else:
        error(wValue)    # jump to error when user input is bad


def temp(*args):  # if statements and def's depending on user input
    global tValue, labelT    # set globals
    tValue = tempValue.get()  # set variable to entry box input
    if '-' in tValue:   # if '-' in input
        tValueCheck = tValue.replace('-', '')    # remove '-'
        if tValueCheck.isdigit():   # if input is digit
            if int(tValue) <= 0:    # if input lower than 0
                labelT.grid_remove()    # remove text
                labelT = Label(root, text="It's freezing out there with a Temperature of " + str(tValue) +
                               "°C.\n You should bring some snow gear", fg='#19D9F7',
                               font=("", 16, "bold", "italic"))  # set text
                labelT.grid(column=1, row=5, columnspan=2, pady=(12, 0))  # call text
        else:   # if not digit
            labelT.grid_remove()    # remove text
            labelT = Label(root, text="Sorry, '" + tValue + "' is not a valid Temperature.",
                           fg='#F32D2D', font=("", 16, "bold", "italic"))  # set error message
            labelT.grid(column=1, row=5, columnspan=2, pady=(12, 0))  # call text
    elif tValue == '':  # if input is empty
        labelT.grid_remove()    # remove text
    elif tValue.isdigit() and int(tValue) <= 5:  # ''
        labelT.grid_remove()    # ''
        labelT = Label(root, text="It's pretty cold today with a Temperature of " + str(tValue) +
                       "°C.\n You May also need a beanie.", fg='#50BFEF', font=("", 16, "bold", "italic"))   # ''
        labelT.grid(column=1, row=5, columnspan=2, pady=(12, 0))  # ''
    elif tValue.isdigit() and int(tValue) <= 15:
        labelT.grid_remove()
        labelT = Label(root, text="It's cool today with a Temperature of " + str(tValue) +
                       "°C.\n You might want to wear a jacket.", fg='#2D4EF3', font=("", 16, "bold", "italic"))
        labelT.grid(column=1, row=5, columnspan=2, pady=(12, 0))
    elif tValue.isdigit() and int(tValue) <= 25:
        labelT.grid_remove()
        labelT = Label(root, text="It's warm Today with a Temperature of " + str(tValue) +
                       "°C.\n Shorts would be a wise decision.", fg='#F0B11E', font=("", 16, "bold", "italic"))
        labelT.grid(column=1, row=5, columnspan=2, pady=(12, 0))
    elif tValue.isdigit() and int(tValue) <= 35:
        labelT.grid_remove()
        labelT = Label(root, text="It's hot today with a Temperature of " + str(tValue) +
                       "°C.\nShorts and a T-Shirt are you're best bet.", fg='#F29816',
                       font=("", 16, "bold", "italic"))
        labelT.grid(column=1, row=5, columnspan=2, pady=(12, 0))
    elif tValue.isdigit() and int(tValue) <= 45:
        labelT.grid_remove()
        labelT = Label(root, text="It's Burning out there with a Temperature of " + str(tValue) +
                       "°C!\nYou should consider going for a swim.", fg='#FC6A21',
                       font=("", 16, "bold", "italic"))
        labelT.grid(column=1, row=5, columnspan=2, pady=(12, 0))
    elif tValue.isdigit() and int(tValue) > 45:
        labelT.grid_remove()
        labelT = Label(root, text="Only Bear Grills can help you in a desert with a Temperature of " +
                       str(tValue) + "°C.\n", fg='#F32D2D', font=("", 16, "bold", "italic"))
        labelT.grid(column=1, row=5, columnspan=2, pady=(12, 0))
    else:   # if input is bad
        labelT.grid_remove()    # remove text
        labelT = Label(root, text="Sorry, '" + tValue + "' is not a valid Temperature.",
                       fg='#F32D2D', font=("", 16, "bold", "italic"))  # set error message
        labelT.grid(column=1, row=5, columnspan=2, pady=(12, 0))  # call text

root = Tk()  # define Tk as root
root.attributes("-topmost", True)   # main attributes for topmost window
root.title("Weather Calculator v2.7")  # title

text = Label(root, text="placeholder")
weatherValue = StringVar()  # set variable to StringVar type
tempValue = StringVar()  # set variable to StringVar type

labelT = Label(root, text="", font=("", 1))  # palce holder

Label(root, text="Welcome to Leon and Justin's Weather Calculator v2.7!", fg="#fe7e00",
      font=("", 18)).grid(column=1, columnspan=2, pady=(7, 0), padx=5)
Label(root, text="Please input the current cloud cover %\nand the current temperature.",
      fg="#41a3c8", font=("", 18)).grid(row=1, column=1, columnspan=2, pady=(0, 10))

weather_entry = Entry(root, width=20, textvariable=weatherValue)
weather_entry.grid(row=2, column=1, columnspan=2)

temp_entry = Entry(root, width=20, textvariable=tempValue)
temp_entry.grid(row=3, column=1, columnspan=2, pady=(0, 10))

Label(root, text="Cloud Percentage (%): ").grid(row=2, column=1, padx=(0, 80), pady=(0, 5))
Label(root, text="Temperature (°C): ").grid(row=3, column=1, padx=(0, 57), pady=(0, 5))

Button(root, text="Calculate", command=weather, bg="#fe7e00", fg="#FDFEFE").grid(
    row=2, column=2, columnspan=2, rowspan=2, pady=(0, 10), padx=(0, 60))
Button(root, text="Quit", command=killTk, bg="#ec5043", fg="#FDFEFE").grid(
    row=2, column=2, rowspan=2, sticky=(E), padx=10, pady=(0, 10))

imageTemp = PhotoImage(file="pictures/B2.gif")
image = Label(root, image=imageTemp)
image.grid(column=1, columnspan=2, padx=7, pady=7)

weather_entry.focus()
root.bind('<Return>', weather)
root.bind('<Escape>', killTk)

root.focus_force()
root.mainloop()
