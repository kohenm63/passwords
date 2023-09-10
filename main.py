import tkinter as tk
from tkinter import messagebox
from tkinter import Listbox
import string
import secrets

# Function to add a password to the list
def add_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if website and username and password:
        # Append the password to the list
        password_listbox.insert(tk.END, f"Website: {website}, Username: {username}, Password: {password}")

        # Clear the input fields
        website_entry.delete(0, tk.END)
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

        # Save the passwords to a text file
        save_passwords()
    else:
        messagebox.showwarning("Warning", "Please fill in all fields.")

# Function to generate a strong password
def generate_password():
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(password_characters) for i in range(12))  # Generates a new 12-character password
    password_entry.delete(0, tk.END)  # Clear the current entry
    password_entry.insert(0, password)

# Function to load passwords from a text file
def load_passwords():
    password_listbox.delete(0, tk.END)  # Clear the current password list
    try:
        with open("passwords.txt", "r") as file:
            for line in file:
                password_listbox.insert(tk.END, line.strip())
    except FileNotFoundError:
        pass

# Function to save passwords to a text file
def save_passwords():
    with open("passwords.txt", "a") as file:
        file.write(password_listbox.get(0, tk.END)[0] + "\n")

# Function to search passwords by website name
def search_passwords():
    search_query = search_entry.get().lower()
    password_listbox.delete(0, tk.END)  # Clear the current password list

    try:
        with open("passwords.txt", "r") as file:
            for line in file:
                if search_query in line.lower():
                    password_listbox.insert(tk.END, line.strip())
    except FileNotFoundError:
        pass

# Create a Tkinter window
root = tk.Tk()
root.title("Password Manager")

# Create labels and entry fields with increased font size
font_size = 22  # Reduced the font size for better readability

website_label = tk.Label(root, text="Website:", font=("Helvetica", font_size))
website_label.pack(pady=5)

website_entry = tk.Entry(root, font=("Helvetica", font_size))
website_entry.pack(pady=5)

username_label = tk.Label(root, text="Username:", font=("Helvetica", font_size))
username_label.pack(pady=5)

username_entry = tk.Entry(root, font=("Helvetica", font_size))
username_entry.pack(pady=5)

password_label = tk.Label(root, text="Password:", font=("Helvetica", font_size))
password_label.pack(pady=5)

password_entry = tk.Entry(root, show="*", font=("Helvetica", font_size))  # Show asterisks for password input
password_entry.pack(pady=5)

# Create buttons
generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=("Helvetica", font_size))
generate_button.pack(pady=10)

add_button = tk.Button(root, text="Add Password", command=add_password , font=("Helvetica", font_size))
add_button.pack(pady=5)

load_button = tk.Button(root, text="Load Passwords", command=load_passwords, font=("Helvetica", font_size))
load_button.pack(pady=5)

# Create a search entry field and button
search_entry = tk.Entry(root, font=("Helvetica", font_size))
search_entry.pack(pady=5)
search_button = tk.Button(root, text="🔍 Search by Website", command=search_passwords)
search_button.pack(pady=5)

# Create a Listbox
password_listbox = tk.Listbox(root, font=("Helvetica", font_size), selectbackground="lightblue", selectmode=tk.SINGLE)
password_listbox.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
