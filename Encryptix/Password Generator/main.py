import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import random
import string
import pyperclip

# Function to generate password
def generate_password():
    length = length_var.get()
    include_uppercase = uppercase_var.get()
    include_numbers = numbers_var.get()
    include_symbols = symbols_var.get()
    exclude_chars = exclude_var.get()
    
    if not length.isdigit() or int(length) < 1:
        messagebox.showerror("Invalid Input", "Please enter a valid length")
        return

    length = int(length)

    char_set = string.ascii_lowercase
    if include_uppercase:
        char_set += string.ascii_uppercase
    if include_numbers:
        char_set += string.digits
    if include_symbols:
        char_set += string.punctuation

    if exclude_chars:
        char_set = ''.join(ch for ch in char_set if ch not in exclude_chars)

    if not char_set:
        messagebox.showerror("Invalid Input", "Character set is empty")
        return

    password = ''.join(random.choice(char_set) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Function to copy password to clipboard
def copy_to_clipboard():
    password = password_entry.get()
    pyperclip.copy(password)
    messagebox.showinfo("Copied", "Password copied to clipboard")

# Create main window
root = tk.Tk()
root.title("Advanced Password Generator")

# Create and place widgets
tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=10)
length_var = tk.StringVar(value="12")
tk.Entry(root, textvariable=length_var).grid(row=0, column=1, padx=10, pady=10)

uppercase_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var).grid(row=1, column=0, columnspan=2, padx=10, pady=10)

numbers_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

symbols_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

tk.Label(root, text="Exclude Characters:").grid(row=4, column=0, padx=10, pady=10)
exclude_var = tk.StringVar()
tk.Entry(root, textvariable=exclude_var).grid(row=4, column=1, padx=10, pady=10)

tk.Button(root, text="Generate Password", command=generate_password).grid(row=5, column=0, columnspan=2, pady=10)

password_entry = tk.Entry(root, width=50)
password_entry.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).grid(row=7, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
