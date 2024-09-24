To-Do List App
A simple to-do list application built using Python and Tkinter with a graphical user interface (GUI). The app allows users to add tasks, set task time and date, mark tasks as completed, remove all tasks, and save the task list as a PDF. Tasks are automatically saved and loaded from a JSON file, ensuring they persist between sessions.

Features
Add Tasks: Add tasks with a description, time, and date.
Mark as Completed: Check off tasks when completed with a toggle button.
Remove All Tasks: Clear the entire task list with a single click.
Save as PDF: Export your task list to a PDF file with the option to choose the save location.
Persistent Storage: Tasks are saved to a JSON file and reloaded when the app is reopened.
Installation
Prerequisites
Ensure you have Python installed on your system. This app is compatible with Python 3.x.

Required Libraries
Install the required libraries using pip:

bash
Copy code
pip install tkcalendar fpdf
Running the Application
Download or clone this repository.

Navigate to the directory containing the script.

Run the application using:

bash
Copy code
python your_script_name.py
Replace your_script_name.py with the name of your Python script.

How to Use
Add a Task: Enter the task description, set the time and date, and click Add Task.
Mark as Completed: Select a task from the list and click Toggle Complete to mark it as done.
Remove All Tasks: Click Remove All Tasks to clear the task list. A confirmation dialog will appear.
Save as PDF: Click Save as PDF to export your tasks. You can choose where to save the PDF file.
Close the App: Tasks are automatically saved to tasks.json when you close the app and will be loaded when you open it again.

Code Structure
TASKS_FILE: The JSON file (tasks.json) where tasks are saved.
load_tasks(): Loads tasks from the JSON file at startup.
save_tasks(): Saves the tasks to the JSON file when modified.
add_task(): Adds a new task to the list and saves it.
update_task_list(): Updates the task display in the GUI.
toggle_task(): Toggles the completion status of a selected task.
save_as_pdf(): Exports the task list to a PDF file.
remove_all_tasks(): Clears all tasks from the list after confirmation.
Future Improvements
Add the ability to edit tasks directly from the list.
Implement a search or filter functionality to find tasks quickly.
Add notifications or reminders for tasks based on time and date.
Troubleshooting
GUI Issues: Ensure that your Tkinter version is compatible with Python 3.x.
PDF Formatting: Adjust the font size in the save_as_pdf() function if the text appears too small or too large.
Missing JSON File: If tasks.json is missing, the app will automatically create it when tasks are saved.
Contributing
If you wish to contribute, please fork the repository and submit a pull request with your improvements.

License
This project is open-source and available under the MIT License.