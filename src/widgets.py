from tkinter.ttk import *
from tkinter import PhotoImage
from tkinter import StringVar
from tkinter import messagebox
from frames import *
from shared import *

widgets = dict()

def clickHandler(*args):
    print(args[0])
    
    if (args[0] == "addMain"):
        if getAddWindow() is None:
            createAddWindow("Add", 500, 300, 0, 0, False, False, 0, 0, 500, 300, 1)
            loadWidgets(loadAddFrames(getAddWindow()))
        
    if (args[0] == "modifyMain"):
        if len(getWidgets()["days"].selection()) == 0:
            messagebox.showerror("Selection Error",
                                 "No day selected")
            return()
        
        if getModifyWindow() is None:
            createModifyWindow("Modify", 500, 300, 0, 0, False, False, 0, 0, 500, 300, 1)
            loadWidgets(loadModifyFrames(getModifyWindow()))
            
            item = getWidgets()["days"].item(getWidgets()["days"].selection()[0])
            values = item['values']
            
            getStrings()["dateEntry"].set(values[0])
            getStrings()["timeEntry"].set(values[1])
            getStrings()["distanceEntry"].set(values[2])
            getStrings()["weightEntry"].set(values[3])
            
    if (args[0] == "add"):        
        getWidgets()["days"].insert('', 0, values = (
            getStrings()["dateEntry"].get(),
            getStrings()["timeEntry"].get(),
            getStrings()["distanceEntry"].get(),
            getStrings()["weightEntry"].get()
        ))
    
    if (args[0] == "modify"):
        selectedItem = getWidgets()["days"].selection()[0]
        getWidgets()["days"].item(selectedItem, values = (
            getStrings()["dateEntry"].get(),
            getStrings()["timeEntry"].get(),
            getStrings()["distanceEntry"].get(),
            getStrings()["weightEntry"].get()
        ))
        
    if (args[0] == "remove"):
        if len(getWidgets()["days"].selection()) == 0:
            messagebox.showerror("Selection Error",
                                 "No day selected")
            return()
        
        selectedItem = getWidgets()["days"].selection()[0]
        getWidgets()["days"].delete(selectedItem)



def loadWidgets(frames):
    if "daysF" in frames:
        loadDays(frames["daysF"])
    if "buttonsF" in frames:
        loadButtons(frames["buttonsF"])
    if "addFrame" in  frames:
        loadAdd(frames["addFrame"])
    if "modifyFrame" in frames:
        loadModify(frames["modifyFrame"])
        
        
        
def loadDays(frame):
    columns = ('date', 'time', 'distance', 'weight')
    
    days = Treeview(
        frame,
        columns = columns,
        show = 'headings'
    )
    
    days.heading('date', text = "Date")
    days.heading('time', text = "Time")
    days.heading('distance', text = "Distance (Km)")
    days.heading('weight', text = "Weight (Kg)")
    
    scrollbar = Scrollbar(frame, orient = VERTICAL, command = days.yview)
    days.configure(yscroll = scrollbar.set)
    
    days.pack(side = LEFT, fill = 'both', expand = True)
    
    getWidgets()["days"] = days
    

def loadButtons(frame):
    addButton = Button(
        frame,
        text = "Add",
        command = lambda: clickHandler("addMain")
    )
    
    removeButton = Button(
        frame,
        text = "Remove",
        command = lambda: clickHandler("remove")
    )
    
    modifyButton = Button(
        frame,
        text = "Modify",
        command = lambda: clickHandler("modifyMain")
    )
    
    progressButton = Button(
        frame,
        text = "Progress",
        command = lambda: clickHandler("progressMain")
    )
    
    addButton.grid(column = 0, row = 0, sticky = "E")
    removeButton.grid(column = 1, row = 0)
    modifyButton.grid(column = 2, row = 0, sticky = "W")
    progressButton.grid(column = 3, row = 0, sticky = "W")


def loadAdd(frame):
    getStrings()["dateEntry"] = StringVar(name = "dateEntry")
    getStrings()["timeEntry"] = StringVar(name = "timeEntry")
    getStrings()["distanceEntry"] = StringVar(name = "distanceEntry")
    getStrings()["weightEntry"] = StringVar(name = "weightEntry")
    
    dateLabel = Label(
        frame,
        text = "Date"
    )
    
    dateEntry = Entry(
        frame,
        textvariable = getStrings()["dateEntry"]
    )
    dateEntry.focus()
    
    
    timeLabel = Label(
        frame,
        text = "Time"
    )
    
    timeEntry = Entry(
        frame,
        textvariable = getStrings()["timeEntry"]
    )
    
    
    distanceLabel = Label(
        frame,
        text = "Distance"
    )
    
    distanceEntry = Entry(
        frame,
        textvariable = getStrings()["distanceEntry"]
    )
    
    
    weightLabel = Label(
        frame,
        text = "Weight"
    )
    
    weightEntry = Entry(
        frame,
        textvariable = getStrings()["weightEntry"]
    )
    
    
    addButton = Button(
        frame,
        text = "Add",
        command = lambda: clickHandler("add")
    )
    
    
    dateLabel.grid(row = 0, column = 0)
    dateEntry.grid(row = 0, column = 1, sticky = "EW")
    
    timeLabel.grid(row = 1, column = 0)
    timeEntry.grid(row = 1, column = 1, sticky = "EW")
    
    distanceLabel.grid(row = 2, column = 0)
    distanceEntry.grid(row = 2, column = 1, sticky = "EW")
    
    weightLabel.grid(row = 3, column = 0)
    weightEntry.grid(row = 3, column = 1, sticky = "EW")
    
    addButton.grid(row = 4, column = 0, columnspan = 2)
    
    
def loadModify(frame):
    getStrings()["dateEntry"] = StringVar(name = "dateEntry")
    getStrings()["timeEntry"] = StringVar(name = "timeEntry")
    getStrings()["distanceEntry"] = StringVar(name = "distanceEntry")
    getStrings()["weightEntry"] = StringVar(name = "weightEntry")
    
    dateLabel = Label(
        frame,
        text = "Date"
    )
    
    dateEntry = Entry(
        frame,
        textvariable = getStrings()["dateEntry"]
    )
    dateEntry.focus()
    
    
    timeLabel = Label(
        frame,
        text = "Time"
    )
    
    timeEntry = Entry(
        frame,
        textvariable = getStrings()["timeEntry"]
    )
    
    
    distanceLabel = Label(
        frame,
        text = "Distance"
    )
    
    distanceEntry = Entry(
        frame,
        textvariable = getStrings()["distanceEntry"]
    )
    
    
    weightLabel = Label(
        frame,
        text = "Weight"
    )
    
    weightEntry = Entry(
        frame,
        textvariable = getStrings()["weightEntry"]
    )
    
    
    modifyButton = Button(
        frame,
        text = "Modify",
        command = lambda: clickHandler("modify")
    )
    
    
    dateLabel.grid(row = 0, column = 0)
    dateEntry.grid(row = 0, column = 1, sticky = "EW")
    
    timeLabel.grid(row = 1, column = 0)
    timeEntry.grid(row = 1, column = 1, sticky = "EW")
    
    distanceLabel.grid(row = 2, column = 0)
    distanceEntry.grid(row = 2, column = 1, sticky = "EW")
    
    weightLabel.grid(row = 3, column = 0)
    weightEntry.grid(row = 3, column = 1, sticky = "EW")
    
    modifyButton.grid(row = 4, column = 0, columnspan = 2)
    