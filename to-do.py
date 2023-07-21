import tkinter as tk
from tkinter import messagebox

def add_task(event=None):
    task = entry.get()
    description = description_entry.get("1.0", tk.END).strip()  # Get the description text
    if task:
        task_with_description = f"{task}\n{description}"
        listbox.insert(tk.END, task_with_description)
        entry.delete(0, tk.END)
        description_entry.delete("1.0", tk.END)  # Clear the description entry
        update_task_count()
        listbox.see(tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task(event=None):
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
        update_task_count()
    except IndexError:
        pass

def clear_tasks(event=None):
    listbox.delete(0, tk.END)
    update_task_count()

def edit_task(event=None):
    try:
        index = listbox.curselection()[0]
        selected_task = listbox.get(index).split("\n")[0]  # Get the task name without the description
        selected_description = listbox.get(index).split("\n", 1)[1]  # Get the description
        entry.delete(0, tk.END)
        entry.insert(tk.END, selected_task)
        description_entry.delete("1.0", tk.END)
        description_entry.insert(tk.END, selected_description.strip())
        listbox.delete(index)
    except IndexError:
        pass

def update_task_count():
    task_count = listbox.size()
    count_label.configure(text=f"Total Tasks: {task_count}")

def main():
    global entry, description_entry, listbox, count_label
    root = tk.Tk()
    root.title("To-Do List")
    root.geometry("500x600")
    root.resizable(False, False)

    # Styling
    root.configure(background="#F0F0F0")
    root.option_add("*Font", "Arial 12")

    heading_frame = tk.Frame(root, bg="#A26FF5")
    heading_frame.pack(fill=tk.BOTH)

    heading_label = tk.Label(
        heading_frame,
        text="To-Do List",
        font=("Brush Script MT", 36, "bold"),
        fg="white",
        bg="#A26FF5",
        padx=10,
        pady=5,
    )
    heading_label.pack()

    frame = tk.Frame(root, bg="#F0F0F0", bd=1, relief=tk.SOLID)
    frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

    listbox = tk.Listbox(
        frame,
        width=50,
        height=10,
        font=("Arial", 14),
        bd=0,
        bg="#F8F8F8",
        selectbackground="#C0C0C0",
    )
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=5, pady=5)

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    entry = tk.Entry(
        root,
        font=("Arial", 14),
        bg="white",
        relief=tk.SOLID,
        borderwidth=1,
    )
    entry.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

    description_label = tk.Label(
        root,
        text="Description:",
        font=("Arial", 14),
        bg="#F0F0F0",
    )
    description_label.pack(pady=5)

    description_entry = tk.Text(
        root,
        font=("Arial", 14),
        height=5,
        bg="white",
        relief=tk.SOLID,
        borderwidth=1,
    )
    description_entry.pack(pady=5, padx=20, fill=tk.BOTH, expand=True)

    button_frame = tk.Frame(root, bg="#F0F0F0")
    button_frame.pack(pady=10)

    button_style = {
        "font": ("Arial", 14, "bold"),
        "bg": "#B9B9B9",
        "fg": "white",
        "activebackground": "#707070",
        "activeforeground": "white",
        "relief": tk.SOLID,
        "bd": 0,
        "highlightthickness": 0,
    }

    add_button = tk.Button(
        button_frame,
        text="Add Task",
        **button_style,
        command=add_task,
    )
    add_button.pack(side=tk.LEFT, padx=10)

    delete_button = tk.Button(
        button_frame,
        text="Delete Task",
        **button_style,
        command=delete_task,
    )
    delete_button.pack(side=tk.LEFT, padx=10)

    clear_button = tk.Button(
        button_frame,
        text="Clear All",
        **button_style,
        command=clear_tasks,
    )
    clear_button.pack(side=tk.LEFT, padx=10)

    count_label = tk.Label(
        root,
        text="Total Tasks: 0",
        font=("Arial", 14),
        bg="#F0F0F0",
    )
    count_label.pack(pady=5)

    # Double-click to edit task
    listbox.bind("<Double-Button-1>", edit_task)

    # Keyboard shortcuts
    root.bind("<Return>", add_task)
    root.bind("<Delete>", delete_task)
    root.bind("<Control-Delete>", clear_tasks)

    root.mainloop()

if __name__ == "__main__":
    main()
