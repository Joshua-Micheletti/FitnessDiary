window = None
addWindow = None
modifyWindow = None

strings = dict()
widgets = dict()


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
    
