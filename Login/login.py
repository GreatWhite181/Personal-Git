try:
    from Tkinter import *
except ImportError:
    from tkinter import *

registered = ['Lon Sally']
registeredLower = [i.lower() for i in registered]


def login(*args):
    loginUser = usr.get()
    passUser = pss.get()
    combo = loginUser + ' ' + passUser
    if combo in registered or combo in registeredLower:
        popup = Tk()
        popup.attributes('-topmost', True)
        Label(popup, text="Yokozo").grid()
        Button(popup, text="ok", command=None).grid()
        popup.mainloop()
    else:
        Label(loginFrame, text='Incorrect Username or Password').grid(row=3, columnspan=3)


def register():
    regUser = chooseUsr.get()
    regPass = choosePss.get()
    regCombo = regUser + ' ' + regPass
    registered.append(regCombo)

def showPassword():
    global showPasswordStatus
    if showPasswordStatus == 1:
        choosePassword.config(show='')
        choosePassword.update()
        showPasswordStatus = 0
        show.config(text='hide')
        show.update()
    elif showPasswordStatus == 0:
        choosePassword.config(show='*')
        choosePassword.update()
        showPasswordStatus = 1
        show.config(text='show')
        show.update()


def killTk(*args):
    root.destroy()


def Reg():
    global regFrame, choosePassword, showPasswordStatus, show, chooseUsr, choosePss
    if regFrame is not None:
        return
    regFrame = Frame()
    regFrame.grid(padx=10, pady=(0, 10))

    chooseUsr = StringVar()
    choosePss = StringVar()

    Frame(regFrame, height=2, bd=1, relief=SUNKEN).grid(sticky=EW, padx=10, pady=(0, 5), columnspan=3)

    Label(regFrame, text='If you don\'t have an account, Please Register Below.',
          font=("", 17)).grid(row=1, column=0, columnspan=3, sticky=E, pady=(0, 10))

    Label(regFrame, text='Choose Username:').grid(row=2, column=0, sticky=E)
    Label(regFrame, text='Choose Password:').grid(row=3, column=0, sticky=E)

    chooseUsername = Entry(regFrame, textvariable=chooseUsr)
    chooseUsername.grid(row=2, column=1)
    choosePassword = Entry(regFrame, textvariable=choosePss, show='*')
    choosePassword.grid(row=3, column=1)

    showPasswordStatus = 1
    show = Button(regFrame, text='Show', command=showPassword, width=7)
    show.grid(row=3, column=2, columnspan=2, sticky=W)

    Button(regFrame, text='Submit', command=register, width=10).grid(row=4, column=0, columnspan=3)

    for child in regFrame.winfo_children():
        child.grid_configure(padx=5, pady=5)

root = Tk()
root.attributes("-topmost", True)
root.title("User Pass")

loginFrame = Frame()
loginFrame.grid(padx=45, pady=10)

usr = StringVar()
pss = StringVar()
regFrame = None

Label(loginFrame, text='Please Enter Your Username and Password',
      font=("", 17)).grid(row=0, column=0, columnspan=3)
Label(loginFrame, text='Username:').grid(row=1, column=0, sticky=E)
Label(loginFrame, text='Password:').grid(row=2, column=0, sticky=E)

username = Entry(loginFrame, textvariable=usr)
username.grid(row=1, column=1)
password = Entry(loginFrame, textvariable=pss, show="*")
password.grid(row=2, column=1)

Button(loginFrame, text='Login', command=login, width=10).grid(row=4, column=0, columnspan=3)
Button(loginFrame, text='Register', command=Reg).grid(row=4, column=2, columnspan=1)

for child in loginFrame.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.bind('<Return>', login)
root.bind('<Escape>', killTk)
root.mainloop()
