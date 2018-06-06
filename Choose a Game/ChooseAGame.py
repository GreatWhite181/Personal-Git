from tkinter import *
import random
import time
import math

lineCount = 0
spinCount = 0
colours = ['#2ecc71', '#3498db', '#9b59b6', '#e67e22', '#e74c3c', '#f39c12', '#20e4de', '#43deaf', '#f65ec2', '#c8e734']
colourCount = len(colours)

def chooseGame():
    global gameNumber, spinCount, timer
    gameNumber = random.randrange(0, lineCount)
    text.config(text=Games[gameNumber], fg=colours[random.randrange(0, colourCount)])
    text.update()
    if spinCount != 25:
        spinCount += 1
        time.sleep(math.exp(0.018*spinCount)-1)
        chooseGame()
    else:
        spinCount = 0

with open('Gamelist.txt') as f:
    Games = [i.rstrip('\n') for i in open('Gamelist.txt')]

for i in open('Gamelist.txt'):
    lineCount += 1

root = Tk()

text = Label(root, text="Hi there, press that button.", font=('', 20, 'bold'))
text.grid(pady=15)

Button(root, text="button", command=chooseGame).grid(row=1, padx=150, pady=(0, 15))

root.mainloop()
