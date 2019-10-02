from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPlainTextEdit, QFormLayout, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QTableWidget,QTableWidgetItem
import dictionary
from platform import system

#creating table in window
def createTable(tableWidget):
    dic = dictionary.readDictionaryAsList()
    [[tableWidget.setItem(i,j,QTableWidgetItem()) for j in range(2)] for i in range(len(dic))]

#creating widgets
#main app dictionary    
appDict = QApplication([])
#creating window
windowDict = QWidget()
#setting title
windowDict.setWindowTitle('Dictionary for you')
#setting icon
if system() == "Windows" :
    windowDict.setWindowIcon(QIcon('dictionary.png'))
#setting size
windowDict.resize(600,400)

#signup window  
appSignUp = QApplication([])
#creating window 
windowSignUp = QWidget()
#setting title 
windowSignUp.setWindowTitle('Signup : Dictionary for you')
#setting icon 
if system() == "Windows" :
    windowSignUp.setWindowIcon(QIcon('dictionary.png'))

#signin window
appSignin = QApplication([])
#creating window 
windowSignin = QWidget()
#setting title 
windowSignin.setWindowTitle('Signin : Dictionary for you')
#setting icon 
if system() == "Windows" :
    windowSignin.setWindowIcon(QIcon('dictionary.png'))

def addToDict():
    #print(keyEdit.text())
    #print(valueEdit.text())
    dictionary.writeInDictionary(keyEdit.text(),valueEdit.text())
    dic = dictionary.readDictionaryAsList()
    tableWidget.setRowCount(len(dic))
    tableWidget.setColumnCount(2)
    [[tableWidget.setItem(i,j,QTableWidgetItem(dic[i][j])) for j in range(2)] for i in range(len(dic))]
    keyEdit.clear()
    valueEdit.clear()
    
def searchInDict():
    #print(searchkeyEdit.text())
    if(not dictionary.verifExistDict(searchkeyEdit.text())):
        resultBox.clear()
        resultBox.insertPlainText("Sorry, we don't have this Acronym in our Dictionay. You can add it if you want!")
        #print("inexistant")
    else :
        value = dictionary.searchInDict(searchkeyEdit.text())
        #print(value)
        resultBox.clear()
        resultBox.insertPlainText(searchkeyEdit.text().upper()+' : '+value)
    searchkeyEdit.clear()

def shuffle():
    key,value = dictionary.shufflefromDict()
    #print(value)
    resultBox.clear()
    resultBox.insertPlainText(key+' : '+value)

def dictionaryApp():
    windowSignin.hide()
    windowSignUp.hide()
    #outer layout
    layout = QVBoxLayout()
    #within layout
    layoutAdd = QHBoxLayout()
    #within layout
    layoutSearch = QHBoxLayout()
    motherlayoutSearch = QVBoxLayout()
    #within layout
    layoutTableSearch = QHBoxLayout()

    #labels
    searchLabel = QLabel('search for acronyms : ')
    addLabel = QLabel('add acronyms : ')

    #add form
    addFormLayout = QFormLayout()
    keyLabel = QLabel("Key : ")
    global keyEdit
    keyEdit = QLineEdit()
    valueLabel = QLabel("Value : ")
    global valueEdit
    valueEdit = QLineEdit()
    addButton = QPushButton("Add Acronym")
    addButton.clicked.connect(addToDict)
    addFormLayout.addRow(keyLabel,keyEdit)
    addFormLayout.addRow(valueLabel,valueEdit)

    layoutAdd.addLayout(addFormLayout)
    layoutAdd.addWidget(addButton)

    #search form
    searchFormLayout = QFormLayout()
    searchkeyLabel = QLabel("Key : ")
    global searchkeyEdit
    searchkeyEdit = QLineEdit()
    searchButton = QPushButton("Search Acronym")
    searchButton.clicked.connect(searchInDict)
    searchFormLayout.addRow(searchkeyLabel,searchkeyEdit)
    global resultBox
    resultBox = QPlainTextEdit()
    resultBox.insertPlainText("result will appear here.\n")
    resultBox.setDisabled(True)
    
    layoutSearch.addLayout(searchFormLayout)
    layoutSearch.addWidget(searchButton)

    #search layout
    motherlayoutSearch.addWidget(searchLabel)
    motherlayoutSearch.addLayout(layoutSearch)
    motherlayoutSearch.addWidget(resultBox)
    motherlayoutSearch.addStretch()
    #table
    global tableWidget
    tableWidget = QTableWidget()
    dic = dictionary.readDictionaryAsList()
    tableWidget.setRowCount(len(dic))
    tableWidget.setColumnCount(2)
    tableWidget.setColumnWidth(0,130)
    tableWidget.setColumnWidth(1,500)
    tableWidget.setHorizontalHeaderLabels(["Key", "Value"])
    [[tableWidget.setItem(i,j,QTableWidgetItem(dic[i][j])) for j in range(2)] for i in range(len(dic))]

    #tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
    #tableWidget.move(0,0)

    #setting inner layout
    #layoutTableSearch.addStretch()
    layoutTableSearch.addLayout(motherlayoutSearch)
    layoutTableSearch.addSpacing(15)
    layoutTableSearch.addWidget(tableWidget)
    #layoutTableSearch.addStretch()

    #add outer layout
    layout.addWidget(addLabel)
    layout.addLayout(layoutAdd)
    shufflelayout = QHBoxLayout()
    shuffleButton = QPushButton("shuffle")
    shuffleButton.clicked.connect(shuffle)
    shufflelayout.addStretch()
    shufflelayout.addWidget(shuffleButton)
    shufflelayout.addStretch()
    layout.addSpacing(5)
    layout.addLayout(shufflelayout)
    layout.addSpacing(5)
    layout.addLayout(layoutTableSearch)
    #set layout to window
    windowDict.setLayout(layout)

    windowDict.show()
    appDict.exec_()
    

def closesignup():
    #print("close")
    windowSignin.show()
    windowSignUp.hide()

def submitsignup():
    #print(signupusernameEdit.text())
    #print(signuppasswordEdit.text())
    #print(signuppasswordConfirmEdit.text())
    dictionary.signup(signupusernameEdit.text(),signuppasswordEdit.text(),signuppasswordConfirmEdit.text())
    #windowSignin.show()
    #windowSignUp.hide()
    signupusernameEdit.clear()
    signuppasswordEdit.clear()
    signuppasswordConfirmEdit.clear()
    
def signUp():
    formLayout = QFormLayout()

    usernameLabel = QLabel("UserName")
    global signupusernameEdit
    signupusernameEdit = QLineEdit()
    
    formLayout.addRow(usernameLabel,signupusernameEdit)

    passwordLabel = QLabel("Password")
    global signuppasswordEdit
    signuppasswordEdit = QLineEdit()
    signuppasswordEdit.setEchoMode(QLineEdit.Password)
    formLayout.addRow(passwordLabel,signuppasswordEdit)

    passwordConfirmLabel = QLabel("Confirm Password")
    global signuppasswordConfirmEdit
    signuppasswordConfirmEdit = QLineEdit()
    signuppasswordConfirmEdit.setEchoMode(QLineEdit.Password)
    formLayout.addRow(passwordConfirmLabel,signuppasswordConfirmEdit)

    submitButton = QPushButton("Submit")
    submitButton.clicked.connect(submitsignup)
    
    cancelButton = QPushButton("SignIn")
    cancelButton.clicked.connect(closesignup)

    formLayout.addRow(submitButton,cancelButton)

    windowSignUp.setLayout(formLayout)

    windowSignUp.show()
    appSignUp.exec_()

signupFirst = True;

def closesignIn():
    #print("close")
    global signupFirst
    if signupFirst:
        #print("entered")
        signUp()
        signupFirst = False
    else:
        windowSignUp.show()
    windowSignin.hide()

def submitsignIn():
    #print(signInusernameEdit.text())
    #print(signInpasswordEdit.text())
    sign = dictionary.signin(str(signInusernameEdit.text()),str(signInpasswordEdit.text()))
    #print(sign)
    if sign == True :
        dictionaryApp()
    signInusernameEdit.clear()
    signInpasswordEdit.clear()
        
def signIn():

    formLayout = QFormLayout()

    usernameLabel = QLabel("UserName")
    global signInusernameEdit
    signInusernameEdit = QLineEdit()
    formLayout.addRow(usernameLabel,signInusernameEdit)

    passwordLabel = QLabel("Password")
    global signInpasswordEdit
    signInpasswordEdit = QLineEdit()
    signInpasswordEdit.setEchoMode(QLineEdit.Password)
    formLayout.addRow(passwordLabel,signInpasswordEdit)

    submitButton = QPushButton("Submit")
    submitButton.clicked.connect(submitsignIn)

    cancelButton = QPushButton("SignUp")
    cancelButton.clicked.connect(closesignIn)

    formLayout.addRow(submitButton,cancelButton)

    windowSignin.setLayout(formLayout)

    windowSignin.show()
    appSignin.exec_()


#main
dictionary.banner()
signIn()
