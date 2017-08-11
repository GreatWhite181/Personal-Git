#By Leon Salsiccia
#Started on June 28th 2017

import random   #import dependencies
try:    #try to import tkinter for python 3, else import tkinter for python 2
    from Tkinter import *
except ImportError:
    from tkinter import *
import linecache as linecache

lowestNumber = 1    #variables
highestNumber = 100
count = 0
counterStat = False
numberOfGuesses = 0
secret = 0
user = linecache.getline("text files/loginStatus.txt", 2)[0:-1]
easyDifficulty = 100
mediumDifficulty = 500
hardDifficulty = 1000

def counter():  #define counter
    global count, counterStat, secret   #set global variables
    if guess != str(secret):    #increase timer when they havent guessed correctly
        count += 1
        root.after(1000, counter)   #repeat after 1 second
    else:   #when they guess correctly, reset timer
        count = 0
        counterStat = False
        secret = random.randrange(lowestNumber, highestNumber)  #set new random number

def run(*args):
    global guess, counterStat, gameMsg, numberOfGuesses #set global variables
    gameMsg.grid(row=3, pady=(0, 10))   #place game message widget
    guess = guessEntry.get()    #grab user input from entry box
    numberOfGuesses += 1    #increment the number of guesses user has taken this turn
    if counterStat == False:    #checks to see if they have started guessing
        counterStat = True #prevent counter from overlapping
        counter()   #start timer
    if guess.isdigit() and int(guess) == secret and count == 0: #if they guess it first try
        gameMsg.config(text='WOW! You Guessed that first try! Ver Gud.')    #change the text of gameMsg Label widget
        guessEntry.delete(0, END)   #clear entry box input
        gameMsg.update()    #update gameMsw Label with new text
        numberOfGuesses = 0 #reset number of guesses
    elif guess.isdigit() and int(guess) == secret:  #if they guess it not on first try
        correctAnswer() #go to correctAnswer Def
        guessEntry.delete(0, END)
        gameMsg.update()
        root.after (5000, lambda: gameMsg.grid_remove())    #after 5 seconds, remove the message
        numberOfGuesses = 0
    elif guess.isdigit() and int(guess) > secret and int(guess) <= highestNumber:   #if they guessed too high
        gameMsg.config(text='Too high! Try Again.')
        guessEntry.delete(0, END)
        gameMsg.update()
    elif guess.isdigit() and int(guess) < secret and int(guess) >= lowestNumber:    #if they guessed too low
        gameMsg.config(text='Too low! Try Again.')
        guessEntry.delete(0, END)
        gameMsg.update()
    else:
        gameMsg.config(text='Sorry, but "' + guess + '" is not a valid option.\nPlease try again.') #if they input an invalid option
        guessEntry.delete(0, END)
        gameMsg.update()

def correctAnswer():    #check what difficulty they chose, update the response based on selectin
    if highestNumber == easyDifficulty:
        correctAnswerResponse(3, 7)
    elif highestNumber == mediumDifficulty:
        correctAnswerResponse(5, 10)
    elif highestNumber == hardDifficulty:
        correctAnswerResponse(8 ,13)
    else:   #for the custom user set range
        gameMsg.config(text='Nice, ' + user + '!\nYou got it in ' + str(count) +
        ' seconds and ' + str(numberOfGuesses) + ' Guesses!\nI\'ll randomise it again for you.')

def correctAnswerResponse(x, y):    #display various outputs depending on user performance
    if numberOfGuesses <= x:    #updates arguments depending on difficulty chosen
        gameMsg.config(text='Out of this World, ' + user + '.\nYou got it in ' + str(count) +
        ' seconds and ' + str(numberOfGuesses) + ' Guesses!\nI\'ll randomise it again for you!')
    elif numberOfGuesses > x and numberOfGuesses <= y:
        gameMsg.config(text='Pretty good, ' + user + '.\nYou got it in ' + str(count) +
        ' seconds and ' + str(numberOfGuesses) + ' Guesses!\nI\'ll randomise it again for you!')
    elif numberOfGuesses > y:
        gameMsg.config(text='Shabby, ' + user + '.\nYou got it in ' + str(count) +
        ' seconds and ' + str(numberOfGuesses) + ' Guesses.\nI\'ll randomise it again for you.')

def setDifficulty(lowest, highest): #sets difficulty depending on user input
    global lowestNumber, highestNumber, secret  #set globals
    lowestNumber = lowest
    highestNumber = highest
    instruction.config(text="Please enter a number between " + str(lowestNumber) + " and " +
                  str(highestNumber) + ".") #intruction message that updates depending on difficulty
    instruction.update()
    secret = random.randrange(lowestNumber, highestNumber)  #set secret
    setFrame.grid_remove()  #clears other windows
    diffFrame.grid_remove()
    gameMsg.grid_remove()   #removes the message
    gameFrame.grid()    #place main game
    if highestNumber == easyDifficulty: #update colour of game depending on difficulty
        setGameColour("easy")
    elif highestNumber == mediumDifficulty:
        setGameColour("medium")
    elif highestNumber == hardDifficulty:
        setGameColour("hard")

def setGameColour(difficulty):  #sets colours for each difficulty
    global gameFrameColour, gameFrameColour_Button  #set global variables
    if difficulty == "easy":
        gameFrameColour = "#a9f160"
        gameFrameColour_Button = "#c4f493"
    elif difficulty == "medium":
        gameFrameColour = "#f1aa60"
        gameFrameColour_Button = "#f1c08d"
    elif difficulty == "hard":
        gameFrameColour = "#f16069"
        gameFrameColour_Button = "#f47980"
    updateGameColour()  #goto def

def updateGameColour(): #applys the new colour changes
    for i in gameFrame.winfo_children():    #for each widget in the game frame
        if 'Button' not in str(i.winfo_class()) and 'Entry' not in str(i.winfo_class()):    #if it isnt a button or entry box
            i.config (bg=gameFrameColour)   #colour it the new colour
        elif 'Button' in str(i.winfo_class()):    #if its a button
            i.config (bg=gameFrameColour_Button)    #colour it the new button colour
        gameFrame.config (bg=gameFrameColour)   #set the frame background colour

def setCustomNumbers(): #let user choose their own numbers
    global gameFrameColour, gameFrameColour_Button  #set global variables
    customHigh = highSet.get()  #get custom high number from entry box
    customLow = lowSet.get()    #get custom low number from entry box
    highSet.delete(0, END)  #clear entry boxes
    lowSet.delete(0, END)

    gameFrameColour = "#abacff" #set game colours
    gameFrameColour_Button = "#c0c1fb"

    if customLow.isdigit() and customHigh.isdigit() and int(customLow) < int(customHigh):   #check to see if the custom numbers are valid
        setFrame.grid_remove()  #remove the set numbers window
        updateGameColour()  #update colours
        setDifficulty(int(customLow), int(customHigh))  #set custom difficulty
    else:
        if customLow.isdigit() and customHigh.isdigit() and int(customLow) > int(customHigh):   #checks if the lower number is higher
            customLabel.config(text="Lowest number can't be larger than Highest number.")
        else:   #if user input anything else that is invalid
            customLabel.config(text="Sorry, but '" + customHigh + "' and '" + customLow + "' are not valid entries.")
        customLabel.update()
        root.after(4000, lambda: customLabel.config(text=""))   #after 4 seconds, clear text
        customLabel.update()

def callWelcomeFrame(): #displays the first welcome window
    global count, counterStat, guess, numberOfGuesses    #define globals
    gameFrame.grid_remove() #remove the main game frame
    diffFrame.grid_remove() #removes difficulty window
    setFrame.grid_remove()
    welcomeFrame.grid()    #place difficulty selection frame
    guessEntry.delete(0, END)    #reset guess entry box
    count = 0   #reset count
    counterStat = 0 #reset counter status
    numberOfGuesses = 0 #reset guesses counter
    guess = str(secret) #stop timer

def callDiffFrame():    #removes all other open windows and opens the difficulty window
    welcomeFrame.grid_remove()
    helpFrame.grid_remove()
    gameFrame.grid_remove()
    diffFrame.grid()

def callCustomFrame():  #display custom number window
    setFrame.grid(column=1, row=0)

def killTk(*args):
    root.destroy()  #quit the program

textColour = "#2a2a2a"  #variables for each colour
welcomeFrameColour = "#60b4f1"
welcomeFrameColour_Button = "#8ec8f2"
helpFrameColour = "#93f160"
helpFrameColour_Button = "#b2f48e"
diffFrameColour = "#f47980"
diffFrameColour_Button = "#f4adb1"
gameFrameColour = "#e6e585"
gameFrameColour_Button = "#f6f6a2"
setFrameColour = "#eee272"
setFrameColour_Button = "#eee589"


root = Tk() #define tkinter
root.attributes("-topmost", True)   #make window topmost
root.title("Guessing Game by Leon Salsiccia") #set title

#Welcome Screen ##################
welcomeFrame = Frame(bg=welcomeFrameColour) #create new frame
Label(welcomeFrame, text="Welcome, " + user + ",\n to 'A Guessing Game'!", font=('', 18, 'bold', 'italic'), fg=textColour).grid(row=0, padx=15,
 pady=15)   #set and place text with user's name
Button(welcomeFrame, text="Start!", command=callDiffFrame, width=8).grid(row=1) #place start and help buttons
Button(welcomeFrame, text="Help!", command=lambda: helpFrame.grid(column=1,row=0), width=8).grid(sticky=E, row=1, padx=(0, 10))

tempWelcomeImage = PhotoImage(file= "pictures/welcomeFrame.gif")   #set image path
Label(welcomeFrame, image=tempWelcomeImage).grid(padx=65, pady=15, row=2)   #place image

for i in welcomeFrame.winfo_children(): #colour all elements in frame
    if 'Button' not in str(i.winfo_class()):
        i.config (bg=welcomeFrameColour)
    else:
        i.config (bg=welcomeFrameColour_Button)
##################################

#Help Screen #####################
helpFrame = Frame(bg=helpFrameColour)   #create new frame
Label(helpFrame, text="1. Click \"Start!\"\n2. Choose a difficulty\n(or choose your own numbers)\n3. Guess what the number is\n\nClick \"Back\" to return to the title\n\nFor further help, refer to the manual.", font=('', 16)).grid(padx=10,
 pady=15)   #help text
Button(helpFrame, text="Close!", command=lambda: helpFrame.grid_remove(), width=8).grid(pady=(5, 17))  #close button

for i in helpFrame.winfo_children():    #colour all elements in frame
    if 'Button' not in str(i.winfo_class()):
        i.config (bg=helpFrameColour)
    else:
        i.config (bg=helpFrameColour_Button)
##################################

#Difficulty Select ###############
diffFrame = Frame(bg=diffFrameColour)   #create new frame
Label(diffFrame, text="Choose a Difficulty.", font=('', 18, 'bold', 'italic'), fg=textColour).grid(row=0,
 column=0, columnspan=3, padx=15, pady=(15, 0))
Button(diffFrame, text="Easy", command=lambda: setDifficulty(1, easyDifficulty), width=8).grid(row=1, column=0, padx=(35, 0))   #create various difficulty buttons
Button(diffFrame, text="Medium", command=lambda: setDifficulty(1, mediumDifficulty), width=8).grid(row=1, column=1, pady=15, padx=40)
Button(diffFrame, text="Hard", command=lambda: setDifficulty(1, hardDifficulty), width=8).grid(row=1, column=2, padx=(0, 35))

tempDiffImage = PhotoImage(file= "pictures/diffFrame.gif")   #set image path
Label(diffFrame, image=tempDiffImage).grid(padx=15, pady=(0, 45), columnspan=3) #display image

Button(diffFrame, text="Back", command=callWelcomeFrame, width=8).grid(row=2, pady=10, padx=(15, 0), sticky=SW) #display back and custom numbers buttons
Button(diffFrame, text="Custom", command=callCustomFrame, width=8).grid(row=2, column=2, pady=10, padx=(0, 15), sticky=SE)

for i in diffFrame.winfo_children():    #colour all elements in frame
    if 'Button' not in str(i.winfo_class()):
        i.config (bg=diffFrameColour)
    else:
        i.config (bg=diffFrameColour_Button)
##################################

#Main Game #######################
gameFrame = Frame(bg=gameFrameColour)   #create new frame
instruction = Label(gameFrame, text="", font=('', 18, 'bold', 'italic'))    #create placeholder text with custom font and size
instruction.grid(padx=15, pady=(15, 0), row=0, column=0) #place instruction message
guessEntry = Entry(gameFrame)   #create entry widget
guessEntry.grid(row=1)  #place entry widget
Button(gameFrame, text="Go!", command=run, width=8).grid(row=2, pady=15)    #create go and back buttons
Button(gameFrame, text="Back", command=callWelcomeFrame, width=8).grid(row=2, pady=15, padx=(15, 0), sticky=W)
gameMsg = Label(gameFrame, font=('', 11))   #placeholder label to be configured automatically

for i in gameFrame.winfo_children():    #colour all elements in frame
    if 'Button' not in str(i.winfo_class()) and 'Entry' not in str(i.winfo_class()):
        i.config (bg=gameFrameColour)
    elif 'Button' in str(i.winfo_class()):
        i.config (bg=gameFrameColour_Button)
##################################

#Set Own Numbers #################
setFrame = Frame(bg=setFrameColour) #create new frame
Label(setFrame, text="Set your own numbers.", font=('', 18, 'bold', 'italic')).grid(padx=45, pady=(15, 15), columnspan=2)   #create text
Label(setFrame, text="Highest: ").grid(row=1, sticky=E, pady=(0, 15))
highSet = Entry(setFrame)   #create entry box
highSet.grid(row=1, column=1, pady=(0, 15), sticky=W)
Label(setFrame, text="Lowest: ").grid(row=2, sticky=E, pady=(0, 15))
lowSet = Entry(setFrame)
lowSet.grid(row=2, column=1, pady=(0, 15), sticky=W)
customLabel = Label(setFrame, font=('', 11))    #placeholder label to be configured automatically
customLabel.grid(row=3, pady=(0, 15), columnspan=2)
Button(setFrame, text="Set", command=setCustomNumbers, width=12).grid(row=4, columnspan=2)  #display set and close buttons
Button(setFrame, text="Close", command=lambda: setFrame.grid_remove(), width=8).grid(row=5, columnspan=2, pady=(27, 15))

for i in setFrame.winfo_children(): #colour all elements in frame
    if 'Button' not in str(i.winfo_class()) and 'Entry' not in str(i.winfo_class()):
        i.config (bg=setFrameColour)
    elif 'Button' in str(i.winfo_class()):
        i.config (bg=setFrameColour_Button)
#################################

welcomeFrame.grid() #call welcome frame to start the program

root.bind('<Return>', run)  #bind enter key to run definition
root.bind('<Escape>', killTk)   #bind escape to end program
root.mainloop() #loop tkiner
