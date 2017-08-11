def userNew(regUser, regPass):
    userFile = open("text files/Users.txt", 'a')
    userFile.write (regUser+':'+regPass+'\n')
    userFile.close()

def loginStatus(x, user):
    loginStatus = open("text files/loginStatus.txt", 'w')
    loginStatus.write (x)
    if x == '1':
        loginStatus.write ('\n' + user)
    loginStatus.close()
