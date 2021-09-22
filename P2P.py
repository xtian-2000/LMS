import tkinter as tk
from datetime import datetime
from tkinter import ttk, messagebox
from databaseController import Database
import mysql.connector as mysql
from contentController import Content
import functools

# import numpy as np
# import matplotlib.pyplot as plt

# Global variables for database
host = "localhost"
user = "PongoDev"
password = "PongoDev44966874"


class Window:

    def __init__(self, master):
        # Instance attributes define within init scope conforming to PEP standards
        self.master = master
        self.login_lf, self.login_l, self.login_username_entry, self.login_password_entry = None, None, None, None
        self.register_lf, self.register_b, self.register_cancel_b, self.login_b = ttk.LabelFrame, None, None, None
        self.key, self.key_str = None, None
        self.register_top, self.register_user_name_entry, self.register_password_entry, self.\
            register_email_entry, self.register_done_b = None, None, None, None, None
        self.menu_lf, self.home_b, self.loan_b, self.account_b, self.body_lf, self.\
            toolbar_lf, self.logout_b = None, tk.Button, tk.Button, tk.Button, None, None, None
        self.content_lf, self.home_lf, self.home_dashboard_lf, self.loan_lf, self.\
            loans_menu_lf, self.account_lf = None, None, None, None, None, None
        self.account_database_view_f, self.account_database_view_scr, self.account_buttons_lf, self.\
            account_database_view_lf, self.account_content_view_lf, self.account_content_name_e, self.\
            account_content_address_e, self.account_content_age_e, self.account_content_gender_e, self.\
            delete_account_b, self.save_account_b = None, None, None, None, None, None, None, None, None, None, None
        self.account_borrower_header = None
        self.account_borrower_lb = ttk.Treeview
        self.add_people_b = None
        self.add_people_top = None
        self.add_people_lf = None
        self.add_people_name_entry = None
        self.add_people_address_entry = None
        self.age_spinbox = None
        self.gender_combobox = None
        self.finish_add_people_b = None
        self.cancel_add_people_b = None
        self.success_add_people_message = None
        self.db1, self.mycursor = None, None

        # Instantiate Database class
        Database()

        # Instantiate login window
        self.login_win()

        # Initialize class for default styles
        Content.widget_styles(self.master)

    def login_win(self):
        # Destroy window contents
        Content.destroy_content(self.master)

        # Create window attribute
        self.master.title("P2P Lending Management System")
        width = self.master.winfo_screenwidth()
        height = self.master.winfo_screenheight()
        self.master.geometry("%dx%d" % (width, height))
        self.master.resizable(True, True)
        self.master.configure(bg="#4C8404")

        # Login container
        self.login_lf = tk.LabelFrame(self.master, padx=20, pady=20, relief="flat")
        self.login_lf.pack(anchor="center", expand=True)

        # Login widgets
        ttk.Label(self.login_lf, text="Log in", style="h1.TLabel").grid(column=0, row=0, pady=10)

        ttk.Label(self.login_lf, text="User Name", style="h3.TLabel").grid(column=0, row=1, pady=10, sticky="w")

        self.login_username_entry = ttk.Entry(self.login_lf, width=40)
        self.login_username_entry.grid(column=1, row=1, pady=10)

        # Focuses cursor on username entry
        self.login_username_entry.focus()

        ttk.Label(self.login_lf, text="Password", style="h3.TLabel").grid(column=0, row=2, pady=10, sticky="w")

        self.login_password_entry = ttk.Entry(self.login_lf, show="*", width=40)
        self.login_password_entry.grid(column=1, row=2, pady=10)

        self.register_b = tk.Button(self.login_lf, text="                              Register                        "
                                                        "       ", font="OpenSans, 12", fg="#4C8404", bg="#FFFFFF",
                                    relief="flat", command=self.register_win)
        self.register_b.grid(column=0, row=3, columnspan=2, pady=10)

        self.login_b = tk.Button(self.login_lf, text="                                Log in                           "
                                                     "      ", font="OpenSans, 12", fg="#FFFFFF", bg="#4C8404",
                                 relief="flat", command=self.login_validation)
        self.login_b.grid(column=0, row=4, columnspan=2, pady=10)

        Content.background_change_labelframe(self.master, "#EBEBEB")
        Content.background_change_label(self.login_lf, "#EBEBEB")

    def register_win(self):
        # Destroy window content
        Content.destroy_content(self.master)

        # Register container
        self.register_lf = tk.LabelFrame(self.master, padx=20, pady=20, relief="flat")
        self.register_lf.pack(anchor="center", expand=True)

        # Creating widgets
        ttk.Label(self.register_lf, text="Register", style="h1.TLabel").grid(column=0, row=0, columnspan=1, pady=10)

        ttk.Label(self.register_lf, text="User Name", style="h3.TLabel").grid(column=0, row=1, pady=10, sticky="w")

        self.register_user_name_entry = ttk.Entry(self.register_lf, width=40)
        self.register_user_name_entry.grid(column=1, row=1, pady=10)

        # Focuses cursor on username entry
        self.register_user_name_entry.focus()

        ttk.Label(self.register_lf, text="Password", style="h3.TLabel").grid(column=0, row=2, pady=10, sticky="w")

        self.register_password_entry = ttk.Entry(self.register_lf, width=40)
        self.register_password_entry.grid(column=1, row=2, pady=10)

        ttk.Label(self.register_lf, text="Email", style="h3.TLabel").grid(column=0, row=3, pady=10, sticky="w")

        self.register_email_entry = ttk.Entry(self.register_lf, width=40)
        self.register_email_entry.grid(column=1, row=3, pady=10)

        # Button for cancelling registration
        self.register_cancel_b = tk.Button(self.register_lf, text="                                Cancel              "
                                                                  "                   ", font="OpenSans, 12",
                                           relief="flat", fg="#4C8404", bg="#FFFFFF", command=self.login_win)
        self.register_cancel_b.grid(column=0, row=4, columnspan=2, pady=10)

        # Button for adding people to database
        self.register_done_b = tk.Button(self.register_lf, text="                               Register               "
                                                                "                 ", font="OpenSans, 12", relief="flat",
                                         fg="#FFFFFF", bg="#4C8404", command=self.register_validation)
        self.register_done_b.grid(column=0, row=5, columnspan=2, pady=10)

        Content.background_change_labelframe(self.master, "#EBEBEB")

        Content.background_change_label(self.register_lf, "#EBEBEB")

    def create_widgets(self):
        # Destroy window contents
        Content.destroy_content(self.master)

        # Menu container
        self.menu_lf = tk.LabelFrame(self.master, bg="#2C441D", relief="flat")
        self.menu_lf.pack(side="left", fill="both")

        # Menu buttons
        self.home_b = tk.Button(self.menu_lf, text="Home", font="OpenSans 18", relief="flat", bg="#2C441D",
                                fg="#FFFFFF", anchor="w", command=self.switch_home)
        self.home_b.pack(side="top", fill="both")

        self.loan_b = tk.Button(self.menu_lf, text="Loans", font="OpenSans, 18", relief="flat", bg="#2C441D",
                                fg="#FFFFFF", anchor="w", command=self.switch_loan)
        self.loan_b.pack(side="top", fill="both")

        self.account_b = tk.Button(self.menu_lf, text="Accounts", font="OpenSans, 18", relief="flat", bg="#2C441D",
                                   fg="#FFFFFF", anchor="w", command=self.switch_account)
        self.account_b.pack(side="top", fill="both")

        # Content Container
        self.body_lf = tk.LabelFrame(self.master, relief="flat")
        self.body_lf.pack(side="left", fill="both", expand="true")

        # Toolbar Button Container
        self.toolbar_lf = tk.LabelFrame(self.body_lf, bg="#FFFFFF", relief="flat")
        self.toolbar_lf.pack(side="top", fill="x")

        # Button for opening form for adding borrower
        self.add_people_b = tk.Button(self.toolbar_lf, text="Add people", font="OpenSans, 10", fg="#FFFFFF",
                                      bg="#4C8404", relief="flat", command=self.add_people)
        self.add_people_b.pack(side="left", padx=5, pady=5)

        self.logout_b = tk.Button(self.toolbar_lf, text="Logout", font="OpenSans, 10", relief="flat", bg="#FFFFFF",
                                  fg="green", highlightcolor="#2C441D", command=self.login_win)
        self.logout_b.pack(side="right", padx=100, pady=5)

        # Contents container
        self.content_lf = tk.LabelFrame(self.body_lf, relief="flat")
        self.content_lf.pack(side="left", fill="both", expand="true")

        # Initialize switch_home method for the default content
        self.switch_home()

    def switch_home(self):
        # Destroy content_lf
        Content.destroy_content(self.content_lf)

        # Home container
        self.home_lf = tk.LabelFrame(self.content_lf, relief="flat")
        self.home_lf.pack(fill="both", expand=True)

        # Home dashboard container
        self.home_dashboard_lf = tk.LabelFrame(self.home_lf, bg="#FFFFFF", relief="flat")
        self.home_dashboard_lf.pack(side="top", fill="x")

        # Configure button state
        self.state_button(self.home_b, self.account_b, self.loan_b)

    def switch_loan(self):
        # Destroy content_lf
        Content.destroy_content(self.content_lf)

        # Loan container
        self.loan_lf = tk.LabelFrame(self.content_lf, relief="flat")
        self.loan_lf.pack(fill="both", expand=True)

        # Loan menu container
        self.loans_menu_lf = tk.LabelFrame(self.loan_lf, bg="#FFFFFF", relief="flat")
        self.loans_menu_lf.pack(side="top", fill="x")

        # Configure button state
        self.state_button(self.loan_b, self.account_b, self.home_b)

    def switch_account(self):
        # Destroy content_lf
        Content.destroy_content(self.content_lf)

        # Profile container
        self.account_lf = tk.LabelFrame(self.content_lf, relief="flat")
        self.account_lf.pack(fill="both", expand=True)

        # Profile view database container
        self.account_database_view_lf = tk.LabelFrame(self.account_lf, bg="#FFFFFF", relief="flat")
        self.account_database_view_lf.pack(side="top", pady=10, fill="both")

        # Profile view database frame
        self.account_database_view_f = tk.Frame(self.account_database_view_lf, relief="flat")
        self.account_database_view_f.pack(side="top", fill="both")

        self.account_database_view_scr = tk.Scrollbar(self.account_database_view_f)
        self.account_database_view_scr.pack(side="right", fill="y")

        # Create tree
        self.account_borrower_lb = ttk.Treeview(self.account_database_view_f, style="default.Treeview",
                                                yscrollcommand=self.account_database_view_scr.set)

        self.account_database_view_scr.configure(command=self.account_borrower_lb.yview)

        # Define column
        self.account_borrower_lb["columns"] = ("Name", "Address", "Age", "Gender")

        # Format column
        self.account_borrower_lb.column("#0", width=0, stretch="no")
        self.account_borrower_lb.column("Name", anchor="w", width=120)
        self.account_borrower_lb.column("Address", anchor="w", width=120)
        self.account_borrower_lb.column("Age", anchor="center", width=80)
        self.account_borrower_lb.column("Gender", anchor="center", width=80)

        # Create headings
        self.account_borrower_lb.heading("#0", text="", anchor="w")
        self.account_borrower_lb.heading("Name", text="Name", anchor="w")
        self.account_borrower_lb.heading("Address", text="Address", anchor="w")
        self.account_borrower_lb.heading("Age", text="Age", anchor="center")
        self.account_borrower_lb.heading("Gender", text="Gender", anchor="center")

        self.account_borrower_lb.pack(side="left", fill="both", expand=True)

        # Bind the treeview to database_view_info method
        self.account_borrower_lb.bind("<ButtonRelease-1>", self.database_view_account_info)

        # Initialize method for viewing accounts database
        self.database_view_account()

        # Profile view database container
        self.account_content_view_lf = tk.LabelFrame(self.account_lf, bg="#FFFFFF", relief="flat")
        self.account_content_view_lf.pack(side="top", pady=10, fill="both")

        ttk.Label(self.account_content_view_lf, text="Account Information",
                  style="heading.TLabel").grid(column=0, row=0, columnspan=2, pady=5, sticky="w")

        ttk.Label(self.account_content_view_lf, text="No information Available",
                  style="body.TLabel").grid(column=0, row=1, padx=5, pady=5, sticky="w")

        # Configure button state
        self.state_button(self.account_b, self.loan_b, self.home_b)

    def login_validation(self):
        try:
            self.database_connect()
            self.mycursor.execute(
                "SELECT * FROM user where username = '" + self.login_username_entry.get() + "' and password = '" +
                self.login_password_entry.get() + "';")
            myresult = self.mycursor.fetchone()
            if myresult is None:
                messagebox.showerror("Error", "Invalid User Name And Password")
            else:
                self.mycursor.execute(
                    "SELECT DISTINCT userid FROM user where username = '" + self.login_username_entry.get() + "';")

                # Converts the tuple into integer
                self.key = functools.reduce(lambda sub, ele: sub * 10 + ele, self.mycursor.fetchone())
                self.key_str = str(self.key)
                print(self.key_str)

                # Instantiate create_widgets method
                self.create_widgets()

            self.db1.close()
            self.mycursor.close()
        except Exception as e:
            print("Could not connect to lmsdatabase")
            print(e)

    def register_validation(self):
        try:
            self.database_connect()
            self.mycursor.execute("INSERT INTO user (username, password, email) VALUES (%s,%s,%s)",
                                  (self.register_user_name_entry.get(), self.register_password_entry.get(),
                                   self.register_email_entry.get()))
            self.db1.commit()
            self.db1.close()
            self.mycursor.close()

            # Destroy window contents
            Content.destroy_content(self.master)

            # Initializes login_win
            self.login_win()

        except Exception as e:
            print("Could not connect to lmsdatabase")
            print(e)
            # Deletes all entries from ttk.Entry
            Content.delete_entry(self.master)

    def add_people(self):
        # Create instance
        self.add_people_top = tk.Toplevel(self.master)
        self.add_people_top.geometry("500x280")
        self.add_people_top.title("Borrower's Profile")
        self.add_people_top.configure(bg="#4C8404")

        # Register container
        self.add_people_lf = tk.LabelFrame(self.add_people_top, padx=20, pady=20, relief="flat")
        self.add_people_lf.pack(anchor="center", expand=True)

        # Creating widgets
        ttk.Label(self.add_people_lf, text="Name", font="OpenSans, 10").grid(column=0, row=0, padx=5, pady=5,
                                                                             sticky="w")

        self.add_people_name_entry = ttk.Entry(self.add_people_lf, width=50)
        self.add_people_name_entry.grid(column=1, row=0, padx=5, pady=5, sticky="w")

        # Focuses cursor on add name entry
        self.add_people_name_entry.focus()

        ttk.Label(self.add_people_lf, text="Address", font="OpenSans, 10").grid(column=0, row=1, padx=5, pady=5,
                                                                                sticky="w")

        self.add_people_address_entry = ttk.Entry(self.add_people_lf, width=50)
        self.add_people_address_entry.grid(column=1, row=1, padx=5, pady=5, sticky="w")

        ttk.Label(self.add_people_lf, text="Age", font="OpenSans, 10").grid(column=0, row=2, padx=5, pady=5, sticky="w")

        self.age_spinbox = ttk.Spinbox(self.add_people_lf, from_=0, to=200, width=5)
        self.age_spinbox.grid(column=1, row=2, padx=5, pady=5, sticky="w")

        # Combobox for gender
        ttk.Label(self.add_people_lf, text="Gender", font="OpenSans, 10").grid(column=0, row=3, padx=5, pady=5,
                                                                               sticky="w")
        self.gender_combobox = ttk.Combobox(self.add_people_lf, width=10)
        self.gender_combobox['values'] = "Male", "Female", "Others"
        self.gender_combobox.grid(column=1, row=3, padx=5, pady=5, sticky="w")
        self.gender_combobox.current(0)

        # Button for adding people to database
        self.cancel_add_people_b = tk.Button(self.add_people_lf, text="Add Borrower", font="OpenSans, 12", fg="#FFFFFF",
                                             bg="#4C8404", relief="flat", command=self.finish_add_people)
        self.cancel_add_people_b.grid(column=0, row=4, padx=5, pady=5)

        # Button for adding people to database
        self.finish_add_people_b = tk.Button(self.add_people_lf, text="Cancel", font="OpenSans, 12", fg="#4C8404",
                                             bg="#FFFFFF", relief="flat", command=self.add_people_top.destroy)
        self.finish_add_people_b.grid(column=1, row=4, padx=5, pady=5, sticky="w")

        # Disables underlying window
        self.add_people_top.grab_set()

        self.add_people_top.mainloop()

    def finish_add_people(self):
        try:
            self.database_connect()
            self.mycursor.execute(
                "INSERT INTO borrower (userid, name, address, age, created, gender) VALUES (%s, %s,%s,"
                "%s,%s,%s)",
                (self.key, self.add_people_name_entry.get(), self.add_people_address_entry.get(),
                 self.age_spinbox.get(), datetime.now(), self.gender_combobox.get()))
            self.db1.commit()
            self.db1.close()
            self.mycursor.close()

            # Destroy add_people_top form
            self.add_people_top.destroy()

            # Show a messagebox for successfully adding people
            messagebox.showinfo("Borrower's Account", "Account added successfully")
        except Exception as e:
            # Deletes all entries from ttk.Entry
            Content.delete_entry(self.master)
            # Show a messagebox for unsuccessfully adding people
            messagebox.showerror("Borrower's Account", "Did not succeed in adding account")
            print("Could not connect to lmsdatabase")
            print(e)

    def database_connect(self):
        try:
            self.db1 = mysql.connect(host=host,
                                     user=user,
                                     password=password,
                                     database="lmsdatabase")
            print("Connected to lmsdatabase")
            self.mycursor = self.db1.cursor()
        except Exception as e:
            print("Could not connect to lmsdatabase")
            print(e)

    def database_view_account(self):
        # Method for viewing accounts database
        try:
            self.database_connect()
            self.mycursor.execute("SELECT name, address, age, gender FROM borrower where userid = '" + self.key_str +
                                  "';")
            borrowers = self.mycursor.fetchall()
            print(borrowers)

            # Create configure for striped rows
            self.account_borrower_lb.tag_configure("oddrow", background="#FFFFFF")
            self.account_borrower_lb.tag_configure("evenrow", background="#FAFAFA")
            count = 0
            for record in borrowers:
                if count % 2 == 0:
                    self.account_borrower_lb.insert(parent="", index="end", iid=count, text="",
                                                    values=(record[0], record[1], record[2], record[3]),
                                                    tags=("oddrow",))
                else:
                    self.account_borrower_lb.insert(parent="", index="end", iid=count, text="",
                                                    values=(record[0], record[1], record[2], record[3]),
                                                    tags=("evenrow",))
                count += 1

            self.db1.close()
        except Exception as e:
            print("Could not connect to lmsdatabase")
            print(e)

    def database_view_account_info(self, event):
        # Destroy content of account_content_view_lf
        Content.destroy_content(self.account_content_view_lf)

        # Create widgets for displaying account information
        ttk.Label(self.account_content_view_lf, text="Account Information",
                  style="heading.TLabel").grid(column=0, row=0, columnspan=2, pady=5, sticky="w")

        ttk.Label(self.account_content_view_lf, text="Name",
                  style="body.TLabel").grid(column=0, row=1, padx=5, pady=5, sticky="w")

        self.account_content_name_e = ttk.Entry(self.account_content_view_lf, width=40)
        self.account_content_name_e.grid(column=1, row=1, columnspan=2)

        ttk.Label(self.account_content_view_lf, text="Address",
                  style="body.TLabel").grid(column=0, row=2, padx=5, pady=5, sticky="w")

        self.account_content_address_e = ttk.Entry(self.account_content_view_lf, width=40)
        self.account_content_address_e.grid(column=1, row=2, columnspan=2)

        ttk.Label(self.account_content_view_lf, text="Age",
                  style="body.TLabel").grid(column=0, row=3, padx=5, pady=5, sticky="w")

        self.account_content_age_e = ttk.Entry(self.account_content_view_lf, width=40)
        self.account_content_age_e.grid(column=1, row=3, columnspan=2)

        ttk.Label(self.account_content_view_lf, text="Gender",
                  style="body.TLabel").grid(column=0, row=4, padx=5, pady=5, sticky="w")

        self.account_content_gender_e = ttk.Entry(self.account_content_view_lf, width=40)
        self.account_content_gender_e.grid(column=1, row=4, columnspan=2)

        # Grab record number
        selected = self.account_borrower_lb.focus()

        # Grab record values
        values = self.account_borrower_lb.item(selected, "values")

        # Insert values to entry widgets
        self.account_content_name_e.insert(0, values[0])
        self.account_content_address_e.insert(0, values[1])
        self.account_content_age_e.insert(0, values[2])
        self.account_content_gender_e.insert(0, values[3])

        # Button for opening form for adding borrower
        self.delete_account_b = tk.Button(self.account_content_view_lf, text="Delete Account", font="OpenSans, 10",
                                          fg="#FFFFFF", bg="#4C8404", relief="flat", command=self.add_people)
        self.delete_account_b.grid(column=0, row=5, padx=5, pady=5, sticky="w")

        # Button for opening form for adding borrower
        self.save_account_b = tk.Button(self.account_content_view_lf, text="Delete Account", font="OpenSans, 10",
                                        fg="#FFFFFF", bg="#4C8404", relief="flat", command=self.add_people)
        self.save_account_b.grid(column=1, row=5, padx=5, pady=5, sticky="w")

        print(event)

    @staticmethod
    def state_button(widget1, widget2, widget3):
        widget1.configure(bg="#4C8404")
        widget2.configure(bg="#2C441D")
        widget3.configure(bg="#2C441D")


win = tk.Tk()
initialize = Window(win)

win.mainloop()
