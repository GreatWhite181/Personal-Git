try:
    from Tkinter import *
except ImportError:
    from tkinter import *
import Database

open("text files/Users.txt", 'a')

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!defs
def login(*args):
    loginUser = username.get()
    passUser = password.get()
    if loginUser+':'+passUser+'\n' in open('text files/Users.txt').read():
        Database.loginStatus("1", loginUser)
        killTk()
    else:
        Database.loginStatus("0", "")
        Bad = Label(loginFrame, text='Incorrect Username or Password')
        Bad.grid(row=3, columnspan=3, padx=(30,0))
        Bad.after(3000, lambda: Bad.grid_remove())

def showPassword():
    global showPasswordStatus
    if showPasswordStatus == 1:
        choosePassword.config(show='')
        choosePassword.update()
        showPasswordStatus = 0
        show.config(text='Hide')
        show.update()
    elif showPasswordStatus == 0:
        choosePassword.config(show='*')
        choosePassword.update()
        showPasswordStatus = 1
        show.config(text='Show')
        show.update()

def clearRegMenu():
    if success == 1:
        regFrame.grid_forget()
        SignStatus.grid_remove()
        choosePassword.delete(0,END)
        chooseUsername.delete(0,END)
        username.focus_set()
    else:
        SignStatus.grid_remove()
        submitButton.grid()

def register():
    global SignStatus, success
    regUser = chooseUsername.get()
    regPass = choosePassword.get()
    submitButton.grid_remove()
    if regUser+':'+regPass+'\n' not in open('text files/Users.txt').read():
        SignStatus = Label(regFrame, text="Sign Up Successful.")
        Database.userNew(regUser, regPass)
        success = 1
    else:
        SignStatus = Label(regFrame, text="Already Used.")
        success = 0
    SignStatus.grid(row=5, columnspan=4, padx=(35,0), pady=(5, 15))
    regFrame.after(3000, clearRegMenu)

def regMenu():
    submitButton.grid()
    regFrame.grid()

def killTk(*args):
    root.destroy()


root = Tk()
root.attributes("-topmost", True)
root.title("Login")

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!frames

'################################ Login Frame'
loginFrame = Frame()

Label(loginFrame, text='Please Enter Your Username and Password',
      font=("", 12)).grid(row=0, column=0, columnspan=3, padx=40, pady=(10, 15))
Label(loginFrame, text='Username:').grid(row=1, column=0, sticky=E, pady=5, padx=(40, 0))
Label(loginFrame, text='Password:').grid(row=2, column=0, sticky=E, pady=5, padx=(40, 0))

username = Entry(loginFrame)
username.grid(row=1, column=1, pady=5)
password = Entry(loginFrame, show="*")
password.grid(row=2, column=1, pady=5)

Button(loginFrame, text='Login', command=login, width=10).grid(row=4, column=0, columnspan=3, padx=(40,5), pady=(10, 10))
Button(loginFrame, text='Register', command=regMenu).grid(row=4, column=2, sticky=E, columnspan=1, padx=(5, 10), pady=5)

'################################ Register Frame'
regFrame = Frame()

Frame(regFrame, height=2, bd=1, relief=SUNKEN).grid(sticky=EW, padx=10, pady=(5,10), columnspan=3)

Label(regFrame, text='If you don\'t have an account, Please Register Below.',
      font=("", 12)).grid(row=1, column=0, columnspan=3, padx=5, pady=(5, 15))
Label(regFrame, text='Choose Username:').grid(row=2, column=0, pady=5, sticky=E)
Label(regFrame, text='Choose Password:').grid(row=3, column=0, pady=5, sticky=E)

chooseUsername = Entry(regFrame)
chooseUsername.grid(row=2, column=1, pady=5)
choosePassword = Entry(regFrame, show='*')
choosePassword.grid(row=3, column=1, pady=5)

showPasswordStatus = 1
show = Button(regFrame, text='Show', command=showPassword, width=7)
show.grid(row=3, column=2, columnspan=2, sticky=W)

submitButton = Button(regFrame, text='Submit', command=register, width=10)
submitButton.grid(row=5, column=0, columnspan=3, padx=(40,5), pady=(5, 10))

Label(regFrame, text=' ').grid(row=5, column=2, sticky=E, padx=30, pady=5,)

#!!!!!!!!!!!!!!!!!!!!callingFrames
loginFrame.grid()

root.bind('<Return>', login)
root.bind('<Escape>', killTk)
root.mainloop()
