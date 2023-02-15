from tkinter.ttk import *
from tkinter import *
from shared import *
from functools import partial

def popupMenu(event):
    try:
        getWidgets()["rightClickMenu"].tk_popup(event.x_root, event.y_root)
    finally:
        getWidgets()["rightClickMenu"].grab_release()
        
        
def styleSelector(style):
    styleObj = Style(getWindow())
    styleObj.theme_use(style)

def loadStyle(window):
    styles = Style(window)
    
    window.tk.call("source", "./themes/azure/azure.tcl")
    window.tk.call("set_theme", "dark")

    styles.configure("Warning.TLabel",
        foreground = "#f0ad4e",
        font = ("Arial", 40)
    )

    styles.configure("TLabel",
        font = ("Arial", 30)
    )
    
    rightClickMenu = Menu(
        window,
        tearoff = 0
    )
    
    getWidgets()["rightClickMenu"] = rightClickMenu
    
    for style in styles.theme_names():
        rightClickMenu.add_command(
            label = style,
            command = partial(styleSelector, style)
        )
        
    window.bind("<Button-3>", popupMenu)
    
    