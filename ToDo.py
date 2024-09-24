import tkinter as tk
from tkinter import messagebox, filedialog
from tkcalendar import DateEntry
from fpdf import FPDF
import json
import os

# File path for saving tasks
TASKS_FILE = "tasks.json"

# Initialize the main app window
root = tk.Tk()
root.title("To-Do")
root.geometry("400x550")

# Lists to store tasks and their completion status
tasks = []

# Load tasks from file if it exists
def load_tasks():
    global tasks
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            tasks = json.load(file)
        update_task_list()

# Save tasks to file
def save_tasks():
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

# Function to add a new task
def add_task():
    task_name = task_entry.get()
    task_time = time_entry.get()
    task_date = date_entry.get()
    
    if not task_name or not task_time or not task_date:
        messagebox.showwarning("Input Error", "All fields are required!")
        return
    
    task = {"name": task_name, "time": task_time, "date": task_date, "completed": False}
    tasks.append(task)
    update_task_list()
    task_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)
    save_tasks()  # Save tasks after adding a new one

# Function to update the task list display
def update_task_list():
    task_listbox.delete(0, tk.END)
    for idx, task in enumerate(tasks):
        task_str = f"{task['name']} - {task['time']} - {task['date']}"
        if task['completed']:
            task_str += " [Completed]"
        task_listbox.insert(tk.END, task_str)

# Function to toggle task completion
def toggle_task():
    selected = task_listbox.curselection()
    if selected:
        idx = selected[0]
        tasks[idx]['completed'] = not tasks[idx]['completed']
        update_task_list()
        save_tasks()  # Save tasks after toggling completion

# Function to save tasks as a PDF with improved formatting
def save_as_pdf():
    if not tasks:
        messagebox.showwarning("No Tasks", "No tasks to save.")
        return
    
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if not file_path:
        return
    
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=14)

    pdf.cell(200, 10, txt="To-Do List", ln=True, align="C")

    for task in tasks:
        status = "Completed" if task['completed'] else "Pending"
        task_text = f"Task: {task['name']} | Time: {task['time']} | Date: {task['date']} | Status: {status}"
        pdf.multi_cell(0, 10, txt=task_text)

    pdf.output(file_path)
    messagebox.showinfo("Success", f"Tasks saved as {file_path}")

# Function to remove all tasks
def remove_all_tasks():
    if not tasks:
        messagebox.showwarning("No Tasks", "There are no tasks to remove.")
        return
    
    confirm = messagebox.askyesno("Remove All Tasks", "Are you sure you want to remove all tasks?")
    if confirm:
        tasks.clear()
        update_task_list()
        save_tasks()

# GUI Elements
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)
task_entry.insert(0, "Enter Task")

time_entry = tk.Entry(root, width=30)
time_entry.pack(pady=10)
time_entry.insert(0, "Enter Time (e.g., 10:00 AM)")

date_entry = DateEntry(root, width=27, background='darkblue', foreground='white', borderwidth=2)
date_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=10)

task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=15)
task_listbox.pack(pady=20)

toggle_button = tk.Button(root, text="Finished", command=toggle_task)
toggle_button.pack(pady=5)

remove_all_button = tk.Button(root, text="Remove All Tasks", command=remove_all_tasks)
remove_all_button.pack(pady=5)

save_button = tk.Button(root, text="Save as PDF", command=save_as_pdf)
save_button.pack(pady=5)

# Load tasks when the app starts
load_tasks()

# Save tasks when the window is closed
root.protocol("WM_DELETE_WINDOW", lambda: (save_tasks(), root.destroy()))

# Run the application
root.mainloop()


