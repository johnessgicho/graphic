import tkinter as tk

def register_user():
    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()
    email = email_entry.get()

    # check if password matches confirm password
    if password != confirm_password:
        register_label.config(text="Passwords do not match")
    else:
        # register the user here
        # for example, print the user's details
        print("Username:", username)
        print("Password:", password)
        print("Email:", email)
        register_label.config(text="Registration successful!")

root = tk.Tk()
root.geometry("300x250")
root.title("Registration Form")

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

# create the confirm password label and entry
confirm_password_label = tk.Label(root, text="Confirm Password:")
confirm_password_label.pack()
confirm_password_entry = tk.Entry(root, show="*")
confirm_password_entry.pack()

# create the email label and entry
email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

# create the register button
register_button = tk.Button(root, text="Register", command=register_user)
register_button.pack()

# create the registration status label
register_label = tk.Label(root, text="")
register_label.pack()

root.mainloop()
