import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        
        self.tasks = []

        self.task_listbox = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=20)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=10)

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.pack(side=tk.LEFT, padx=10)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=10)

        self.complete_button = tk.Button(root, text="Complete Task", command=self.complete_task)
        self.complete_button.pack(side=tk.LEFT, padx=10)

    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter the task:")
        if task and task.strip(): 
            self.tasks.append({"task": task, "completed": False})
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Completed" if task["completed"] else "Not Completed"
            self.task_listbox.insert(tk.END, f"{task['task']} [{status}]")

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if not selected_task_index:
            messagebox.showwarning("Warning", "Please select a task to update.")
            return

        task_index = selected_task_index[0]
        new_task = simpledialog.askstring("Update Task", "Enter the new task:")
        if new_task and new_task.strip(): 
            self.tasks[task_index]["task"] = new_task
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "Updated task cannot be empty!")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if not selected_task_index:
            messagebox.showwarning("Warning", "Please select a task to delete.")
            return

        task_index = selected_task_index[0]
        self.tasks.pop(task_index)
        self.update_task_listbox()

    def complete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if not selected_task_index:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")
            return

        task_index = selected_task_index[0]
        self.tasks[task_index]["completed"] = True
        self.update_task_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
