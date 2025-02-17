# Tkinter used for GUI
from tkinter import Tk , Canvas
import tkinter as tk
# For calendar
from tkcalendar import Calendar 

# Global variable for seeing if there is a listbox already present
listbox_present = False;

# Create the window, giving it a title, and its dimensions
root = Tk()
root.title("To-Do List")
root.geometry('400x600')
# Color
root.configure(bg="LightSteelBlue2")

# Function for displaying the date
def show_date(event):
    selected_date = cal.get_date()
    label.config(text=f"Selected Date: {selected_date}")

# For showing the list
def show_list():
    # Global call to variable
    global listbox_present
    if not listbox_present:
        # Then create it
        lb = tk.Listbox(root)
        # Change boolean
        listbox_present = True;
        lb.configure(background="lightblue", width=43, height = 15)
        lb.pack(pady=10)

# Function for adding entry
def add_entry():
    # task_label.pack(pady=10)
    task_entry.pack(pady=10)
    task = task_var.get()
    print(task)

# Variable for user input
task_var=tk.StringVar()

# Adding a calendar
cal = Calendar(root, selectmode="day", date_pattern="mm/dd/yy", 
background="white", foreground = "green", firstweekday="sunday",
font= "Arial 18", disabledaybackground="green")
cal.pack(pady=20)

# Label for date
label = tk.Label(root, text="Selected Date: ", font="Arial 18" )
label.pack(pady=10)

# Binding the show_date function
cal.bind("<<CalendarSelected>>", show_date, show_list)

# Label for entry
# task_label = tk.Label(root, text="Add task")
# Creating an entry
task_entry = tk.Entry(root, textvariable=task_var, font=('calibre',12,'bold'))

# Adding a button for adding a task
add = tk.Button(root, text="+", font="Arial 15", command=add_entry)
add.place(x=45, y=282)

# Executing the GUI
root.mainloop()