import tkinter as tk

def validate_login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "gi-ness":
        login_label.config(text="Login successful!")
    else:
        login_label.config(text="Invalid username or password")

root = tk.Tk()
root.geometry("300x200")
root.title("Login Form")

# create the username label and entry
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# create the password label and entry
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# create the login button
login_button = tk.Button(root, text="Login", command=validate_login)
login_button.pack()

# create the login status label
login_label = tk.Label(root, text="")
login_label.pack()

root.mainloop()
