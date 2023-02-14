from tkinter import *
from ttkthemes import ThemedTk

import matplotlib.pyplot as plt

from shared import *
from style import *
from dataParser import *

# function to call when the window gets closed
def closeWindowCallback(event):
    if getFileDir() != "":
        newDays = []
            
        for line in getWidgets()["days"].get_children():
            newDays.append({})
            for i in range(len(getWidgets()["days"].item(line)['values'])):
                if i == 0:
                    newDays[len(newDays) - 1]["date"] = getWidgets()["days"].item(line)['values'][i]
                elif i == 1:
                    newDays[len(newDays) - 1]["time"] = getWidgets()["days"].item(line)['values'][i]
                elif i == 2:
                    newDays[len(newDays) - 1]["distance"] = getWidgets()["days"].item(line)['values'][i]
                elif i == 3:
                    newDays[len(newDays) - 1]["weight"] = getWidgets()["days"].item(line)['values'][i]
                    
        setDays(newDays)
        writeTXT(getFileDir(), getDays())
    
    getWindow().destroy()
def closeWindowWM():
    if getFileDir() != "":
        newDays = []
            
        for line in getWidgets()["days"].get_children():
            newDays.append({})
            for i in range(len(getWidgets()["days"].item(line)['values'])):
                if i == 0:
                    newDays[len(newDays) - 1]["date"] = getWidgets()["days"].item(line)['values'][i]
                elif i == 1:
                    newDays[len(newDays) - 1]["time"] = getWidgets()["days"].item(line)['values'][i]
                elif i == 2:
                    newDays[len(newDays) - 1]["distance"] = getWidgets()["days"].item(line)['values'][i]
                elif i == 3:
                    newDays[len(newDays) - 1]["weight"] = getWidgets()["days"].item(line)['values'][i]
                    
        setDays(newDays)
        writeTXT(getFileDir(), getDays())
        
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

def closeProgressWindowCallback(event):
    plt.close("all")
    getProgressWindow().destroy()
    setProgressWindow(None)
def closeProgressWindowWM():
    plt.close("all")
    getProgressWindow().destroy()
    setProgressWindow(None)

# function to create a window
def createWindow(title = "GUI App", width = 1280, height = 720, offsetX = 0, offsetY = 0, resizeX = TRUE, resizeY = TRUE, minResizeX = 400, minResizeY = 400, maxResizeX = 1920, maxResizeY = 1080, alpha = 1, icon = ""):
    window = getWindow()

    window = ThemedTk()                     # create the window
    window.geometry(str(width) + "x" + str(height) + "+" + str(offsetX) + "+" + str(offsetY)) # "1280x720+offsetx+offsety"
    window.title("Fitness Diary")                    # set the window name
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


def createProgressWindow(title = "GUI App", width = 1280, height = 720, offsetX = 0, offsetY = 0, resizeX = TRUE, resizeY = TRUE, minResizeX = 400, minResizeY = 400, maxResizeX = 1920, maxResizeY = 1080, alpha = 1, icon = ""):
    progressWindow = getProgressWindow()

    progressWindow = Toplevel()                     # create the window
    progressWindow.geometry(str(width) + "x" + str(height) + "+" + str(offsetX) + "+" + str(offsetY)) # "1280x720+offsetx+offsety"
    progressWindow.title(title)                    # set the window name
    progressWindow.resizable(resizeX, resizeY)     # resizable width and height
    progressWindow.minsize(minResizeX, minResizeY) # min resize dimensions
    progressWindow.maxsize(maxResizeX, maxResizeY) # max resize dimensions
    progressWindow.attributes('-alpha', alpha)     # opacity
    #window.attributes('-topmost', 1)      # window always on top
    if icon != "":
        progressWindow.iconphoto(False, PhotoImage(file = icon)) # load the icon
        
    progressWindow.bind('<Escape>', closeProgressWindowCallback)   # bind the escape button to close the program
    progressWindow.protocol("WM_DELETE_WINDOW", closeProgressWindowWM)

    setProgressWindow(progressWindow)

    return(progressWindow)


