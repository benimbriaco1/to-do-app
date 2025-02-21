# Tkinter used for GUI
from tkinter import Tk , Canvas, IntVar, Frame, Checkbutton
import tkinter as tk
# For calendar
from tkcalendar import Calendar 

# Global variable for seeing if there is a listbox already present
listbox_present = False;

# Create the window, giving it a title, its dimensions, color
root = Tk()
root.title("To-Do List")
root.geometry('400x600')
root.configure(bg="LightSteelBlue2")

lb = tk.Listbox(root)

# List to store tasks
tasks = []

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
        global lb
        # Change boolean
        listbox_present = True;
        lb.configure(background="lightblue", width=43, height = 15)
        lb.pack(pady=10)

# Function for adding entry
def add_entry():
    show_list()
    task = task_var.get()
    # Make sure entry isn't already present
    if task: #if task is not empty
        for task, _ in tasks:
            if( tasks == task):
                print(f"{task} already added")
                # Break out
                return  
        
        var = IntVar()
        check = Checkbutton(task_frame, text = task, variable = var, bg="lightblue")
        check.pack(fill="x", padx=5, pady=2, anchor="w")
        tasks.append((task, var))
        # Clear
        task_var.set("")
        update_scroll()

# Updating scrollbar
def update_scroll():
    task_canvas.update_idletasks()
    task_canvas.config(scrollregion=task_canvas.bbox("all"))

# Adding a calendar
cal = Calendar(root, selectmode="day", date_pattern="mm/dd/yy", 
background="white", foreground = "green", firstweekday="sunday",
font= "Arial 18", disabledaybackground="green")
cal.pack(pady=20)

# Label for date
label = tk.Label(root, text="Selected Date: ", font="Arial 18" )
label.pack(pady=10)

# Binding the show_date function
cal.bind("<<CalendarSelected>>", show_date)

# Creating an entry
task_var=tk.StringVar()
task_entry = tk.Entry(root, textvariable=task_var, font=('calibre',12,'bold'))
task_entry.pack(pady=10)

# Adding a button for adding a task
add = tk.Button(root, text="+", font="Arial 15", command=add_entry)
add.place(x=45, y=282)
add.pack()

# Canvas
task_canvas = Canvas(root, bg='lightblue')
task_canvas.pack(pady=10, expand=True)
# Making the scrollbar
scrollbar = tk.Scrollbar(root, orient="vertical", command=task_canvas.yview)
scrollbar.pack(side="right", fill="y")
# Making the frame
task_frame = Frame(task_canvas, bg="lightblue")
task_canvas.create_window((0,0), window=task_frame, anchor="nw")
#Configure
task_canvas.config(yscrollcommand=scrollbar.set)


# Executing the GUI
root.mainloop()