import random
try:
    from Tkinter import *
except ImportError:
    from tkinter import *


def startGuessing():
    global x, y, lowest, highest, instr, secret, guessStr, output, main, guess, guessEntry, lowSet
    x = 1
    y = 100

    def remove():
        global main
        main.grid_remove()

    def set(*args):
        global x, y, lowest, highest, instr, secret
        x = int(lowest.get())
        y = int(highest.get())
        instr.grid_remove()
        instr = Label(main, text="Please enter a number between " + str(x) + " and " +
                      str(y) + ".", font=('', 20, 'bold', 'italic'), fg="#42D8A1")
        instr.grid(columnspan=2, row=2, column=0)
        secret = random.randrange(x, y + 1)

    def go(*args):
        global x, y, lowest, highest, instr, secret, guessStr, output, main, guess, guessEntry, lowSet
        guessStr = guess.get()
        if guessStr.isdigit() and int(guessStr) > secret and int(guessStr) >= x and int(guessStr) <= y:
            output.grid_remove()
            output = Label(main, text="Too High! Try Again!", font=('', 20, 'bold'), fg="#333333")
            output.grid(row=5, column=0, columnspan=2, pady=(3, 15))
        elif guessStr.isdigit() and int(guessStr) < secret and int(guessStr) >= x and int(guessStr) <= y:
            output.grid_remove()
            output = Label(main, text="Too Low! Try Again!", font=('', 20, 'bold'), fg="#333333")
            output.grid(row=5, column=0, columnspan=2, pady=(3, 15))
        elif guessStr.isdigit() and int(guessStr) == secret:
            output.grid_remove()
            output = Label(main, text="Nice! You Got It!\nI'll Randomise it again for you.", font=(
                '', 20, 'bold'), fg='#38E635')
            output.grid(row=5, column=0, columnspan=2, pady=(3, 15))
            secret = random.randrange(x, y + 1)
        else:
            output.grid_remove()
            output = Label(main, text='Sorry, "' + guessStr + '" is not an option.',
                           font=('', 20, 'bold'), fg='#E63555')
            output.grid(row=5, column=0, columnspan=2, pady=(3, 15))

    secret = random.randrange(x, y + 1)

    main = Frame()
    main.grid(row=7, column=1, columnspan=2)

    guess = StringVar()

    Frame(main, height=2, bd=1, relief=SUNKEN).grid(
        sticky=E + W, padx=10, pady=(15, 5), columnspan=2, row=0)

    output = Label(main, text="", font=('', 1))
    output.grid(row=5, column=0, columnspan=2)

    Label(main, text="Welcome to My Guessing Game, By Lon!", font=('', 26, 'bold', 'italic'),
          fg="#D84279").grid(padx=45, pady=(15, 0), columnspan=2, row=1, column=0)
    instr = Label(main, text="Please enter a number between " + str(x) + " and " +
                  str(y) + ".", font=('', 20, 'bold', 'italic'), fg="#42D8A1")
    instr.grid(columnspan=2, row=2, column=0)
    guessEntry = Entry(main, textvariable=guess)
    guessEntry.grid(row=3, column=0, columnspan=2, pady=10)
    Button(main, text="GO!", command=go).grid(row=4, columnspan=2, pady=(0, 10))

    lowest = StringVar()
    highest = StringVar()

    Label(main, text="Set your own numbers here!", font=('', 26, 'bold', 'italic'),
          fg="#D84279").grid(padx=15, pady=(0, 0), columnspan=2, row=6, column=0)
    Label(main, text="Lowest:", fg="#333333").grid(row=7, column=0, padx=(100, 0))
    lowSet = Entry(main, textvariable=lowest)
    lowSet.grid(row=7, column=0, columnspan=2, pady=5)
    Label(main, text="Highest:", fg="#333333").grid(row=8, column=0, pady=(0, 10), padx=(100, 0))
    highSet = Entry(main, textvariable=highest)
    highSet.grid(row=8, column=0, columnspan=2, pady=(0, 10))
    Button(main, text="Set!", command=set).grid(row=9, columnspan=2, pady=(0, 10))
    Button(main, text="Close!", command=remove, bg="#ec5043", fg="#FDFEFE").grid(
        row=9, column=1, pady=(0, 10), padx=(0, 10), sticky=E)

    main.bind('<Return>', go)
    main.bind('<Escape>', remove)
