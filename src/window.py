from tkinter import *
from ttkthemes import ThemedTk

from shared import *
from style import *

# function to call when the window gets closed
def closeWindowCallback(event):
    getWindow().destroy()
def closeWindowWM():
    getWindow().destroy()
    
def closeAddWindowCallback(event):
    getAddWindow().destroy()
    setAddWindow(None)
def closeAddWindowWM():
    getAddWindow().destroy()
    setAddWindow(None)
    
def closeModifyWindowCallback(event):
    getModifyWindow().destroy()
    setModifyWindow(None)
def closeModifyWindowWM():
    getModifyWindow().destroy()
    setModifyWindow(None)

# function to create a window
def createWindow(title = "GUI App", width = 1280, height = 720, offsetX = 0, offsetY = 0, resizeX = TRUE, resizeY = TRUE, minResizeX = 400, minResizeY = 400, maxResizeX = 1920, maxResizeY = 1080, alpha = 1, icon = ""):
    window = getWindow()

    window = ThemedTk()                     # create the window
    window.geometry(str(width) + "x" + str(height) + "+" + str(offsetX) + "+" + str(offsetY)) # "1280x720+offsetx+offsety"
    window.title(title)                    # set the window name
    window.resizable(resizeX, resizeY)     # resizable width and height
    window.minsize(minResizeX, minResizeY) # min resize dimensions
    window.maxsize(maxResizeX, maxResizeY) # max resize dimensions
    window.attributes('-alpha', alpha)     # opacity
    #window.attributes('-topmost', 1)      # window always on top
    if icon != "":
        window.iconphoto(False, PhotoImage(file = icon)) # load the icon
        
    window.bind('<Escape>', closeWindowCallback)   # bind the escape button to close the program
    window.protocol("WM_DELETE_WINDOW", closeWindowWM)
    
    loadStyle(window)
    setWindow(window)

    return(window)


def createAddWindow(title = "GUI App", width = 1280, height = 720, offsetX = 0, offsetY = 0, resizeX = TRUE, resizeY = TRUE, minResizeX = 400, minResizeY = 400, maxResizeX = 1920, maxResizeY = 1080, alpha = 1, icon = ""):
    addWindow = getAddWindow()

    addWindow = Toplevel()                     # create the window
    addWindow.geometry(str(width) + "x" + str(height) + "+" + str(offsetX) + "+" + str(offsetY)) # "1280x720+offsetx+offsety"
    addWindow.title(title)                    # set the window name
    addWindow.resizable(resizeX, resizeY)     # resizable width and height
    addWindow.minsize(minResizeX, minResizeY) # min resize dimensions
    addWindow.maxsize(maxResizeX, maxResizeY) # max resize dimensions
    addWindow.attributes('-alpha', alpha)     # opacity
    #window.attributes('-topmost', 1)      # window always on top
    if icon != "":
        addWindow.iconphoto(False, PhotoImage(file = icon)) # load the icon
        
    addWindow.bind('<Escape>', closeAddWindowCallback)   # bind the escape button to close the program
    addWindow.protocol("WM_DELETE_WINDOW", closeAddWindowWM)

    setAddWindow(addWindow)

    return(addWindow)


def createModifyWindow(title = "GUI App", width = 1280, height = 720, offsetX = 0, offsetY = 0, resizeX = TRUE, resizeY = TRUE, minResizeX = 400, minResizeY = 400, maxResizeX = 1920, maxResizeY = 1080, alpha = 1, icon = ""):
    modifyWindow = getModifyWindow()

    modifyWindow = Toplevel()                     # create the window
    modifyWindow.geometry(str(width) + "x" + str(height) + "+" + str(offsetX) + "+" + str(offsetY)) # "1280x720+offsetx+offsety"
    modifyWindow.title(title)                    # set the window name
    modifyWindow.resizable(resizeX, resizeY)     # resizable width and height
    modifyWindow.minsize(minResizeX, minResizeY) # min resize dimensions
    modifyWindow.maxsize(maxResizeX, maxResizeY) # max resize dimensions
    modifyWindow.attributes('-alpha', alpha)     # opacity
    #window.attributes('-topmost', 1)      # window always on top
    if icon != "":
        modifyWindow.iconphoto(False, PhotoImage(file = icon)) # load the icon
        
    modifyWindow.bind('<Escape>', closeModifyWindowCallback)   # bind the escape button to close the program
    modifyWindow.protocol("WM_DELETE_WINDOW", closeModifyWindowWM)

    setModifyWindow(modifyWindow)

    return(modifyWindow)


