import tkinter as tk

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []
        self.create_widgets()

    def create_widgets(self):
        self.task_listbox = tk.Listbox(self.root, height=10, width=50, font=("Arial", 14))
        self.task_listbox.pack()

        self.entry = tk.Entry(self.root, font=("Arial", 14), width=40)
        self.entry.pack(pady=10)

        add_button = tk.Button(self.root, text="Add Task", font=("Arial", 14), command=self.add_task)
        add_button.pack()

        delete_button = tk.Button(self.root, text="Delete Task", font=("Arial", 14), command=self.delete_task)
        delete_button.pack()

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.entry.delete(0, tk.END)

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.task_listbox.get(selected_task_index)
            self.tasks.remove(task)
            self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
