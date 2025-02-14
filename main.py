# Tkinter used for GUI
from tkinter import Tk
import tkinter as tk
# For calendar
from tkcalendar import Calendar 

def show_date(event):
    selected_date = cal.get_date()
    label.config(text=f"Selected Date: {selected_date}")

# Create the window, giving it a title, and its dimensions
root = Tk()
root.title("To-Do List")
root.geometry('400x600')
# Color
root.configure(bg="LightSteelBlue2")

# Adding a calendar
cal = Calendar(root, selectmode="day", date_pattern="mm/dd/yy", 
background="white", foreground = "green", firstweekday="sunday",
font= "Arial 17")
cal.pack(pady=20)

# Label for date
label = tk.Label(root, text="Selected Date: ")
label.pack(pady=10)

# Binding the show_date function
cal.bind("<<CalendarSelected>>", show_date)

# Executing the GUI
root.mainloop()