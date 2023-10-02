import tkinter as tk
from tkinter import messagebox

# Create the main application window
app = tk.Tk()
app.title("To-Do List App")

# Initialize a list to store tasks
tasks = []

# Function to add a new task
def add_task():
    task = entry.get()
    if task:
        tasks.append({"task": task, "complete": False})
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to remove a selected task
def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        del tasks[selected_task_index[0]]
        update_listbox()

# Function to mark a task as complete or incomplete
def toggle_complete():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        tasks[selected_task_index[0]]["complete"] = not tasks[selected_task_index[0]]["complete"]
        update_listbox()

# Function to update the task listbox
def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        if task["complete"]:
            listbox.insert(tk.END, "[X] " + task["task"])
        else:
            listbox.insert(tk.END, "[ ] " + task["task"])

# Entry widget for entering tasks
entry = tk.Entry(app)
entry.pack(pady=10)

# Button to add tasks
add_button = tk.Button(app, text="Add Task", command=add_task)
add_button.pack()

# Button to remove tasks
remove_button = tk.Button(app, text="Remove Task", command=remove_task)
remove_button.pack()

# Button to mark/unmark tasks as complete
complete_button = tk.Button(app, text="Mark/Unmark Complete", command=toggle_complete)
complete_button.pack()

# Listbox to display tasks
listbox = tk.Listbox(app)
listbox.pack()

# Run the application
app.mainloop()
