import tkinter as tk
from tkinter import messagebox

tasks = []


def add_task(event=None):
    task = entry.get()
    if task != "":
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def update_task():
    try:
        index = listbox.curselection()[0]
        new_task = entry.get()
        if new_task != "":
            tasks[index] = new_task
            listbox.delete(index)
            listbox.insert(index, new_task)
            entry.delete(0, tk.END)
    except:
        pass

def delete_task():
    try:
        index = listbox.curselection()[0]
        tasks.pop(index)
        listbox.delete(index)
    except:
        pass

def view_tasks():
    if tasks:
        all_tasks = "\n".join(tasks)
        messagebox.showinfo("All Tasks", all_tasks)
    else:
        messagebox.showinfo("All Tasks", "NO TASKS AVAILABLE ")


def stop_app():
    root.destroy()


root = tk.Tk()
root.title("TO-DO LIST")
root.geometry("400x420")
root.resizable(False, False)

tk.Label(root, text="WELCOME TO-DO LIST MANAGEMENT",
         font=("Times New Roman", 14, "bold")).pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=5, padx=10, fill=tk.X)

#  Auto-add when Enter key is pressed
entry.bind("<Return>", add_task)

listbox = tk.Listbox(root, font=("Arial", 12), height=10)
listbox.pack(pady=10, padx=20, fill=tk.BOTH)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

# tk.Button(btn_frame, text="Add", width=10,
#           command=add_task).grid(row=0, column=0, padx=5)

tk.Button(btn_frame, text="Update", width=10,
          command=update_task).grid(row=0, column=1, padx=5)

tk.Button(btn_frame, text="Delete", width=10,
          command=delete_task).grid(row=0, column=2, padx=5)

tk.Button(btn_frame, text="View", width=10,
          command=view_tasks).grid(row=0, column=3, pady=5)

tk.Button(root, text="Stop", width=20,
          command=stop_app).pack(pady=10)

root.mainloop()
