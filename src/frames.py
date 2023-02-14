from app import *
from widgets import *
from tkinter.ttk import *
from shared import *

def loadFrames(window):
    frames = dict()

    getWindow().columnconfigure(0, weight = 1)
    getWindow().rowconfigure(0, weight = 12)
    getWindow().rowconfigure(1, weight = 0)

    daysF = Frame(getWindow())
    daysF["padding"] = (20, 20)
    daysF["relief"] = "flat"
    daysF.grid(column = 0, row = 0, sticky = "nsew")
    
    frames["daysF"] = daysF
    
    buttonsF = Frame(getWindow())
    buttonsF["padding"] = (20, 20)
    buttonsF["relief"] = "flat"
    buttonsF.columnconfigure(0, weight = 1)
    buttonsF.columnconfigure(1, weight = 5)
    buttonsF.columnconfigure(2, weight = 1)
    buttonsF.columnconfigure(3, weight = 5)
    buttonsF.columnconfigure(4, weight = 1)
    buttonsF.grid(column = 0, row = 1, sticky = "nsew")  
    
    frames["buttonsF"] = buttonsF

    return(frames)


def loadAddFrames(window):
    frames = dict()
    
    getAddWindow().columnconfigure(0, weight = 1)
    getAddWindow().rowconfigure(0, weight = 1)
    
    addFrame = Frame(getAddWindow())
    addFrame["padding"] = (20, 20)
    addFrame["relief"] = "flat"
    addFrame.columnconfigure(0, weight = 1)
    addFrame.columnconfigure(1, weight = 5)
    addFrame.rowconfigure(0, weight = 1)
    addFrame.rowconfigure(1, weight = 1)
    addFrame.rowconfigure(2, weight = 1)
    addFrame.rowconfigure(3, weight = 1)
    addFrame.rowconfigure(4, weight = 1)
    
    addFrame.grid(column = 0, row = 0, sticky = "nsew")
    
    frames["addFrame"] = addFrame
    
    return(frames)


def loadModifyFrames(window):
    frames = dict()
    
    getModifyWindow().columnconfigure(0, weight = 1)
    getModifyWindow().rowconfigure(0, weight = 1)
    
    modifyFrame = Frame(getModifyWindow())
    modifyFrame["padding"] = (20, 20)
    modifyFrame["relief"] = "flat"
    modifyFrame.columnconfigure(0, weight = 1)
    modifyFrame.columnconfigure(1, weight = 5)
    modifyFrame.rowconfigure(0, weight = 1)
    modifyFrame.rowconfigure(1, weight = 1)
    modifyFrame.rowconfigure(2, weight = 1)
    modifyFrame.rowconfigure(3, weight = 1)
    modifyFrame.rowconfigure(4, weight = 1)
    
    modifyFrame.grid(column = 0, row = 0, sticky = "nsew")
    
    frames["modifyFrame"] = modifyFrame
    
    return(frames)


def loadProgressFrames(window):
    frames = dict()
    
    getProgressWindow().columnconfigure(0, weight = 0)
    getProgressWindow().rowconfigure(0, weight = 0)
    
    progressFrame = Frame(getProgressWindow())
    progressFrame["padding"] = (20, 20)
    
    progressFrame.columnconfigure(0, weight = 1)
    progressFrame.columnconfigure(1, weight = 1)
    progressFrame.columnconfigure(2, weight = 1)
    progressFrame.rowconfigure(0, weight = 1)
    progressFrame.rowconfigure(1, weight = 1)
    
    progressFrame.grid(column = 0, row = 0, sticky = "nsew")
    
    timeGraphFrame = Frame(progressFrame)
    timeGraphFrame["relief"] = "flat"
    timeGraphFrame.grid(column = 0, row = 0, sticky = "nsew")
    
    distanceGraphFrame = Frame(progressFrame)
    distanceGraphFrame["relief"] = "flat"
    distanceGraphFrame.grid(column = 1, row = 0, sticky = "nsew")
    
    weightGraphFrame = Frame(progressFrame)
    weightGraphFrame["relief"] = "flat"
    weightGraphFrame.grid(column = 2, row = 0, sticky = "nsew")
    
    streakFrame = Frame(progressFrame)
    streakFrame.columnconfigure(0, weight = 1)
    streakFrame.columnconfigure(1, weight = 1)
    streakFrame["relief"] = "flat"
    streakFrame.grid(column = 1, row = 1, sticky = "nsew")
    
    
    frames["progressFrame"] = progressFrame
    frames["timeGraphFrame"] = timeGraphFrame
    frames["distanceGraphFrame"] = distanceGraphFrame
    frames["weightGraphFrame"] = weightGraphFrame
    frames["streakFrame"] = streakFrame
    
    return(frames)