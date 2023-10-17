"""
New project

Date: 29/09/2023

Name of project: Login

Created by Sardordev
"""

from tkinter import *
from tkinter import messagebox
import re

root = Tk()
root.title("Login_Gui")  # Dastur nomi
root.geometry("515x420")
root.resizable(False, False)

frame1 = Frame(root, width=520, height=420, bg="#333")
frame1.place(x=0, y=0)

Label(root, text="Login", font=("Helvetica 50 bold"), bg="#333", fg="#fff").place(x=160, y=10)

def clear():
    username_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)

def is_valid_username(user):
    username_pattern = r"^[A-Za-z0-9_-]{3,15}$"
    return re.match(username_pattern, user) is not None

def is_valid_email(email):
    email_pattern = r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
    return re.match(email_pattern, email) is not None

def is_valid_password(password):
    # Parol andozalari:
    # 1. Kamida 8 belgi uzunligi
    # 2. Kamida bitta harf (katta yoki kichik)
    # 3. Kamida bitta raqam
    password_pattern = r"^(?=.*[A-Za-z])(?=.*\d).{8,}$"
    return re.match(password_pattern, password) is not None

def toggle_password():
    current_show_value = password_entry.cget("show")
    if current_show_value == "":
        password_entry.config(show="*")
        show_password_button.config(text="Show")
    else:
        password_entry.config(show="")
        show_password_button.config(text="Hide")


def login():
    user = username_entry.get()
    email_address = email_entry.get()
    password = password_entry.get()

    username_valid = is_valid_username(user)
    email_valid = is_valid_email(email_address)
    password_valid = is_valid_password(password)

    if username_valid and email_valid and password_valid:
        messagebox.showinfo("Success", f"Account created successfully!")
    else:
        error_messages = []
        if not username_valid:
            error_messages.append("Your username does not meet the requirements!")
        if not email_valid:
            error_messages.append("Your email does not meet the requirements!")
        if not password_valid:
            error_messages.append("Your password does not meet the requirements!")

        error_message = "\n".join(error_messages)
        messagebox.showerror("Error", error_message)


username_label = Label(frame1, text="Enter username:", font=("verdana", 14), bg="#333", fg="#fff")
username_label.place(x=47, y=95)

username_entry = Entry(frame1, width=34, font=("verdana", 14), relief=RAISED, borderwidth=3, fg="#333")
username_entry.place(x=50, y=140)

email_label = Label(frame1, text="Enter your email:", font=("verdana", 14), bg="#333", fg="#fff")
email_label.place(x=47, y=180)

email_entry = Entry(frame1, width=34, font=("verdana", 14), relief=RAISED, borderwidth=3, fg="#333")
email_entry.place(x=50, y=220)

password_label = Label(frame1, text="Enter password:", font=("verdana", 14),  bg="#333", fg="#fff")
password_label.place(x=47, y=260)

password_entry = Entry(frame1, width=30, font=("verdana", 14), fg="#333", relief=RAISED, borderwidth=3, show="*")
password_entry.place(x=50, y=300)

show_password_button = Button(frame1, text="Show", relief=RAISED, command=toggle_password, borderwidth=3, fg="#333", cursor="hand2")
show_password_button.place(x=425, y=300)

login_button = Button(root, text="Create an accaunt", width=51, relief=RAISED, command=login, borderwidth=3, fg="#333", cursor="hand2")
login_button.place(x=50, y=350)

clear_button = Button(root, text="Clear", relief=RAISED, command=clear, borderwidth=3, fg="#333", cursor="hand2")
clear_button.place(x=425, y=350)

root.mainloop()
