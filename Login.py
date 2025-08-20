import tkinter as tk
from tkinter import messagebox
import sqlite3
import os
def validate_login():
    username = entry_username.get()
    password = entry_password.get()
    
    conn = sqlite3.connect("user_credentials.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()

    if user:
        messagebox.showinfo("Login Successful", "Welcome, " + username)
        os.startfile("dashboard.py")
        quit()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")
    
    conn.close()

# Create the main window
root = tk.Tk()
#root.configure(bg='blue')

root.geometry("550x400+365+160")
root.title("Login Page")

# Create labels and entry widgets for username and password
#frame = tk.Frame(root, bg='white', padx=20, pady=20)
#frame.configure(bg = "blue")
#frame.pack(expand=False, fill=tk.BOTH)
label_username = tk.Label(root, text="Username",font=("times new roman", 20, "bold"),bg="#5d636d",fg="white")
label_username.place(x=25,y=75,width = 225, height = 50)

entry_username = tk.Entry(root,font=("times new roman", 20, "bold"),bg="#5d636d",fg="white")
entry_username.place(x=275,y=75,width = 225, height = 50)

label_password = tk.Label(root, text="Password",font=("times new roman", 20, "bold"),bg="#5d636d",fg="white")
label_password.place(x=25,y=150,width = 225, height = 50)

entry_password = tk.Entry(root, show="*",font=("times new roman", 20, "bold"),bg="#5d636d",fg="white")
entry_password.place(x=275,y=150,width = 225, height = 50)

# Create a login button
login_button = tk.Button(root, text="Login", command=validate_login,font=("times new roman", 20, "bold"),bg="#5d636d",fg="white",cursor="hand2")
login_button.place(x=175,y=250,width = 225, height = 50)

# Run the application
root.mainloop()
