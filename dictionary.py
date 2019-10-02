#import uuid module to generate Universally Unique IDentifier
import uuid
#import hashlib module which implements a common interface to many different secure hash and message digest algorithms
import hashlib
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import Qt
import random

#creating window to give feedback to user
#creating app
AppmessageBox = QApplication([])
#creating window
windowmessageBox = QMessageBox()
#setting the window to appear on top
windowmessageBox.setWindowFlags(Qt.WindowStaysOnTopHint)

messageBoxFirst = True;

def showMesaageBox(title,message,additional,icon):
    #setting icon
    if icon =="warning":
        windowmessageBox.setIcon(QMessageBox.Warning)
    elif icon =="info":
        windowmessageBox.setIcon(QMessageBox.Information)
    #setting title
    windowmessageBox.setWindowTitle(title)
    #setting message
    windowmessageBox.setText(message)
    #detailed message
    windowmessageBox.setInformativeText(additional)
    #adding OK and Cancel buttons
    windowmessageBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    #show the window
    windowmessageBox.show()
    #execute the app
    global messageBoxFirst
    if messageBoxFirst:
        AppmessageBox.exec_()
        messageBoxFirst = False

    
def banner():
    print("                             ___       ______ .______        ______   .__   __. ____    ____ .___  ___.      _______.  ") 
    print("                            /   \     /      ||   _  \      /  __  \  |  \ |  | \   \  /   / |   \/   |     /       |  ") 
    print("                           /  ^  \   |  ,----'|  |_)  |    |  |  |  | |   \|  |  \   \/   /  |  \  /  |    |   (----`  ") 
    print("                          /  /_\  \  |  |     |      /     |  |  |  | |  . `  |   \_    _/   |  |\/|  |     \   \       ")
    print("                         /  _____  \ |  `----.|  |\  \----.|  `--'  | |  |\   |     |  |     |  |  |  | .----)   |     ") 
    print("                        /__/     \__\ \______|| _| `._____| \______/  |__| \__|     |__|     |__|  |__| |_______/       ")
    print("                                                                                                                       ") 
    print("                                                 _______   ______   .______         ____    ____  ______    __    __   ") 
    print("                                                |   ____| /  __  \  |   _  \        \   \  /   / /  __  \  |  |  |  |  ") 
    print("                                                |  |__   |  |  |  | |  |_)  |        \   \/   / |  |  |  | |  |  |  |  ") 
    print("                                                |   __|  |  |  |  | |      /          \_    _/  |  |  |  | |  |  |  |   ")
    print("                                                |  |     |  `--'  | |  |\  \----.       |  |    |  `--'  | |  `--'  |   ")
    print("                                                |__|      \______/  | _| `._____|       |__|     \______/   \______/    ")                                                                                                

    
#function to hash passwords
def hashPassword(password):
    # Generate a random UUID as salt of a 32-character hexadecimal string
    salt = uuid.uuid4().hex
    #return a sha512 hash encoding the slat and password and adding the salt at the end to use it later in comparing hashs 
    return hashlib.sha512(salt.encode() + password.encode()).hexdigest() + ':' + salt

#function to check equl hashes
def checkPassword(hashedPassword, userPassword):
    #getting the hashed password and salt by spliting the hashed password
    password, salt = hashedPassword.split(':')
    #comparing the hashed password and the hash of the new password using the same salt
    #if equal return True else return False
    return password == hashlib.sha512(salt.encode() + userPassword.encode()).hexdigest()

#function to verify existance of a user in accounts
def verifExistAccount(user):
    try:
        #open the accounts file ,a+ to create unexistant file
        accountsFile = open("accounts.txt",'r')
        #return strings of username , password as line in a list 
        data = accountsFile.readlines()
        #close the file
        accountsFile.close()
        #verify existance line by line from list
        for line in data:
            #split the line to get list of username in index 0 and password in index 1
            userPass = line.split()
            #comparing usernames
            if user == userPass[0]:
                #if equal return True  
                return True
        #after comparing all usernames without equality return False    
        else :
            return False
    except :
        #create file if doesn't exist 
        dictFile = open("accounts.txt",'w')
        dictFile.close()
        showMesaageBox("general Exception","general exception","Something went wrong!","warning")
    
def signup(username, password, passwordConfirm):
    try:
        #input the username, password and confrim password
        #username = input('Pick a username : ')
        #password = input('Pick a password : ')
        #passwordConfirm = input('Please confirm your password : ')
        #if all inputs are valid and not empty
        assert username != "" and password !="" and passwordConfirm !=""
        #password and comfirm must be the same
        if password == passwordConfirm :
            #add user if username is not used before
            if not verifExistAccount(username):
                #open file as append
                accountsFile = open("accounts.txt",'a')
                #write username in file
                accountsFile.write(username)
                #space between username and password
                accountsFile.write(" ")
                #write hashed password
                accountsFile.write(hashPassword(password))
                #return for the future users infos
                accountsFile.write("\n")
                #close file
                accountsFile.close()
                print("your account has been setup.")
                showMesaageBox("account created","Acount setup","your account has been setup.","info")
            else :
                print("Existant account")
                showMesaageBox("account Error","invalid input","Existant account","info")
        #if password and confirm doesn't match
        else:
            print("your password don't match. please try again")
            showMesaageBox("match Error","invalid input","your password don't match. please try again","warning")
    except AssertionError : 
        print("invalid input : you can't input an empty String")
        showMesaageBox("Assertion Error","invalid input","you can't input an empty String","warning")
    #keyboardInterrupt exception handling   
    except KeyboardInterrupt:
        print("you can't exit")
        showMesaageBox("KeyboardInterrupt Exception","you can't exit","you have to input something","warning")
    #any other exception handling   
    except :
        print("Something went wrong!")
        dictFile = open("accounts.txt",'w')
        dictFile.close()
        showMesaageBox("general Exception","general exception","Something went wrong!","warning")
    
def signin(username,password):
    try:
        #input the username, password 
        #username = input('please enter your username : ')
        #password = input('Please enter your password : ')
        #if all inputs are valid and not empty
        assert username != "" and password !="" 
        #open file as read
        accountsFile = open("accounts.txt",'r')
        #return strings of username , password as line in a list 
        data = accountsFile.readlines()
        #print(data)
        #verify existance line by line from list
        for line in data:
            #split the line to get list of username in index 0 and password in index 1
            userPass = line.split()
            #print(userPass)
            #if username exist and has the same password as registred account
            if username in userPass and checkPassword(userPass[1],password):
                #grant access and return True
                print('access granted')
                return True
        #if username unexistant or unexistant password return false    
        else:
            showMesaageBox("account Error","invalid input","Inexistant account","info")
            return False
        
    except AssertionError : 
        print("invalid input : you can't input an empty String","warning")
        showMesaageBox("Asseryion Error","invalid input","you can't input an empty String","warning")
    #keyboardInterrupt exception handling   
    except KeyboardInterrupt:
        print("you can't exit")
        showMesaageBox("KeyboardInterrupt Exception","you can't exit","you have to input something","warning")
    #any other exception handling   
    except :
        print("Something went wrong!")
        dictFile = open("accounts.txt",'w')
        dictFile.close()
        showMesaageBox("general Exception","general exception","Something went wrong!","warning")           
            
#function to verify existant keys in the dictionary
def verifExistDict(key):
    try : 
        #open the dictionary
        assert key != ""
        dictFile = open("dictionary.txt",'r')
        #return strings of key value as line in a list   
        data = dictFile.readlines()
        #close file
        dictFile.close()
        #verify existance line by line from list
        for line in data:
            #split the line to get list of key in index 0 and value in index 1
            userPass = line.split("#%$@!!@")
            #comparing keys
            if key.lower() == userPass[0].lower():
                #if equal return True    
                return True
        else :
            #after comparing all keys without equality return False
            return False
    except AssertionError:
        print("invalid input : you can't input an empty String")
        showMesaageBox("Asseryion Error","invalid input","you can't input an empty String","warning")
    except :
        #create file if doesn't exist 
        dictFile = open("dictionary.txt",'a+')
        dictFile.close()
        showMesaageBox("general Exception","general exception","Something went wrong!","warning")

#function to write in the dictionary as a file
def writeInDictionary(key,value):
    #try except block to deal with exceptions
    try:
        #making user input the key and value
        #key = input('Pick a key : ')
        #value = input('Pick a value : ')
        #assert if the user inputs some empty values
        assert key != "" and value !="" 
        #verify if exist to ignore redundant
        if not verifExistDict(key):
            #if not existant key open the dictionary file
            dictFile = open("dictionary.txt",'a')
            #write key in file
            dictFile.write(key.upper())
            #space between key and value
            dictFile.write("#%$@!!@")
            #write value
            dictFile.write(value.title())
            #return for the future keys and values
            dictFile.write("\n")
            #close file
            dictFile.close()
        else:
            #if existant inform the user
            print("existant key")
            showMesaageBox("account Error","invalid input","Existant key","info")
    #except the key != "" or value !=""  assertion        
    except AssertionError:
        print("invalid input : you can't input an empty String")
        showMesaageBox("Asseryion Error","invalid input","you can't input an empty String","warning")
    #keyboardInterrupt exception handling   
    except KeyboardInterrupt:
        print("you can't exit")
        showMesaageBox("KeyboardInterrupt Exception","you can't exit","you have to input something","warning")
    #any other exception handling   
    except :
        print("Something went wrong!")
        dictFile = open("dictionary.txt",'a+')
        dictFile.close()
        showMesaageBox("general Exception","general exception","Something went wrong!","warning")

def readDictionaryAsList():
    try:
        #declare an emnpty list
        acronymDict= []
        #open the file as read
        dictFile = open("dictionary.txt",'r')
        #return strings of key value as line in a list  
        data = dictFile.readlines()
        #close file
        dictFile.close()
        #get data line by line from list
        for line in data:
            #split the line to get list of key in index 0 and value in index 1
            items = line.split("#%$@!!@")
            #append to the list
            acronymDict.append(items)

        #print(acronymDict)
        #returning the list
        return sorted(acronymDict)
    except :
        #create file if doesn't exist 
        dictFile = open("dictionary.txt",'a+')
        dictFile.close()
        showMesaageBox("general Exception","general exception","Something went wrong!","warning")
                       
def readDictionary():
    try:
        #declare an emnpty dict
        acronymDict= {}
        #open the file as read
        dictFile = open("dictionary.txt",'r')
        #return strings of key value as line in a list
        data = dictFile.readlines()
        #close file
        dictFile.close()
        #get data line by line from list
        for line in data:
            #split the line to get list of key in index 0 and value in index 1
            items = line.split("#%$@!!@")
            #append to the list
            acronymDict[items[0]] = items[1]

        #print(acronymDict)
        return acronymDict
    except :
        #create file if doesn't exist 
        dictFile = open("dictionary.txt",'a+')
        dictFile.close()
        showMesaageBox("general Exception","general exception","Something went wrong!","warning")    

def searchInDict(key):
    try : 
        #open the dictionary
        assert key != ""
        dictFile = open("dictionary.txt",'r')
        #return strings of key value as line in a list   
        data = dictFile.readlines()
        #close file
        #print(data)
        dictFile.close()
        #verify existance line by line from list
        for line in data:
            #split the line to get list of key in index 0 and value in index 1
            items = line.split("#%$@!!@")
            #print(userPass)
            #comparing keys
            if key.lower() == items[0].lower():
                #if equal return True
                return str(items[1])
        else :
            #after comparing all keys without equality return False
            return "Sorry, we don't have this Acronym in our Dictionay. You can add it if you want!"
    except AssertionError:
        print("invalid input : you can't input an empty String")
        showMesaageBox("Asseryion Error","invalid input","you can't input an empty String","warning")
    except :
        #create file if doesn't exist 
        dictFile = open("dictionary.txt",'a+')
        dictFile.close()
        showMesaageBox("general Exception","general exception","Something went wrong!","warning")

def shufflefromDict():
    values = random.choice(readDictionaryAsList())
    return values[0],values[1]
#main

#banner()
#signup()
#signin()
#while True:
#    if signin():
#        writeInDictionary()
#        readDictionary()
#    else:
#        print("inexistant account ! try again...")
#readDictionaryAsList()
#writeInDictionary()
