import os

from tkinter import *
from widgets import *
from frames import *
from style import *
from window import *
from dataParser import *

# main function
def main():
    createWindow() # create the window
    loadWidgets(loadFrames(getWindow())) # load the frames and the widgets
    
    if os.path.isfile("./data/workout.txt") == True:
        clickHandler("load", "./data/workout.txt")
        
    getWindow().mainloop()    # run the app

if __name__ == "__main__":
    main()