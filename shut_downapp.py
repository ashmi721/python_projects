# tkinter module is the standared python interface to the Tk GUI toolkit, which provide a set of tools
# and widgets for building graphical user interfaces.
from tkinter import *
import tkinter as tk
import os

# Note-:
''' This code with in the funtion define the os.system("shutdown /r /t 1"):
1. os.system() to execute a system command
2. shutdown is the command-line utility to used manage system shutdown operation
3. /r  is shutdown command to restart the computer after shutting it down
4. /t 1 is sets the time delay before the shutdown or restart
'''

# Function to restart the computer
def restart():
    os.system("shutdown /r /t 1")

# Function to restart the computer after a specified time (20 seconds in this case)
def restart_time():
    os.system("shutdown /r /t 20")

# Function to log out of the computer


def logout():
    os.system("shutdown /l")

# Function to shut down the computer
def shutdown():
    os.system("shutdown /s /t 1")


# Create the Tkinter application instance
st = tk.Tk()

# Set the title of the application window
st.title("ShutDown App")

# Set the dimensions of the application window
st.geometry("500x500")

# Set the background color of the application window
st.config(bg="Blue")

# Create a Restart button widget
r_button = Button(st, text="Restart", font=("Times New Roman", 20, "bold"),
                   relief=RAISED, cursor="plus", command=restart)

# Place the button on the application window at the specified position
r_button.place(x=150, y=60, height=50, width=200)

# Create a RestartTime button widget
rt_button = Button(st, text="Restart Time", font=("Times New Roman", 20, "bold"),
                   relief=RAISED, cursor="plus", command=restart_time)
rt_button.place(x=150, y=160, height=50, width=200)

# Create a Logout button widget
lg_button = Button(st, text="Log-Out", font=("Times New Roman", 20, "bold"),
                   relief=RAISED, cursor="plus", command=logout)
lg_button.place(x=150, y=260, height=50, width=200)

# Create a shutdown button widget
st_button = Button(st, text="ShutDown", font=("Times New Roman", 20, "bold"),
                   relief=RAISED, cursor="plus", command=shutdown)
st_button.place(x=150, y=360, height=50, width=200)

# Start the Tkinter event loop
st.mainloop()
