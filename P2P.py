import tkinter as tk
from datetime import datetime
from tkinter import ttk, messagebox
from databaseController import Database
import mysql.connector as mysql
from contentController import Content
import functools
from PIL import ImageTk, Image
from tkcalendar import DateEntry

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
        self.logo_lf = None
        self.login_lf = None
        self.login_l = None
        self.login_username_entry = None
        self.login_password_entry = None
        self.register_lf = None
        self.register_b = None
        self.register_cancel_b = None
        self.login_b = None
        self.key = None
        self.key_str = None
        self.register_top = None
        self.register_user_name_entry = None
        self.register_password_entry = None
        self.register_email_entry = None
        self.register_done_b = None
        self.menu_lf = None
        self.home_b = tk.Button
        self.loan_b = tk.Button
        self.account_b = tk.Button
        self.body_lf = None
        self.toolbar_lf = None
        self.logout_b = tk.Button
        self.content_lf = None
        self.home_lf = None
        self.home_dashboard_lf = None
        self.loan_lf = None
        self.loan_database_view_lf = None
        self.loan_dashboard_lf = None
        self.loan_database_view_f = None
        self.loan_database_view_scr = None
        self.loan_borrower_lb = None
        self.loan_content_view_lf = None
        self.issue_loan_date_de = None
        self.status_combobox = None
        self.account_lf = None
        self.account_database_view_f = None
        self.account_database_view_scr = None
        self.account_buttons_lf = None
        self.account_database_view_lf = None
        self.account_content_view_lf = None
        self.borrower_id = None
        self.account_content_name_e = None
        self.account_content_address_e = None
        self.account_content_age_e = None
        self.account_content_gender_e = None
        self.delete_account_b = None
        self.save_account_b = None
        self.issue_loan_b = None
        self.total_loan_l = None
        self.issue_loan_top = None
        self.issue_loan_lf = None
        self.issue_loan_amount_sb = None
        self.issue_loan_interest_sb = None
        self.issue_loan_days_sb = None
        self.cancel_issue_loan_b = None
        self.finish_issue_loan_b = None
        self.loan_id = None
        self.loan_content_name_l = None
        self.loan_content_amount_e = None
        self.loan_content_interest_e = None
        self.loan_content_interest_pd_e = None
        self.loan_content_date_issued_cal = None
        self.loan_content_status_cb = None
        self.loan_content_date_issued_str = None
        self.delete_loan_b = None
        self.save_loan_b = None
        self.register_payment_b = None
        self.account_borrower_header = None
        self.account_borrower_lb = ttk.Treeview
        self.borrower_key = None
        self.borrower_key_str = None
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
        self.db1 = None
        self.mycursor = None
        self.count = None
        self.year = datetime.today().year
        self.month = datetime.today().month
        self.day = datetime.today().day

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
        self.master.iconbitmap(r"C:\Users\SSD\IdeaProjects\LMS\p2p_official_logo.ico")
        width = self.master.winfo_screenwidth()
        height = self.master.winfo_screenheight()
        self.master.geometry("%dx%d" % (width, height))
        self.master.resizable(True, True)
        self.master.configure(bg="#4C8404")

        # Logo container
        self.logo_lf = tk.LabelFrame(self.master, padx=20, pady=20, relief="flat")
        self.logo_lf.pack(side="left", expand=True, fill="both")

        my_image = ImageTk.PhotoImage(Image.open("P2P_official_logo.png"))
        my_label = ttk.Label(self.logo_lf, image=my_image)
        my_label.pack()

        # Login container
        self.login_lf = tk.LabelFrame(self.master, padx=20, pady=20, relief="flat")
        self.login_lf.pack(side="right", expand=True)

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
        self.add_people_b = tk.Button(self.toolbar_lf, text="Add borrower", font="OpenSans, 10", fg="#FFFFFF",
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
        self.home_dashboard_lf.pack(side="top", fill="both")

        ttk.Label(self.home_dashboard_lf, text="Analytics Dashboard",
                  style="heading.TLabel").grid(column=0, row=0, columnspan=2, pady=5, sticky="w")

        ttk.Label(self.home_dashboard_lf, text="This section is under development",
                  style="body.TLabel").grid(column=0, row=1, padx=5, pady=5, sticky="w")

        # Configure button state
        self.state_button(self.home_b, self.account_b, self.loan_b)

    def switch_loan(self):
        # Destroy content_lf
        Content.destroy_content(self.content_lf)

        # Loan container
        self.loan_lf = tk.LabelFrame(self.content_lf, relief="flat")
        self.loan_lf.pack(fill="both", expand=True)

        # Loan view database container
        self.loan_database_view_lf = tk.LabelFrame(self.loan_lf, bg="#FFFFFF", relief="flat")
        self.loan_database_view_lf.pack(side="top", pady=10, fill="both")

        # Loan view database frame
        self.loan_database_view_f = tk.Frame(self.loan_database_view_lf, relief="flat")
        self.loan_database_view_f.pack(side="top", fill="both")

        self.loan_database_view_scr = tk.Scrollbar(self.loan_database_view_f)
        self.loan_database_view_scr.pack(side="right", fill="y")

        # Create tree
        self.loan_borrower_lb = ttk.Treeview(self.loan_database_view_f, style="default.Treeview",
                                             yscrollcommand=self.loan_database_view_scr.set)

        self.loan_database_view_scr.configure(command=self.loan_borrower_lb.yview)

        # Define column
        self.loan_borrower_lb["columns"] = ("Loan ID", "Name", "Amount", "Interest", "(n) days", "Date issued",
                                            "Status")

        # Format column
        self.loan_borrower_lb.column("#0", width=0, stretch="no")
        self.loan_borrower_lb.column("Loan ID", anchor="center", width=50)
        self.loan_borrower_lb.column("Name", anchor="w", width=80)
        self.loan_borrower_lb.column("Amount", anchor="center", width=50)
        self.loan_borrower_lb.column("Interest", anchor="center", width=50)
        self.loan_borrower_lb.column("(n) days", anchor="center", width=50)
        self.loan_borrower_lb.column("Date issued", anchor="center", width=50)
        self.loan_borrower_lb.column("Status", anchor="center", width=50)

        # Create headings
        self.loan_borrower_lb.heading("#0", text="", anchor="w")
        self.loan_borrower_lb.heading("Loan ID", text="Loan ID", anchor="center")
        self.loan_borrower_lb.heading("Name", text="Name", anchor="w")
        self.loan_borrower_lb.heading("Amount", text="Amount", anchor="center")
        self.loan_borrower_lb.heading("Interest", text="Interest (%)", anchor="center")
        self.loan_borrower_lb.heading("(n) days", text="interest per (n) days", anchor="center")
        self.loan_borrower_lb.heading("Date issued", text="Date issued", anchor="center")
        self.loan_borrower_lb.heading("Status", text="Status", anchor="center")

        self.loan_borrower_lb.pack(side="left", fill="both", expand=True)

        # Bind the treeview to database_view_info method
        self.loan_borrower_lb.bind("<ButtonRelease-1>", self.database_view_loan_info)

        # Initialize method for viewing accounts database
        self.database_view_loan()

        # Profile view database container
        self.loan_content_view_lf = tk.LabelFrame(self.loan_lf, bg="#FFFFFF", relief="flat")
        self.loan_content_view_lf.pack(side="top", pady=10, fill="both")

        ttk.Label(self.loan_content_view_lf, text="Loan Information",
                  style="heading.TLabel").grid(column=0, row=0, columnspan=2, pady=5, sticky="w")

        ttk.Label(self.loan_content_view_lf, text="No information available",
                  style="body.TLabel").grid(column=0, row=1, padx=5, pady=5, sticky="w")

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

        ttk.Label(self.account_content_view_lf, text="No information available",
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
        # self.add_people_top.geometry("500x280")
        self.add_people_top.title("Borrower's Profile")
        self.add_people_top.configure(bg="#4C8404")

        self.add_people_widget()

        # Disables underlying window
        self.add_people_top.grab_set()

        self.add_people_top.mainloop()

    def add_people_widget(self):
        # Register container
        self.add_people_lf = tk.LabelFrame(self.add_people_top, padx=20, pady=20, relief="flat")
        self.add_people_lf.pack(anchor="center", expand=True, fill="both")

        # Creating widgets
        ttk.Label(self.add_people_lf, text="Name", style="h3.TLabel").grid(column=0, row=0, padx=5, pady=5,
                                                                           sticky="w")

        self.add_people_name_entry = ttk.Entry(self.add_people_lf, width=50)
        self.add_people_name_entry.grid(column=1, row=0, padx=5, pady=5, sticky="w")

        # Focuses cursor on add name entry
        self.add_people_name_entry.focus()

        ttk.Label(self.add_people_lf, text="Address", style="h3.TLabel").grid(column=0, row=1, padx=5, pady=5,
                                                                              sticky="w")

        self.add_people_address_entry = ttk.Entry(self.add_people_lf, width=50)
        self.add_people_address_entry.grid(column=1, row=1, padx=5, pady=5, sticky="w")

        ttk.Label(self.add_people_lf, text="Age", style="h3.TLabel").grid(column=0, row=2, padx=5, pady=5, sticky="w")

        self.age_spinbox = ttk.Spinbox(self.add_people_lf, from_=0, to=200, width=5)
        self.age_spinbox.grid(column=1, row=2, padx=5, pady=5, sticky="w")

        # Combobox for gender
        ttk.Label(self.add_people_lf, text="Gender", style="h3.TLabel").grid(column=0, row=3, padx=5, pady=5,
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

    def issue_loan(self):
        # Create instance
        self.add_people_top = tk.Toplevel(self.master)
        # self.add_people_top.geometry("500x280")
        self.add_people_top.title("Borrower's Profile")
        self.add_people_top.configure(bg="#4C8404")

        self.add_people_widget()

        # Grab record number
        selected = self.account_borrower_lb.focus()

        # Grab record values
        values = self.account_borrower_lb.item(selected, "values")

        # Insert values to entry widgets
        self.add_people_name_entry.insert(0, values[0])
        self.add_people_address_entry.insert(0, values[1])
        self.age_spinbox.insert(0, values[2])
        self.gender_combobox.delete(0, "end")
        self.gender_combobox.insert(0, values[3])

        Content.destroy_button(self.add_people_lf)
        Content.disable_entry(self.add_people_lf)

        self.issue_loan_widget()

        # Disables underlying window
        self.add_people_top.grab_set()

        self.add_people_top.mainloop()

    def issue_loan_widget(self):
        # Register container
        self.issue_loan_lf = tk.LabelFrame(self.add_people_top, padx=20, pady=20, relief="flat")
        self.issue_loan_lf.pack(anchor="center", expand=True, fill="both")

        # Creating widgets
        ttk.Label(self.issue_loan_lf, text="Amount", style="h3.TLabel").grid(column=0, row=0, columnspan=2,
                                                                             padx=5, pady=5, sticky="w")

        self.issue_loan_amount_sb = ttk.Spinbox(self.issue_loan_lf, from_=0, to=200000, width=10)
        self.issue_loan_amount_sb.grid(column=1, row=0, padx=5, pady=5, sticky="w")

        # Focuses cursor on add name entry
        self.issue_loan_amount_sb.focus()

        ttk.Label(self.issue_loan_lf, text="Interest rate", style="h3.TLabel").grid(column=0, row=1, padx=5, pady=5,
                                                                                    sticky="w")

        self.issue_loan_interest_sb = ttk.Spinbox(self.issue_loan_lf, from_=0, to=200000, width=5)
        self.issue_loan_interest_sb.grid(column=1, row=1, padx=5, pady=5, sticky="w")

        ttk.Label(self.issue_loan_lf, text="Interest per (n) days", style="h3.TLabel").grid(column=0, row=2, padx=5,
                                                                                            pady=5, sticky="w")

        self.issue_loan_days_sb = ttk.Spinbox(self.issue_loan_lf, from_=0, to=200000, width=5)
        self.issue_loan_days_sb.grid(column=1, row=2, padx=5, pady=5, sticky="w")

        ttk.Label(self.issue_loan_lf, text="Date issued", style="h3.TLabel").grid(column=0, row=3, padx=5, pady=5,
                                                                                  sticky="w")
        self.issue_loan_date_de = DateEntry(self.issue_loan_lf, width=15, background='green',
                                            foreground='white', borderwidth=2)
        self.issue_loan_date_de.grid(column=1, row=3, columnspan=3, padx=5, pady=5, sticky="w")

        # Combobox for loan
        ttk.Label(self.issue_loan_lf, text="Status", style="h3.TLabel").grid(column=0, row=4, padx=5, pady=5,
                                                                             sticky="w")
        self.status_combobox = ttk.Combobox(self.issue_loan_lf, width=15)
        self.status_combobox['values'] = "Active", "Fully Amortized", "Default"
        self.status_combobox.grid(column=1, row=4, padx=5, pady=5, sticky="w")
        self.status_combobox.current(0)

        # Button for adding people to database
        self.cancel_issue_loan_b = tk.Button(self.issue_loan_lf, text="Done", font="OpenSans, 12", fg="#FFFFFF",
                                             bg="#4C8404", relief="flat", command=self.finish_issue_loan)
        self.cancel_issue_loan_b.grid(column=0, row=5, padx=5, pady=5)

        # Button for adding people to database
        self.finish_issue_loan_b = tk.Button(self.issue_loan_lf, text="Cancel", font="OpenSans, 12", fg="#4C8404",
                                             bg="#FFFFFF", relief="flat", command=self.add_people_top.destroy)
        self.finish_issue_loan_b.grid(column=1, row=5, padx=5, pady=5, sticky="w")

    def register_payment(self):
        # Create instance
        self.add_people_top = tk.Toplevel(self.master)
        # self.add_people_top.geometry("500x280")
        self.add_people_top.title("Register payment")
        self.add_people_top.configure(bg="#FFFFFF")

        # Register container
        self.rp_info_lf = tk.LabelFrame(self.add_people_top, padx=20, pady=20, relief="flat", background="#FFFFFF")
        self.rp_info_lf.pack(anchor="center", expand=True, fill="both")

        ttk.Label(self.rp_info_lf, text="Name", style="body.TLabel").grid(column=0, row=0, padx=5, pady=5, sticky="w")

        self.rp_info_name_l = ttk.Label(self.rp_info_lf, style="body.TLabel")
        self.rp_info_name_l.grid(column=1, row=0, padx=5, pady=5, sticky="w")

        ttk.Label(self.rp_info_lf, text="Loan ID", style="body.TLabel").grid(column=0, row=1, padx=5, pady=5,
                                                                             sticky="w")

        self.rp_info_loanid_l = ttk.Label(self.rp_info_lf, style="body.TLabel")
        self.rp_info_loanid_l.grid(column=1, row=1, padx=5, pady=5, sticky="w")

        ttk.Label(self.rp_info_lf, text="Loan amount", style="body.TLabel").grid(column=0, row=2, padx=5, pady=5,
                                                                                 sticky="w")

        self.rp_info_amount_l = ttk.Label(self.rp_info_lf, style="body.TLabel")
        self.rp_info_amount_l.grid(column=1, row=2, padx=5, pady=5, sticky="w")

        ttk.Label(self.rp_info_lf, text="Interest rate (%)", style="body.TLabel").grid(column=0, row=3, padx=5, pady=5,
                                                                                 sticky="w")

        self.rp_interest_l = ttk.Label(self.rp_info_lf, style="body.TLabel")
        self.rp_interest_l.grid(column=1, row=3, padx=5, pady=5, sticky="w")

        ttk.Label(self.rp_info_lf, text="Balance", style="body.TLabel").grid(column=0, row=4, padx=5, pady=5,
                                                                             sticky="w")

        self.rp_info_balance_l = ttk.Label(self.rp_info_lf, style="body.TLabel")
        self.rp_info_balance_l.grid(column=1, row=4, padx=5, pady=5, sticky="w")

        ttk.Label(self.rp_info_lf, text="Recommended payment", style="body.TLabel").grid(column=0, row=5, padx=5,
                                                                                         pady=5, sticky="w")

        self.rp_info_recommend_pay_l = ttk.Label(self.rp_info_lf, style="body.TLabel")
        self.rp_info_recommend_pay_l.grid(column=1, row=5, padx=5, pady=5, sticky="w")

        ttk.Label(self.rp_info_lf, text="Payment amount", style="body.TLabel").grid(column=0, row=6, padx=5, pady=5,
                                                                                    sticky="w")

        self.rp_info_payment_entry = ttk.Entry(self.rp_info_lf, width=30)
        self.rp_info_payment_entry.grid(column=1, row=6, padx=5, pady=5, sticky="w")

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

            # Updates account window
            self.switch_account()
        except Exception as e:
            # Deletes all entries from ttk.Entry
            Content.delete_entry(self.master)
            # Show a messagebox for unsuccessfully adding people
            messagebox.showerror("Borrower's Account", "Did not succeed in adding account")
            print("Could not connect to lmsdatabase")
            print(e)

    def finish_issue_loan(self):
        try:
            self.database_connect()

            self.mycursor.execute(
                "INSERT INTO loan (borrowerid, userid, amount, interest, days, created, dateissued, status) VALUES (%s,"
                " %s, %s, %s, %s, %s, %s, %s)",
                (self.borrower_key_str, self.key_str, self.issue_loan_amount_sb.get(),
                 self.issue_loan_interest_sb.get(), self.issue_loan_days_sb.get(), datetime.now(),
                 self.issue_loan_date_de.get_date(), self.status_combobox.get()))

            self.db1.commit()
            self.db1.close()
            self.mycursor.close()

            # Destroy add_people_top form
            self.add_people_top.destroy()

            # Show a messagebox for successfully adding people
            messagebox.showinfo("Issue loan", "Loan issued successfully")

            # Updates account window
            self.switch_account()
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
            self.mycursor.execute("SELECT name, address, age, gender, borrowerid FROM borrower where userid = '"
                                  + self.key_str +
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

            self.db1.commit()
            self.mycursor.close()
            self.db1.close()

        except Exception as e:
            print("Could not connect to lmsdatabase")
            print(e)

    def register_payment(self):
        # Create instance
        self.add_people_top = tk.Toplevel(self.master)
        # self.add_people_top.geometry("500x280")
        self.add_people_top.title("Register payment")
        self.add_people_top.configure(bg="#FFFFFF")

        # Register container
        self.rp_info_lf = tk.LabelFrame(self.add_people_top, padx=20, pady=20, relief="flat", background="#FFFFFF")
        self.rp_info_lf.pack(anchor="center", expand=True, fill="both")

        ttk.Label(self.rp_info_lf, text="Name", style="body.TLabel").grid(column=0, row=0, padx=5, pady=5, sticky="w")

        self.rp_info_name_l = ttk.Label(self.rp_info_lf, style="body_content.TLabel")
        self.rp_info_name_l.grid(column=1, row=0, padx=5, pady=5, sticky="w")

        ttk.Label(self.rp_info_lf, text="Loan ID", style="body.TLabel").grid(column=0, row=1, padx=5, pady=5,
                                                                             sticky="w")

        self.rp_info_loanid_l = ttk.Label(self.rp_info_lf, style="body_content.TLabel")
        self.rp_info_loanid_l.grid(column=1, row=1, padx=5, pady=5, sticky="w")

        ttk.Label(self.rp_info_lf, text="Loan amount", style="body.TLabel").grid(column=0, row=2, padx=5, pady=5,
                                                                                 sticky="w")

        self.rp_info_amount_l = ttk.Label(self.rp_info_lf, style="body_content.TLabel")
        self.rp_info_amount_l.grid(column=1, row=2, padx=5, pady=5, sticky="w")

        ttk.Label(self.rp_info_lf, text="Interest rate (%)", style="body.TLabel").grid(column=0, row=3, padx=5, pady=5,
                                                                                       sticky="w")

        self.rp_interest_l = ttk.Label(self.rp_info_lf, style="body_content.TLabel")
        self.rp_interest_l.grid(column=1, row=3, padx=5, pady=5, sticky="w")

        ttk.Label(self.rp_info_lf, text="Balance", style="body.TLabel").grid(column=0, row=4, padx=5, pady=5,
                                                                             sticky="w")

        self.rp_info_balance_l = ttk.Label(self.rp_info_lf, style="body_content.TLabel")
        self.rp_info_balance_l.grid(column=1, row=4, padx=5, pady=5, sticky="w")

        ttk.Label(self.rp_info_lf, text="Recommended payment", style="body.TLabel").grid(column=0, row=5, padx=5,
                                                                                         pady=5, sticky="w")

        self.rp_info_recommend_pay_l = ttk.Label(self.rp_info_lf, style="body_content.TLabel")
        self.rp_info_recommend_pay_l.grid(column=1, row=5, padx=5, pady=5, sticky="w")

        ttk.Label(self.rp_info_lf, text="Payment amount", style="body.TLabel").grid(column=0, row=6, padx=5, pady=5,
                                                                                    sticky="w")

        self.rp_info_payment_entry = ttk.Entry(self.rp_info_lf, width=30)
        self.rp_info_payment_entry.grid(column=1, row=6, padx=5, pady=5, sticky="w")

        # Grab record number
        selected = self.loan_borrower_lb.focus()

        # Grab record values
        values = self.loan_borrower_lb.item(selected, "values")

        # Get loan id
        self.loan_id = values[0]
        print(self.loan_id)

        # Insert values to info widgets
        self.rp_info_name_l.configure(text=values[1])
        self.rp_info_loanid_l.configure(text=values[0])
        self.rp_info_amount_l.configure(text=values[2])
        self.rp_interest_l.configure(text=values[3])

        # Disables underlying window
        self.add_people_top.grab_set()

        self.add_people_top.mainloop()

    def database_view_loan(self):
        # Method for viewing accounts database
        try:
            self.database_connect()
            self.mycursor.execute("SELECT loan.loanid, borrower.name, loan.amount, loan.interest, loan.days,"
                                  " loan.dateissued, loan.status, borrower.userid FROM loan INNER JOIN borrower ON"
                                  " loan.borrowerid=borrower.borrowerid "
                                  "where borrower.userid = '" + self.key_str + "';")
            loans = self.mycursor.fetchall()
            print(loans)

            # Create configure for striped rows
            self.loan_borrower_lb.tag_configure("oddrow", background="#FFFFFF")
            self.loan_borrower_lb.tag_configure("evenrow", background="#FAFAFA")
            count = 0
            for record in loans:
                if count % 2 == 0:
                    self.loan_borrower_lb.insert(parent="", index="end", iid=count, text="",
                                                 values=(record[0], record[1], record[2], record[3], record[4],
                                                         record[5], record[6]),
                                                 tags=("oddrow",))
                else:
                    self.loan_borrower_lb.insert(parent="", index="end", iid=count, text="",
                                                 values=(record[0], record[1], record[2], record[3], record[4],
                                                         record[5], record[6]),
                                                 tags=("evenrow",))
                count += 1

            self.db1.commit()
            self.mycursor.close()
            self.db1.close()

        except Exception as e:
            print("Could not connect to lmsdatabase")
            print(e)

    def database_view_loan_info(self, event):
        # Destroy content of account_content_view_lf
        Content.destroy_content(self.loan_content_view_lf)

        # Create widgets for displaying account information
        ttk.Label(self.loan_content_view_lf, text="Loan Information",
                  style="heading.TLabel").grid(column=0, row=0, columnspan=2, pady=5, sticky="w")

        ttk.Label(self.loan_content_view_lf, text="Name",
                  style="body.TLabel").grid(column=0, row=1, columnspan=2, padx=5, pady=5, sticky="w")

        self.loan_content_name_l = ttk.Label(self.loan_content_view_lf, style="body_content.TLabel")
        self.loan_content_name_l.grid(column=1, row=1, columnspan=2, sticky="w")

        ttk.Label(self.loan_content_view_lf, text="Amount",
                  style="body.TLabel").grid(column=0, row=2, columnspan=2, padx=5, pady=5, sticky="w")

        self.loan_content_amount_e = ttk.Entry(self.loan_content_view_lf, width=40)
        self.loan_content_amount_e.grid(column=1, row=2, columnspan=2)

        ttk.Label(self.loan_content_view_lf, text="Interest (%)",
                  style="body.TLabel").grid(column=0, row=3, columnspan=2, padx=5, pady=5, sticky="w")

        self.loan_content_interest_e = ttk.Entry(self.loan_content_view_lf, width=40)
        self.loan_content_interest_e.grid(column=1, row=3, columnspan=2)

        ttk.Label(self.loan_content_view_lf, text="Interest per (n) days",
                  style="body.TLabel").grid(column=0, row=4, padx=5, pady=5, sticky="w")

        self.loan_content_interest_pd_e = ttk.Entry(self.loan_content_view_lf, width=40)
        self.loan_content_interest_pd_e.grid(column=1, row=4, columnspan=2)

        ttk.Label(self.loan_content_view_lf, text="Date issued",
                  style="body.TLabel").grid(column=0, row=5, columnspan=2, padx=5, pady=5, sticky="w")

        self.loan_content_date_issued_cal = DateEntry(self.loan_content_view_lf, width=12, background='green',
                                                      foreground='white', borderwidth=2)
        self.loan_content_date_issued_cal.grid(column=1, row=5, columnspan=2, sticky="w")

        # Combobox for loan
        ttk.Label(self.loan_content_view_lf, text="Status", style="body.TLabel").grid(column=0, row=6, padx=5, pady=5,
                                                                                      sticky="w")

        self.loan_content_status_cb = ttk.Combobox(self.loan_content_view_lf, width=12)
        self.loan_content_status_cb['values'] = "Active", "Fully Amortized", "Default"
        self.loan_content_status_cb.grid(column=1, row=6, sticky="w")
        # self.loan_content_status_cb.current(0)

        # Delete initial entry of date entry
        self.loan_content_date_issued_cal.delete(0, "end")

        # Grab record number
        selected = self.loan_borrower_lb.focus()

        # Grab record values
        values = self.loan_borrower_lb.item(selected, "values")

        # Get loan id
        self.loan_id = values[0]
        print(self.loan_id)

        # Insert values to entry widgets
        self.loan_content_name_l.configure(text=values[1])
        self.loan_content_amount_e.insert(0, values[2])
        self.loan_content_interest_e.insert(0, values[3])
        self.loan_content_interest_pd_e.insert(0, values[4])
        self.loan_content_date_issued_cal.insert(0, values[5])
        self.loan_content_status_cb.insert(0, values[6])

        # Button for deleting a loan
        self.delete_loan_b = tk.Button(self.loan_content_view_lf, text="Delete Loan", font="OpenSans, 10",
                                       fg="#FFFFFF", bg="#4C8404", relief="flat",
                                       command=self.delete_loan_record)
        self.delete_loan_b.grid(column=0, row=7, padx=5, pady=5, sticky="w")

        # Button for updating a record
        self.save_loan_b = tk.Button(self.loan_content_view_lf, text="Save changes", font="OpenSans, 10",
                                     fg="#FFFFFF", bg="#4C8404", relief="flat",
                                     command=self.update_loan_record)
        self.save_loan_b.grid(column=1, row=7, padx=5, pady=5, sticky="w")

        # Button for registering payment
        self.register_payment_b = tk.Button(self.loan_content_view_lf, text="Register payment", font="OpenSans, 10",
                                            fg="#FFFFFF", bg="#4C8404", relief="flat", command=self.register_payment)
        self.register_payment_b.grid(column=2, row=7, padx=5, pady=5, sticky="w")

        print(event)

    def database_view_account_info(self, event):
        # Destroy content of account_content_view_lf
        Content.destroy_content(self.account_content_view_lf)

        # Create widgets for displaying account information
        ttk.Label(self.account_content_view_lf, text="Account Information",
                  style="heading.TLabel").grid(column=0, row=0, columnspan=2, pady=5, sticky="w")

        ttk.Label(self.account_content_view_lf, text="Name",
                  style="body.TLabel").grid(column=0, row=1, padx=5, pady=5, sticky="w")

        self.account_content_name_e = ttk.Entry(self.account_content_view_lf, width=40)
        self.account_content_name_e.grid(column=1, row=1, columnspan=3)

        ttk.Label(self.account_content_view_lf, text="Address",
                  style="body.TLabel").grid(column=0, row=2, padx=5, pady=5, sticky="w")

        self.account_content_address_e = ttk.Entry(self.account_content_view_lf, width=40)
        self.account_content_address_e.grid(column=1, row=2, columnspan=3)

        ttk.Label(self.account_content_view_lf, text="Age",
                  style="body.TLabel").grid(column=0, row=3, padx=5, pady=5, sticky="w")

        self.account_content_age_e = ttk.Entry(self.account_content_view_lf, width=40)
        self.account_content_age_e.grid(column=1, row=3, columnspan=3)

        ttk.Label(self.account_content_view_lf, text="Gender",
                  style="body.TLabel").grid(column=0, row=4, padx=5, pady=5, sticky="w")

        self.account_content_gender_e = ttk.Entry(self.account_content_view_lf, width=40)
        self.account_content_gender_e.grid(column=1, row=4, columnspan=3)

        # Grab record number
        selected = self.account_borrower_lb.focus()

        # Grab record values
        values = self.account_borrower_lb.item(selected, "values")

        # Insert values to entry widgets
        self.account_content_name_e.insert(0, values[0])
        self.account_content_address_e.insert(0, values[1])
        self.account_content_age_e.insert(0, values[2])
        self.account_content_gender_e.insert(0, values[3])

        # Button for deleting a record
        self.delete_account_b = tk.Button(self.account_content_view_lf, text="Delete Account", font="OpenSans, 10",
                                          fg="#FFFFFF", bg="#4C8404", relief="flat",
                                          command=self.delete_account_record)
        self.delete_account_b.grid(column=0, row=5, padx=5, pady=5, sticky="w")

        # Button for updating a record
        self.save_account_b = tk.Button(self.account_content_view_lf, text="Save changes", font="OpenSans, 10",
                                        fg="#FFFFFF", bg="#4C8404", relief="flat",
                                        command=self.update_account_record)
        self.save_account_b.grid(column=1, row=5, padx=5, pady=5, sticky="w")

        # Button for opening form for adding borrower
        self.issue_loan_b = tk.Button(self.account_content_view_lf, text="Issue loan", font="OpenSans, 10",
                                      fg="#FFFFFF", bg="#4C8404", relief="flat",
                                      command=self.issue_loan)
        self.issue_loan_b.grid(column=2, row=5, padx=5, pady=5, sticky="w")

        ttk.Label(self.account_content_view_lf, text="Total loans",
                  style="body.TLabel").grid(column=4, row=1, padx=5, pady=5, sticky="w")

        self.total_loan_l = ttk.Label(self.account_content_view_lf, text=0, style="body_content.TLabel")
        self.total_loan_l.grid(column=5, row=1, padx=5, pady=5, sticky="w")

        print(event)

        # Assign variable to borrower id
        self.show_borrower_id()

        # Initialize additional info on account
        self.database_view_account_add_info()

    def database_view_account_add_info(self):
        self.total_loan_l.configure(text=0)
        # Method for viewing accounts database
        self.database_connect()
        self.mycursor.execute("SELECT loanid FROM loan where borrowerid = '"
                              + self.borrower_key_str +
                              "';")
        loan = self.mycursor.fetchall()
        print(loan)

        self.count = 0

        for self.count, item in enumerate(loan):
            self.count += 1

        print(self.count)

        self.total_loan_l.configure(text=self.count)
        self.db1.commit()
        self.mycursor.close()
        self.db1.close()

    def show_borrower_id(self):
        try:
            self.database_connect()

            self.mycursor.execute("SELECT DISTINCT borrowerid FROM borrower WHERE NAME = '"
                                  + self.account_content_name_e.get() + "' AND userid = '" + self.key_str + "';")

            # Converts the tuple into integer
            self.borrower_key = functools.reduce(lambda sub, ele: sub * 10 + ele, self.mycursor.fetchone())
            self.borrower_key_str = str(self.borrower_key)
            print(self.borrower_key_str)

            self.mycursor.close()
            self.db1.close()

        except Exception as e:
            print("Could not connect to lmsdatabase")
            print(e)

    def update_account_record(self):
        self.database_connect()
        self.mycursor.execute(
            "UPDATE borrower SET name = '"
            + self.account_content_name_e.get() + "', address = '"
            + self.account_content_address_e.get() + "', age = '"
            + self.account_content_age_e.get() + "', gender = '"
            + self.account_content_gender_e.get() + "' WHERE borrowerid = '" + self.borrower_key_str + "';")

        self.db1.commit()
        self.db1.close()
        self.mycursor.close()

        # Update account window
        self.switch_account()

    def update_loan_record(self):
        self.database_connect()
        self.loan_content_date_issued_str = str(self.loan_content_date_issued_cal.get_date())
        print(type(self.loan_content_date_issued_str))
        self.mycursor.execute(
            "UPDATE loan SET amount = '" + self.loan_content_amount_e.get() + "', interest = '"
            + self.loan_content_interest_e.get() + "', days = '"
            + self.loan_content_interest_pd_e.get() + "', dateissued = '"
            + self.loan_content_date_issued_str + "', status = '"
            + self.loan_content_status_cb.get() + "' WHERE loanid = '" + self.loan_id + "';")

        self.db1.commit()
        self.db1.close()
        self.mycursor.close()

        # Update account window
        self.switch_loan()

    def delete_account_record(self):
        self.database_connect()
        # self.mycursor.execute("SET FOREIGN_KEY_CHECKS=0;")

        self.mycursor.execute("DELETE FROM borrower WHERE borrowerid = '" + self.borrower_key_str +
                              "';")
        # self.mycursor.execute("SET FOREIGN_KEY_CHECKS=1;")
        self.db1.commit()
        self.db1.close()
        self.mycursor.close()
        self.switch_account()

    def delete_loan_record(self):
        self.database_connect()
        # self.mycursor.execute("SET FOREIGN_KEY_CHECKS=0;")

        self.mycursor.execute("DELETE FROM loan WHERE loanid = '" + self.loan_id +
                              "';")
        # self.mycursor.execute("SET FOREIGN_KEY_CHECKS=1;")
        self.db1.commit()
        self.db1.close()
        self.mycursor.close()
        self.switch_loan()

    @staticmethod
    def state_button(widget1, widget2, widget3):
        widget1.configure(bg="#4C8404")
        widget2.configure(bg="#2C441D")
        widget3.configure(bg="#2C441D")


win = tk.Tk()
initialize = Window(win)

win.mainloop()
