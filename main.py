# Tkinter used for GUI
from tkinter import Tk
import tkinter as tk
# For calendar
from tkcalendar import Calendar 

def show_date():
    selected_date = cal.get_date()
    label.config(text=f"Selected Date: {selected_date}")

# Create the window, giving it a title, and its dimensions
root = Tk()
root.title("To-Do List")
root.geometry('400x400')
# Color
root.configure(bg="LightSteelBlue2")

# Adding a calendar
cal = Calendar(root, selectmode="day", date_pattern="m/d/yy", 
background="white", foreground = "green")
cal.pack(pady=20)

# Label for date
label = tk.Label(root, text="Selected Date: ")
label.pack(pady=10)

# Button for the show date function
button = tk.Button(root, text="Get Date", command=show_date)
button.pack()

# Executing the GUI
root.mainloop()