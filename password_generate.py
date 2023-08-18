import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_label.config(text="Generated Password: " + password)

# Create the main window
root = tk.Tk()
root.title("Random Password Generator App")

# Create and place widgets
length_label = tk.Label(root, text="Enter the desired Password Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

password_label = tk.Label(root, text="")
password_label.pack()

# Start the main loop
root.mainloop()
