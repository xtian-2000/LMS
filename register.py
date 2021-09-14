import tkinter as tk
from tkinter import ttk
from contentController import Content


class Register(tk.Tk):

    def __init__(self):
        super().__init__(self)
        self.register_user_name_entry = None
        self.register_password_entry = None
        self.register_email_entry = None
        self.register_done_b = None

    def register_win(self):
        # Change window attribute
        self.title("Register")
        self.geometry("500x500")
        self.resizable(False, False)
        self.configure(bg="#FFFFFF")

        # Destroy window content
        Content.destroy_content(self.master)

        # Creating widgets
        ttk.Label(self.master, text="Register").grid(column=0, row=0)
        ttk.Label(self.master, text="User Name").grid(column=0, row=1)

        self.register_user_name_entry = ttk.Entry(self.master, width=50)
        self.register_user_name_entry.grid(column=1, row=1)

        ttk.Label(self.master, text="Password").grid(column=0, row=2)

        self.register_password_entry = ttk.Entry(self.master, width=50)
        self.register_password_entry.grid(column=1, row=2)

        ttk.Label(self.master, text="Email").grid(column=0, row=3)

        self.register_email_entry = ttk.Entry(self.master, width=50)
        self.register_email_entry.grid(column=1, row=3)

        # Button for adding people to database
        self.register_done_b = ttk.Button(self.master, text="Done")
        self.register_done_b.grid(column=0, row=4)

        self.register_user_name_entry.focus()

