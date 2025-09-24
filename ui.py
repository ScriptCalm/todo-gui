# ui.py
import tkinter as tk
from tkinter import messagebox
import db

def refresh_task_list():
    listbox.delete(0, tk.END)
    tasks = db.get_tasks()
    for task in tasks:
        listbox.insert(tk.END, f"{task[0]}. {task[1]}")

def add_task():
    task_text = entry.get().strip()
    if task_text == "":
        messagebox.showwarning("Empty Task", "Please enter a task.")
        return
    db.add_task(task_text)
    entry.delete(0, tk.END)
    refresh_task_list()

def delete_task():
    selected = listbox.curselection()
    if not selected:
        messagebox.showinfo("Select Task", "Please select a task to delete.")
        return
    task_str = listbox.get(selected[0])
    task_id = int(task_str.split(".")[0])
    db.delete_task(task_id)
    refresh_task_list()

# GUI Setup
root = tk.Tk()
root.title("To-Do App")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

entry = tk.Entry(frame, width=40)
entry.grid(row=0, column=0, padx=(0, 5))

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=1)

listbox = tk.Listbox(frame, width=50, height=10)
listbox.grid(row=1, column=0, columnspan=2, pady=10)

delete_button = tk.Button(frame, text="Delete Selected", command=delete_task)
delete_button.grid(row=2, column=0, columnspan=2)

# Initialize DB and load tasks
db.init_db()
refresh_task_list()

root.mainloop()
