import tkinter as tk
from tkinter import ttk
from contentController import Content


class Validate:

    def __init__(self):
        super().__init__(self)
        self.login_username_entry = None
        self.login_password_entry = None
        self.register_b = None
        self.login_b = None
        self.register_user_name_entry = None
        self.register_password_entry = None
        self.register_email_entry = None
        self.register_done_b = None

    def login_win(self, master=tk.Tk()):
        # Create window attribute
        master.title("Login")
        master.geometry("500x250")
        master.resizable(False, False)
        master.configure(bg="#FFFFFF")

        # Login widgets
        ttk.Label(master, text="Login", background="#FFFFFF").grid(column=0, row=0)
        ttk.Label(master, text="User Name", background="#FFFFFF").grid(column=0, row=1)

        self.login_username_entry = ttk.Entry(master, width=50)
        self.login_username_entry.grid(column=1, row=1)

        ttk.Label(master, text="Password", background="#FFFFFF").grid(column=0, row=2)

        self.login_password_entry = ttk.Entry(master, width=50)
        self.login_password_entry.grid(column=1, row=2)
 
        self.register_b = tk.Button(master, text="Register", bg="#FFFFFF", font="Arial, 15", relief="flat",
                                    command=self.register_win(master))
        self.register_b.grid(column=0, row=3)

        self.login_b = tk.Button(master, text="Login", bg="#FFFFFF", font="Arial, 15", relief="flat")
        self.login_b.grid(column=1, row=3)

        # Content.destroy_content(win)

    def register_win(self, master=tk.Tk()):
        # Change window attribute
        master.title("Register")
        master.geometry("500x500")
        master.resizable(False, False)
        master.configure(bg="#FFFFFF")

        # Destroy window content
        # Content.destroy_content(self.master)

        # Creating widgets
        ttk.Label(master, text="Register").grid(column=0, row=0)
        ttk.Label(master, text="User Name").grid(column=0, row=1)

        self.register_user_name_entry = ttk.Entry(master, width=50)
        self.register_user_name_entry.grid(column=1, row=1)

        ttk.Label(master, text="Password").grid(column=0, row=2)

        self.register_password_entry = ttk.Entry(master, width=50)
        self.register_password_entry.grid(column=1, row=2)

        ttk.Label(master, text="Email").grid(column=0, row=3)

        self.register_email_entry = ttk.Entry(master, width=50)
        self.register_email_entry.grid(column=1, row=3)

        # Button for adding people to database
        self.register_done_b = ttk.Button(master, text="Done")
        self.register_done_b.grid(column=0, row=4)

        self.register_user_name_entry.focus()
