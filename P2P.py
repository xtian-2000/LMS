import tkinter as tk
from datetime import datetime
from tkinter import ttk, END, messagebox
from databaseController import Database
import mysql.connector as mysql
from contentController import Content

# Global variables for database
host = "localhost"
user = "PongoDev"
password = "PongoDev44966874"


class Window:

    def __init__(self, master):
        # Instance attributes define within init scope conforming to PEP standards
        self.master = master
        self.login_username_entry = None
        self.login_password_entry = None
        self.register_b = None
        self.login_b = None
        self.register_top = None
        self.register_user_name_entry = None
        self.register_password_entry = None
        self.register_email_entry = None
        self.register_done_b = None
        self.menu_lf = None
        self.home_b = None
        self.loan_b = None
        self.profile_b = None
        self.content_lf = None
        self.home_lf = None
        self.home_dashboard_lf = None
        self.loan_lf = None
        self.profile_lf = None
        self.profile_buttons_lf = None
        self.add_people_b = None
        self.add_people_top = None
        self.add_people_name_entry = None
        self.add_people_address_entry = None
        self.age_spinbox = None
        self.gender_combobox = None
        self.finish_add_people_b = None
        self.success_add_people_message = None

        # Instantiate Database class
        Database()

        # Instantiate login window
        self.login_win()

    def login_win(self):
        # Create window attribute
        self.master.title("Login")
        self.master.geometry("500x250")
        self.master.resizable(False, False)
        self.master.configure(bg="#FFFFFF")

        # Login widgets
        ttk.Label(self.master, text="Login").grid(column=0, row=0)
        ttk.Label(self.master, text="User Name").grid(column=0, row=1)

        self.login_username_entry = ttk.Entry(self.master, width=50)
        self.login_username_entry.grid(column=1, row=1)

        ttk.Label(self.master, text="Password").grid(column=0, row=2)

        self.login_password_entry = ttk.Entry(self.master, width=50)
        self.login_password_entry.grid(column=1, row=2)

        self.register_b = tk.Button(self.master, text="Register", font="Arial, 15", relief="flat",
                                    command=self.register_win)
        self.register_b.grid(column=0, row=3)

        self.login_b = tk.Button(self.master, text="Login", font="Arial, 15", relief="flat",
                                 command=self.login_validation)
        self.login_b.grid(column=1, row=3)
        # color =

        Content.background_change_label(self.master, "#FFFFFF")
        Content.background_change_button(self.master, "#FFFFFF")

    def register_win(self):
        # Destroy window content
        Content.destroy_content(self.master)

        # Change window attribute
        self.master.title("Register")
        self.master.geometry("500x500")
        self.master.resizable(False, False)
        self.master.configure(bg="#FFFFFF")

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
        self.register_done_b = tk.Button(self.master, text="Done", font="Arial, 15", relief="flat",
                                         command=self.register_validation)
        self.register_done_b.grid(column=0, row=4)

        self.register_user_name_entry.focus()

        Content.background_change_label(self.master, "#FFFFFF")
        Content.background_change_button(self.master, "#FFFFFF")

    def login_validation(self):
        try:
            db1 = mysql.connect(host=host,
                                user=user,
                                password=password,
                                database="lmsdatabase")
            print("Connected to lmsdatabase")
            mycursor = db1.cursor()
            mycursor.execute(
                "SELECT * FROM user where username = '" + self.login_username_entry.get() + "' and password = '" +
                self.login_password_entry.get() + "';")
            myresult = mycursor.fetchone()
            if myresult is None:
                messagebox.showerror("Error", "Invalid User Name And Password")
            else:
                self.create_widgets()

            db1.close()
            mycursor.close()
        except Exception as e:
            print("Could not connect to lmsdatabase")
            print(e)

    def register_validation(self):
        try:
            db1 = mysql.connect(host=host,
                                user=user,
                                password=password,
                                database="lmsdatabase")
            print("Connected to lmsdatabase")
            mycursor = db1.cursor()
            mycursor.execute("INSERT INTO user (username, password, email) VALUES (%s,%s,%s)",
                             (self.register_user_name_entry.get(), self.register_password_entry.get(),
                              self.register_email_entry.get()))
            db1.commit()
            db1.close()
            mycursor.close()
        except Exception as e:
            print("Could not connect to lmsdatabase")
            print(e)

        self.login_win()
        Content.delete_entry(self.master)

    def create_widgets(self):
        # Destroy window contents
        Content.destroy_content(self.master)

        # Change window attribute
        self.master.title("P2P Lending Management System")
        width = self.master.winfo_screenwidth()
        height = self.master.winfo_screenheight()
        self.master.geometry("%dx%d" % (width, height))
        self.master.resizable(True, True)
        self.master.configure(bg="#FFFFFF")

        # Menu container
        self.menu_lf = tk.LabelFrame(self.master, bg="#FFFFFF")
        self.menu_lf.pack(side="left", fill="both")

        # Menu buttons
        self.home_b = tk.Button(self.menu_lf, text="Home", bg="#FFFFFF", font="Arial, 20", relief="flat",
                                command=self.switch_home)
        self.home_b.pack(side="top", padx=5, pady=5)

        self.loan_b = tk.Button(self.menu_lf, text="Loans", bg="#FFFFFF", font="Arial, 20", relief="flat",
                                command=self.switch_loan)
        self.loan_b.pack(side="top", padx=5)

        self.profile_b = tk.Button(self.menu_lf, text="Profile", bg="#FFFFFF", font="Arial, 20", relief="flat",
                                   command=self.switch_profile)
        self.profile_b.pack(side="top", padx=5, pady=5)

        # Contents container
        self.content_lf = tk.LabelFrame(self.master, bg="#FFFFFF")
        self.content_lf.pack(side="left", fill="both", expand="true")

        # Home container
        self.home_lf = tk.LabelFrame(self.content_lf, bg="#FFFFFF")
        self.home_lf.grid(column=0, row=0)

        # Dashboard container
        self.home_dashboard_lf = tk.LabelFrame(self.home_lf, bg="#FFFFFF")
        self.home_dashboard_lf.pack(side="top")

        ttk.Label(self.home_dashboard_lf, text="Dashboard", background="#FFFFFF").pack(side="top")

    def switch_home(self):
        # Destroy content_lf
        Content.destroy_content(self.content_lf)

        # Home container
        self.home_lf = tk.LabelFrame(self.content_lf, bg="#FFFFFF")
        self.home_lf.grid(column=0, row=0)

        # Home dashboard container
        self.home_dashboard_lf = tk.LabelFrame(self.home_lf, bg="#FFFFFF")
        self.home_dashboard_lf.pack(side="top")

        ttk.Label(self.home_dashboard_lf, text="Dashboard", background="#FFFFFF").pack(side="top")

    def switch_loan(self):
        # Destroy content_lf
        Content.destroy_content(self.content_lf)

        # Loan container
        self.loan_lf = tk.LabelFrame(self.content_lf, bg="#FFFFFF")
        self.loan_lf.grid(column=0, row=0)

        ttk.Label(self.loan_lf, text="Loans", background="#FFFFFF").pack(side="top")

    def switch_profile(self):
        # Destroy content_lf
        Content.destroy_content(self.content_lf)

        # Profile container
        self.profile_lf = tk.LabelFrame(self.content_lf, bg="#FFFFFF")
        self.profile_lf.grid(column=0, row=0)

        ttk.Label(self.profile_lf, text="Profile", background="#FFFFFF").pack(side="top")

        # Profile Button Container
        self.profile_buttons_lf = tk.LabelFrame(self.profile_lf, bg="#FFFFFF")
        self.profile_buttons_lf.pack(side="top")

        self.add_people_b = tk.Button(self.profile_buttons_lf, text="add people", command=self.add_people)
        self.add_people_b.pack(side="top")

    def add_people(self):
        # Create instance
        self.add_people_top = tk.Toplevel()
        self.add_people_top.geometry("500x500")
        self.add_people_top.title("Add people")

        # Creating widgets
        ttk.Label(self.add_people_top, text="Borrower's Profile").grid(column=0, row=0)
        ttk.Label(self.add_people_top, text="Name").grid(column=0, row=1)

        self.add_people_name_entry = ttk.Entry(self.add_people_top, width=50)
        self.add_people_name_entry.grid(column=1, row=1)

        ttk.Label(self.add_people_top, text="Address").grid(column=0, row=2)

        self.add_people_address_entry = ttk.Entry(self.add_people_top, width=50)
        self.add_people_address_entry.grid(column=1, row=2)

        ttk.Label(self.add_people_top, text="Age").grid(column=0, row=3)

        self.age_spinbox = ttk.Spinbox(self.add_people_top, from_=0, to=200, width=5)
        self.age_spinbox.grid(column=1, row=3)

        # Combobox for gender

        ttk.Label(self.add_people_top, text="Gender").grid(column=0, row=4)
        self.gender_combobox = ttk.Combobox(self.add_people_top, width=10)
        self.gender_combobox['values'] = "Male", "Female", "Others"
        self.gender_combobox.grid(column=1, row=4)
        self.gender_combobox.current(0)

        # Button for adding people to database

        self.finish_add_people_b = ttk.Button(self.add_people_top, text="Add",
                                              command=self.finish_add_people)
        self.finish_add_people_b.grid(column=0, row=5)

        self.add_people_name_entry.focus()

        self.add_people_top.mainloop()

    def finish_add_people(self):
        try:
            db1 = mysql.connect(host=host,
                                user=user,
                                password=password,
                                database="lmsdatabase")
            print("Connected to lmsdatabase")
            mycursor = db1.cursor()
            mycursor.execute("INSERT INTO borrower (name, address, age, created, gender) VALUES (%s,%s,%s,%s,%s)",
                             (self.add_people_name_entry.get(), self.add_people_address_entry.get(),
                              self.age_spinbox.get(),
                              datetime.now(), self.gender_combobox.get()))
            db1.commit()
            self.add_people_name_entry.delete(0, END)
            db1.close()
            mycursor.close()
            # Show a messagebox for successfully adding people

            self.success_add_people_message = tk.Toplevel()
            self.success_add_people_message.geometry("200x100")

            ttk.Label(self.success_add_people_message, text="Successfully added borrower's profile!").pack()
            self.success_add_people_message.after(1000, self.success_add_people_message.destroy)
        except Exception as e:
            print("Could not connect to lmsdatabase")
            print(e)


win = tk.Tk()
initialize = Window(win)

win.mainloop()
