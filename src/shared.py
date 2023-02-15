window = None
addWindow = None
modifyWindow = None
progressWindow = None

theme = ""

strings = dict()
widgets = dict()

fileDir = ""
days = []


def getWindow():
    global window
    return(window)

def setWindow(newWindow):
    global window
    window = newWindow
    
    
def getAddWindow():
    global addWindow
    return(addWindow)

def setAddWindow(newWindow):
    global addWindow
    addWindow = newWindow
    

def getModifyWindow():
    global modifyWindow
    return(modifyWindow)

def setModifyWindow(newWindow):
    global modifyWindow
    modifyWindow = newWindow
    
    
def getProgressWindow():
    global progressWindow
    return(progressWindow)

def setProgressWindow(newWindow):
    global progressWindow
    progressWindow = newWindow
    

def getStrings():
    global strings
    return(strings)

def setStrings(newStrings):
    global strings
    strings = newStrings
    

def getWidgets():
    global widgets
    return(widgets)

def setWidgets(newWidgets):
    global widgets
    widgets = newWidgets
    
    
def getFileDir():
    global fileDir
    return(fileDir)

def setFileDir(newFileDir):
    global fileDir
    fileDir = newFileDir
    
    
def getDays():
    global days
    return(days)

def setDays(newDays):
    global days
    days = newDays
    
    
def getTheme():
    global theme
    return(theme)

def setTheme(newTheme):
    global theme
    theme = newTheme

