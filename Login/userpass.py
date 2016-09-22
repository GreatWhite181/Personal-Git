try:    #test.
    from Tkinter import *
except ImportError:
    from tkinter import *


def killTk(*args):
    root.destroy()


def Reg():
    global regFrame
    regFrame.destroy()
    regFrame = Frame()
    regFrame.grid(padx=10, pady=10)

    Frame(regFrame, height=2, bd=1, relief=SUNKEN).grid(sticky=E + W, padx=10, pady=(0, 5), columnspan=2)

    Label(regFrame, text='If you don\'t have an account, Please Register Below.',
          font=("", 17)).grid(row=1, column=0, columnspan=2, sticky=E, pady=(0, 10))

    Label(regFrame, text='Username:').grid(row=2, column=0, sticky=E)
    Label(regFrame, text='Password:').grid(row=3, column=0, sticky=E)

    Username = Entry(regFrame, textvariable=usr)
    Username.grid(row=2, column=1)
    Password = Entry(regFrame, textvariable=pss, show="*")
    Password.grid(row=3, column=1)

    for child in regFrame.winfo_children():
        child.grid_configure(padx=5, pady=5)

root = Tk()
root.attributes("-topmost", True)
root.title("User Pass")

loginFrame = Frame()
loginFrame.grid(padx=10, pady=10)

usr = StringVar()
pss = StringVar()

Label(loginFrame, text='Please Enter Your Username and Password',
      font=("", 17)).grid(row=0, column=0, columnspan=2, sticky=E)
Label(loginFrame, text='Username:').grid(row=1, column=0, sticky=E)
Label(loginFrame, text='Password:').grid(row=2, column=0, sticky=E)

Username = Entry(loginFrame, textvariable=usr)
Username.grid(row=1, column=1)
Password = Entry(loginFrame, textvariable=pss, show="*")
Password.grid(row=2, column=1)

Button(loginFrame, text='Login', command=None).grid(row=3, column=0, columnspan=2)
Button(loginFrame, text='Register', command=Reg).grid(row=3, column=0, columnspan=2, sticky=E)

regFrame = Frame()  # palce holder
regFrame.grid()

for child in loginFrame.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.bind('<Escape>', killTk)
root.mainloop()
