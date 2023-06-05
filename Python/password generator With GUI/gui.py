import random
import string
import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip


def generate_password():
    """Generate a strong and secure password based on user specifications."""
    length = int(length_entry.get())
    complexity = complexity_combobox.get()

    # Define the character sets based on complexity levels
    low_complexity = string.ascii_letters + string.digits
    medium_complexity = low_complexity + string.punctuation
    high_complexity = medium_complexity + string.ascii_uppercase

    # Select the character set based on complexity
    if complexity == 'Low':
        characters = low_complexity
    elif complexity == 'Medium':
        characters = medium_complexity
    elif complexity == 'High':
        characters = high_complexity
    else:
        messagebox.showerror("Error", "Invalid complexity level. Please choose Low, Medium, or High.")
        return

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))

    # Display the generated password
    password_label.config(text=password)


def copy_password():
    """Copy the generated password to the clipboard."""
    password = password_label.cget("text")
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Success", "Password copied to clipboard!")
    else:
        messagebox.showwarning("No Password", "No password generated yet.")


# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Create and pack the widgets
length_label = tk.Label(window, text="Length:")
length_label.pack()
length_entry = tk.Entry(window)
length_entry.pack()

complexity_label = tk.Label(window, text="Complexity:")
complexity_label.pack()
complexity_combobox = ttk.Combobox(window)
complexity_combobox['values'] = ["Low", "Medium", "High"]
complexity_combobox.current(0)
complexity_combobox.pack()

generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

password_label = tk.Label(window, text="Generated Password", relief="solid", padx=10, pady=10)
password_label.pack()

copy_button = tk.Button(window, text="Copy Password", command=copy_password)
copy_button.pack()
# Start the main loop
window.mainloop()
