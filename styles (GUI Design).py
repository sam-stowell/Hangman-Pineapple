from PIL import Image, ImageTk  # Import necessary modules for handling images
import tkinter as tk  # Import tkinter library for GUI

# Color constants for the GUI
BACKGROUND_COLOR_PRIMARY = "#fffa6a"  # Primary background color
BACKGROUND_COLOR_SECONDARY = "#fffa6a"  # Secondary background color
BUTTON_BACKGROUND_COLOR = "white"  # Background color for buttons
TEXT_COLOR = "black"  # Color for text elements
ACTIVE_BUTTON_BACKGROUND_COLOR = "green"  # Background color for active buttons
ACTIVE_BUTTON_FOREGROUND_COLOR = "white"  # Foreground (text) color for active buttons

# Font constants for the GUI
HEADER_FONT = ("Calibri", 30)  # Font for headers
BUTTON_FONT = ("Calibri", 20)  # Font for buttons
LABEL_FONT = ("Calibri", 30)  # Font for labels

# Dimensions for buttons
BUTTON_WIDTH = 5  # Width of buttons
BUTTON_HEIGHT = 3  # Height of buttons

# Function to center a widget on the screen
def center_widget(widget):
    widget.update_idletasks()  # Update widget to get correct size
    width = widget.winfo_width()  # Get widget width
    height = widget.winfo_height()  # Get widget height
    x = (widget.master.winfo_width() - width) // 2  # Calculate x-coordinate for centering
    y = (widget.master.winfo_height() - height) // 2  # Calculate y-coordinate for centering
    widget.place(in_=widget.master, x=x, y=y)  # Place the widget at the calculated coordinates
