# Python GUI App
This is a structure to simplify the management of UIs created with tkinter.
The project is devides the jobs of each part of the UI into its specific source files.

# App
This is where the program starts.

# Shared
Allows every part of the code to access global variables through setters and getters, allowing the parts of the UI to communicate with one another.
This is where the state of the program is usually stored.
By default, the shared module stores the window object and the dictionaries for widgets and stringvars.

# Window
This is where the window creation and destruction code is situated.
In here you can change the behaviour of the main window or create new functions to create and destroy new windows or Toplevel windows.
By default, you can create a window by using the function "createWindow()".

# Frames
In here you can define the frames (similar to '<'div'>') which will populate the window, and at the same time will be populated by specific widgets.
By default, the sample program creates a frame through the function "loadFrames(window)". This function returns a dictionary of all the frames loaded in the window.

# Widgets
This is where you define all your widgets that will be loaded to the corresponding frames. This procedure is automated by calling the "loadWidgets(frames)" function: it will load a dictionaries of frames (returned by the "loadFrames()" function from the Frames module) and call a specific function to load the widgets that will go in that frame.
The association between frames and widgets is done by matching the name of the frame in the "loadWidgets()" function. This allows to populate a window of frames and widgets simply by calling "loadWidgets(loadFrames(getWindow()))". Each new frame needs to have the corresponding entry in the "loadWidgets()" function to be populated by widgets.

# Style
Here is where the window style gets loaded and set, through the use of the "loadStyle(window)" function.