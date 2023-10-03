import tkinter as tk
import random
import string

# Function to generate a random password based on complexity level
def generate_password(length, complexity):
    characters = ""
    if complexity == 1:
        characters = string.ascii_letters
    elif complexity == 2:
        characters = string.ascii_letters + string.digits
    elif complexity == 3:
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to generate and display the password
def generate_and_display_password():
    length = int(length_entry.get())
    complexity = int(complexity_entry.get())
    password = generate_password(length, complexity)
    password_text.delete(1.0, tk.END)  # Clear any previous password
    password_text.insert(tk.END, password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Increase the window size
root.geometry("400x300")

# Create and configure widgets
length_label = tk.Label(root, text="Password Length:")
length_entry = tk.Entry(root)
complexity_label = tk.Label(root, text="Complexity Level (1, 2, or 3):")
complexity_entry = tk.Entry(root)
generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password)
password_text = tk.Text(root, height=5, width=40)

# Pack widgets into the window
length_label.pack()
length_entry.pack()
complexity_label.pack()
complexity_entry.pack()
generate_button.pack()
password_text.pack()

# Start the GUI event loop
root.mainloop()
