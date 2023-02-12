from tkinter import *
from widgets import *
from frames import *
from style import *
from window import *

# main function
def main():
    createWindow() # create the window
    loadWidgets(loadFrames(getWindow())) # load the frames and the widgets
    getWindow().mainloop()    # run the app

if __name__ == "__main__":
    main()