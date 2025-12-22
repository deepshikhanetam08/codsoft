import tkinter as tk

root = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x350")
root.resizable(False, False)

# Entry box
entry = tk.Entry(root, font=("Arial", 20), bd=8, relief=tk.RIDGE, justify="right")
entry.pack(fill=tk.BOTH, ipadx=12, ipady=20, padx=15, pady=15)

def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        clear()
        entry.insert(0, result)
    except:
        clear()
        entry.insert(0, "Error")

# layout for Buttons 
buttons = [
    ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
    ('0', 3, 0), ('AC', 3, 1), ('=', 3, 2), ('+', 3, 3)
]

# Button frame
frame = tk.Frame(root)
frame.pack()

# Create buttons
for (text, row, col) in buttons:
    if text == 'AC':
        btn = tk.Button(frame, text=text, width=6, height=2,
                        command=clear)
    elif text == '=':
        btn = tk.Button(frame, text=text, width=6, height=2,
                        command=calculate)
    else:
        btn = tk.Button(frame, text=text, width=6, height=2,
                        command=lambda t=text: click(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
