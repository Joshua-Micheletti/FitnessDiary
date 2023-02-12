from tkinter.ttk import *

def loadStyle(window):
    style = Style(window)
    
    window.tk.call("source", "./themes/azure/azure.tcl")
    window.tk.call("set_theme", "dark")

    style.configure("Warning.TLabel",
        foreground = "#f0ad4e",
        font = ("Arial", 40)
    )

    style.configure("TLabel",
        font = ("Arial", 30)
    )