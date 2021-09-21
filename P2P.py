import tkinter as tk
from datetime import datetime
from tkinter import ttk, messagebox
from databaseController import Database
import mysql.connector as mysql
from contentController import Content
import functools

# Global variables for database
host = "localhost"
user = "PongoDev"
password = "PongoDev44966874"


class Window:

    def __init__(self, master):
        # Instance attributes define within init scope conforming to PEP standards
        self.master = master
        self.login_lf = ttk.LabelFrame
        self.login_l = None
        self.login_username_entry = None
        self.login_password_entry = None
        self.register_lf = ttk.LabelFrame
        self.register_b = None
        self.register_cancel_b = None
        self.login_b = None
        self.key = None
        self.key_str = str
        self.register_top = None
        self.register_user_name_entry = None
        self.register_password_entry = None
        self.register_email_entry = None
        self.register_done_b = None
        self.menu_lf = None
        self.home_b = tk.Button
        self.loan_b = tk.Button
        self.profile_b = tk.Button
        self.logout_b = tk.Button
        self.content_lf = None
        self.home_lf = None
        self.home_dashboard_lf = None
        self.loan_lf = None
        self.profile_lf = None
        self.profile_buttons_lf = None
        self.profile_database_view_lf = None
        self.column_borrower_header = None
        self.profile_borrower_lb = ttk.Treeview
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

    def create_widgets(self):
        # Destroy window contents
        Content.destroy_content(self.master)

        # Menu container
        self.menu_lf = tk.LabelFrame(self.master, bg="#2C441D", relief="flat")
        self.menu_lf.pack(side="left", fill="both")

        # Menu buttons
        self.home_b = tk.Button(self.menu_lf, text="Home", font="OpenSans 20", relief="flat", bg="#2C441D",
                                fg="#FFFFFF", command=self.switch_home)
        self.home_b.pack(side="top", fill="both")

        self.loan_b = tk.Button(self.menu_lf, text="Loans", font="OpenSans, 20", relief="flat", bg="#2C441D",
                                fg="#FFFFFF", command=self.switch_loan)
        self.loan_b.pack(side="top", fill="both")

        self.profile_b = tk.Button(self.menu_lf, text="Profile", font="OpenSans, 20", relief="flat", bg="#2C441D",
                                   fg="#FFFFFF", command=self.switch_profile)
        self.profile_b.pack(side="top", fill="both")

        self.logout_b = tk.Button(self.menu_lf, text="Logout", font="OpenSans, 10", relief="flat", bg="#2C441D",
                                  fg="#FFFFFF", highlightcolor="#2C441D", command=self.login_win)
        self.logout_b.pack(side="bottom", fill="both", pady=20)

        # Contents container
        self.content_lf = tk.LabelFrame(self.master, relief="flat")
        self.content_lf.pack(side="left", fill="both", expand="true")

        # Initialize switch_home method for the default content
        self.switch_home()

    def switch_home(self):
        # Destroy content_lf
        Content.destroy_content(self.content_lf)

        # Home container
        self.home_lf = tk.LabelFrame(self.content_lf, relief="flat")
        self.home_lf.grid(column=0, row=0)

        # Home dashboard container
        self.home_dashboard_lf = tk.LabelFrame(self.home_lf, bg="#FFFFFF", relief="flat")
        self.home_dashboard_lf.pack(side="top")

        ttk.Label(self.home_dashboard_lf, text="Dashboard", background="#FFFFFF").pack(side="top")

        # Configure underline to none for previous button
        self.active_state(self.home_b)

        # Configure underline for current button
        self.inactive_state(self.profile_b, self.loan_b)

    def switch_loan(self):
        # Destroy content_lf
        Content.destroy_content(self.content_lf)

        # Loan container
        self.loan_lf = tk.LabelFrame(self.content_lf, bg="#FFFFFF", relief="flat")
        self.loan_lf.grid(column=0, row=0)

        ttk.Label(self.loan_lf, text="Loans", background="#FFFFFF").pack(side="top")

        # Configure underline to none for previous button
        self.active_state(self.loan_b)

        # Configure underline for current button
        self.inactive_state(self.profile_b, self.home_b)

    def switch_profile(self):
        # Destroy content_lf
        Content.destroy_content(self.content_lf)

        # Profile container
        self.profile_lf = tk.LabelFrame(self.content_lf, bg="#EBEBEB", relief="flat")
        self.profile_lf.pack(fill="both", expand=True)

        # Profile Button Container
        self.profile_buttons_lf = tk.LabelFrame(self.profile_lf, bg="#FFFFFF", relief="flat")
        self.profile_buttons_lf.pack(side="top", fill="x")

        # Button for opening form for adding borrower
        self.add_people_b = tk.Button(self.profile_buttons_lf, text="Add people", font="OpenSans, 10", fg="#FFFFFF",
                                      bg="#4C8404", relief="flat", command=self.add_people)
        self.add_people_b.pack(side="left", padx=5, pady=5)

        # Profile view database container
        self.profile_database_view_lf = tk.LabelFrame(self.profile_lf, bg="#FFFFFF", relief="flat")
        self.profile_database_view_lf.pack(side="top", pady=20, fill="both")

        self.profile_borrower_lb = ttk.Treeview(self.profile_database_view_lf)

        # Define column
        self.profile_borrower_lb["columns"] = ("Name", "Address", "Age", "Gender")

        # Format column
        self.profile_borrower_lb.column("#0", width=0, stretch="no")
        self.profile_borrower_lb.column("Name", anchor="w", width=120)
        self.profile_borrower_lb.column("Address", anchor="w", width=120)
        self.profile_borrower_lb.column("Age", anchor="center", width=80)
        self.profile_borrower_lb.column("Gender", anchor="center", width=80)

        # Create headings
        self.profile_borrower_lb.heading("#0", text="", anchor="w")
        self.profile_borrower_lb.heading("Name", text="Name", anchor="w")
        self.profile_borrower_lb.heading("Address", text="Address", anchor="w")
        self.profile_borrower_lb.heading("Age", text="Age", anchor="center")
        self.profile_borrower_lb.heading("Gender", text="Gender", anchor="center")

        self.profile_borrower_lb.pack(side="left", padx=20, pady=20, fill="both", expand=True)

        try:
            self.database_connect()
            self.mycursor.execute("SELECT name, address, age, gender FROM borrower where userid = '" + self.key_str +
                                  "';")
            borrowers = self.mycursor.fetchall()
            print(borrowers)

            # Create configure for striped rows
            self.profile_borrower_lb.tag_configure("oddrow", background="#FFFFFF")
            self.profile_borrower_lb.tag_configure("evenrow", background="#FAFAFA")
            count = 0
            for record in borrowers:
                if count % 2 == 0:
                    self.profile_borrower_lb.insert(parent="", index="end", iid=count, text="",
                                                    values=(record[0], record[1], record[2], record[3]),
                                                    tags=("oddrow",))
                else:
                    self.profile_borrower_lb.insert(parent="", index="end", iid=count, text="",
                                                    values=(record[0], record[1], record[2], record[3]),
                                                    tags=("evenrow",))
                count += 1

            self.db1.close()
        except Exception as e:
            print("Could not connect to lmsdatabase")
            print(e)

        # Configure underline to none for previous button
        self.active_state(self.profile_b)

        # Configure underline for current button
        self.inactive_state(self.loan_b, self.home_b)

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
            messagebox.showinfo("Borrower's Profile", "Profile added successfully")
        except Exception as e:
            # Deletes all entries from ttk.Entry
            Content.delete_entry(self.master)
            # Show a messagebox for unsuccessfully adding people
            messagebox.showerror("Borrower's Profile", "Did not succeed in adding profile")
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

    @staticmethod
    def active_state(widget):
        widget.configure(bg="#4C8404")

    @staticmethod
    def inactive_state(widget1, widget2):
        widget1.configure(bg="#2C441D")
        widget2.configure(bg="#2C441D")


win = tk.Tk()
initialize = Window(win)

win.mainloop()
