import tkinter as tk
from tkinter import ttk
from register import Register


class Login(tk.Tk):

    def __init__(self):
        super().__init__(self)
        self.login_username_entry = None
        self.login_password_entry = None
        self.register_b = None
        self.login_b = None

    def login_win(self):
        # Create window attribute
        self.title("Login")
        self.geometry("500x250")
        self.resizable(False, False)
        self.configure(bg="#FFFFFF")

        # Login widgets
        ttk.Label(self.master, text="Login", background="#FFFFFF").grid(column=0, row=0)
        ttk.Label(self.master, text="User Name", background="#FFFFFF").grid(column=0, row=1)

        self.login_username_entry = ttk.Entry(self.master, width=50)
        self.login_username_entry.grid(column=1, row=1)

        ttk.Label(self.master, text="Password", background="#FFFFFF").grid(column=0, row=2)

        self.login_password_entry = ttk.Entry(self.master, width=50)
        self.login_password_entry.grid(column=1, row=2)

        self.register_b = tk.Button(self.master, text="Register", bg="#FFFFFF", font="Arial, 15", relief="flat",
                                    command=Register.register_win)
        self.register_b.grid(column=0, row=3)

        self.login_b = tk.Button(self.master, text="Login", bg="#FFFFFF", font="Arial, 15", relief="flat")
        self.login_b.grid(column=1, row=3)


