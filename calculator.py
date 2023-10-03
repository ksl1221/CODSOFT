import tkinter as tk

def append_digit(digit):
    current_text = entry_var.get()
    if current_text == "0":
        entry_var.set(digit)
    else:
        entry_var.set(current_text + digit)

def clear():
    entry_var.set("0")

def calculate():
    try:
        expression = entry_var.get()
        result = eval(expression)
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")

root = tk.Tk()
root.title("Calculator")

entry_var = tk.StringVar()
entry_var.set("0")

entry = tk.Entry(root, textvariable=entry_var, font=("Helvetica", 24), justify="right")
entry.grid(row=0, column=0, columnspan=4)

button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row, col = 1, 0

for button_text in button_texts:
    if button_text == '=':
        tk.Button(root, text=button_text, padx=20, pady=20, font=("Helvetica", 18), command=calculate).grid(row=row, column=col)
    elif button_text == 'C':
        tk.Button(root, text=button_text, padx=20, pady=20, font=("Helvetica", 18), command=clear).grid(row=row, column=col)
    else:
        tk.Button(root, text=button_text, padx=20, pady=20, font=("Helvetica", 18), command=lambda text=button_text: append_digit(text)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
