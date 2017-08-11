import subprocess
import Database
from sys import platform

open("text files/loginStatus.txt", 'a')

if platform == 'darwin':
    osCommand = "python "
else:
    osCommand = ""
subprocess.call(osCommand + "login.py", shell=True)
if "1" in open('text files/loginStatus.txt').read():
    subprocess.call(osCommand + "GuessingGame.py", shell=True)
Database.loginStatus("0", "")
