import tkinter
import tkinter as tk
from datetime import datetime
from datetime import timedelta
from tkinter import Menu
from tkinter import ttk, messagebox
from databaseController import Database
from ScrollableFrame import ScrollableFrame
import mysql.connector as mysql
from contentController import Content
import toolTip as tt
import functools
# from PIL import ImageTk, Image
from tkcalendar import DateEntry
import pandas as pd
# import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import PhotoImage
import webbrowser
from tkinter import filedialog
import os

# from tkinter.filedialog import asksaveasfile

# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
# import numpy as np

# Global variables for database
host = "localhost"
user = "PongoDev"
password = "PongoDev44966874"

# Global variables
# Create variable for first day of the month
fday_month = datetime.today().replace(day=1)
fday_month = fday_month.strftime("%x")
# Create variable for current day of the month
currentday_month = datetime.today()
currentday_month = currentday_month.strftime("%x")
peso = u"\u20B1"
lms_version = "LMSv.1.30"
url_small_claims = "https://www.philippine-embassy.org.sg/pages/small-claims-in-the-philippines/"
url_fair_debt = "http://legacy.senate.gov.ph/lisdata/26632027!.pdf"


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
        self.main_lf = None
        self.menu_lf = None
        self.home_f = None
        self.home_b = tk.Button
        self.loan_b = tk.Button
        self.account_b = tk.Button
        self.payment_b = tk.Button
        self.body_lf = None
        self.content_lf = None
        self.home_lf = None
        self.home_dashboard_f = None
        self.home_dashboard_scr = None
        self.loan_analytics_content = tk.LabelFrame
        self.payment_analytics_content = tk.LabelFrame
        self.loan_lf = None
        self.loan_database_view_lf = None
        self.loan_dashboard_lf = None
        self.loan_database_view_f = None
        self.loan_database_view_scr = None
        self.loan_borrower_lb = None
        self.loan_content_view_lf = None
        self.issue_loan_date_de = None
        self.status_combobox = None
        self.show_more_dashboard_b = None
        self.payment_lf = None
        self.payment_database_view_lf = None
        self.payment_database_view_f = None
        self.payment_database_view_scr = None
        self.payment_borrower_lb = None
        self.payment_content_view_lf = None
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
        self.loan_id = None
        self.loan_content_name_l = None
        self.loan_content_amount_e = None
        self.loan_content_interest_e = None
        self.loan_content_interest_pd_e = None
        self.loan_content_date_issued_e = None
        self.loan_content_status_cb = None
        self.loan_content_date_issued_str = None
        self.delete_loan_b = None
        self.save_loan_b = None
        self.register_payment_b = None
        self.time_rem_interest_l = None
        self.account_borrower_header = None
        self.account_borrower_lb = ttk.Treeview
        self.borrower_key = None
        self.borrower_key_str = None
        self.add_people_top = None
        self.add_people_lf = None
        self.add_people_name_entry = None
        self.add_people_address_entry = None
        self.age_spinbox = None
        self.gender_combobox = None
        self.finish_add_people_b = None
        self.cancel_add_people_b = None
        self.success_add_people_message = None
        self.rp_info_lf = None
        self.rp_info_name_l = None
        self.rp_info_loanid_l = None
        self.rp_info_amount_l = None
        self.rp_interest_l = None
        self.rp_info_balance_l = None
        self.rp_info_recommend_pay_l = None
        self.rp_info_payment_entry = None
        self.loan_content_date_issued_cal = None
        self.rp_buttons_lf = None
        self.register_payment_done_b = None
        self.register_payment_cancel_b = None
        self.db1 = None
        self.pandasdb = None
        self.mycursor = None
        self.count = None
        self.year = datetime.today().year
        self.month = datetime.today().month
        self.day = datetime.today().day
        self.remaining_days = None
        self.interest = None
        self.borrower_value = tk.IntVar()
        self.loan_value = tk.IntVar()
        self.payment_value = tk.IntVar()
        self.home_icon_inactive_resized = tkinter.PhotoImage
        self.loans_icon_inactive_resized = tkinter.PhotoImage
        self.accounts_icon_inactive_resized = tkinter.PhotoImage
        self.payments_icon_inactive_resized = tkinter.PhotoImage
        self.p2p_logo_resized = tkinter.PhotoImage
        self.home_icon_active_resized = tkinter.PhotoImage
        self.loans_icon_active_resized = tkinter.PhotoImage
        self.accounts_icon_active_resized = tkinter.PhotoImage
        self.payments_icon_active_resized = tkinter.PhotoImage
        self.exit_inactive_resized = tkinter.PhotoImage
        self.export_data_top = None
        self.dashboard_main_filter_from = None
        self.dashboard_main_filter_to = None
        self.filter_loan_cb = None
        self.loan_amount_l = None
        self.loan_count_l = None
        self.payment_amount_l = None
        self.payment_count_l = None
        self.filter_account_cb = None
        self.filter_payment_cb = None

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
        self.master.title("P2P " + lms_version)
        self.master.iconbitmap(r"C:\Users\SSD\IdeaProjects\LMS\images\p2p_icon.ico")
        width = self.master.winfo_screenwidth()
        height = self.master.winfo_screenheight()
        self.master.geometry("%dx%d" % (width, height))
        self.master.resizable(True, True)
        self.master.configure(bg="#4C8404")

        # ================================================ Logo section ================================================
        # Logo container
        self.main_lf = tk.LabelFrame(self.master, bg="#FFFFFF", relief="flat")
        self.main_lf.pack(side="top", fill="x")

        description_lf = tk.LabelFrame(self.main_lf, bg="#FFFFFF", relief="flat")
        description_lf.pack(side="top", fill="x")

        p2p_logo = PhotoImage(file=r"C:\Users\SSD\IdeaProjects\LMS\images\p2p_logo.png")
        self.p2p_logo_resized = p2p_logo.subsample(1, 1)

        ttk.Label(self.main_lf, image=self.p2p_logo_resized).pack(side="left", padx=10, pady=10)

        # ================================================ Description section =========================================
        description_lf = tk.LabelFrame(self.main_lf, bg="#FFFFFF", relief="flat")
        description_lf.pack(side="left")

        ttk.Label(description_lf, text="Welcome to P2P LMS", style="h1_title.TLabel").pack(side="top",
                                                                                           anchor="w", pady=10)
        ttk.Label(description_lf, text="P2P LMS is a tool that allows managing, storing and processing information "
                                       "\ngathered for lending purposes. ",
                  style="h1_body.TLabel").pack(side="top", anchor="w")
        ttk.Label(description_lf, text="Email: christian.gealone1@gmail.com / pongodev0914@gmail.com",
                  style="h1_footnote.TLabel").pack(side="bottom", anchor="w", pady=10)
        ttk.Label(description_lf, text="Contact us:",
                  style="h1_footnote.TLabel").pack(side="bottom", anchor="w")

        # ================================================ Login section ===============================================
        # Login container
        self.login_lf = tk.LabelFrame(self.main_lf, bg="#FFFFFF")
        self.login_lf.pack(side="right", padx=20, pady=20)

        # Login widgets
        ttk.Label(self.login_lf, text="Login", style="h1.TLabel").grid(column=0, row=0, pady=10)

        ttk.Label(self.login_lf, text="User Name", style="h1_footnote.TLabel").grid(column=0,
                                                                                    row=1, pady=10, sticky="w")

        self.login_username_entry = ttk.Entry(self.login_lf, width=40)
        self.login_username_entry.grid(column=1, row=1, padx=5)

        # Focuses cursor on username entry
        self.login_username_entry.focus()

        ttk.Label(self.login_lf, text="Password", style="h1_footnote.TLabel").grid(column=0, row=2, pady=10, sticky="w")

        self.login_password_entry = ttk.Entry(self.login_lf, show="*", width=40)
        self.login_password_entry.grid(column=1, row=2, padx=5)

        self.register_b = tk.Button(self.login_lf, text="                              Register                        "
                                                        "       ", font="OpenSans, 12", fg="#4C8404", bg="#D4DEC9",
                                    relief="flat", command=self.register_win)
        self.register_b.grid(column=0, row=3, columnspan=2, pady=5)

        self.login_b = tk.Button(self.login_lf, text="                                Log in                           "
                                                     "      ", font="OpenSans, 12", fg="#FFFFFF", bg="#4C8404",
                                 relief="flat", command=self.login_validation)
        self.login_b.grid(column=0, row=4, columnspan=2, pady=5)

        # ================================================ Features Description section ================================
        features_lf = tk.LabelFrame(self.master, bg="#FFFFFF", relief="flat")
        features_lf.pack(side="top", expand=True, anchor="center", ipadx=20, ipady=20)

        # ================================================ Features Description section ================================
        system_features_lf = tk.LabelFrame(features_lf, background="#FFFFFF", relief="flat")
        system_features_lf.pack(side="left", padx=40, pady=40)

        ttk.Label(system_features_lf, text="P2P Lending Management System",
                  style="featured_h1.TLabel").pack(side="top", pady=10, anchor="w")
        ttk.Label(system_features_lf, text="_____",
                  style="featured_h1_big.TLabel").pack(side="top", anchor="w")
        ttk.Label(system_features_lf, text="Lending Management System comes \n"
                                           "with a slew of capabilities, from \n"
                                           "a user-friendly interface to extensive \n"
                                           "data management controls,as well as \n"
                                           "extra data visualization options. \n\n"
                                           "Extend your business with a centralized \n"
                                           "system that takes care of the hassle of \n"
                                           "data processing.\n",
                  style="featured_h2.TLabel").pack(side="top", anchor="w")

        # ================================================ Features Description section ================================
        system_features_2_lf = tk.LabelFrame(features_lf, bg="#FFFFFF")
        system_features_2_lf.pack(side="left", pady=10, padx=10)

        ttk.Label(system_features_2_lf, text="Developer's Information",
                  style="featured_h1_2.TLabel").pack(side="top", pady=10, anchor="w")
        ttk.Label(system_features_2_lf, text="Gealone, Christian A.\n"
                                             "Anotado, Michael M. \n"
                                             "Gonzales, John Patrick M.\n"
                                             "Reyes, Angel Bryan L. \n"
                                             "Herrera, Jeremy \n"
                                             "Jaudian, Jeffrey G.\n\n\n",
                  style="featured_h2_2.TLabel").pack(side="top", anchor="w")

    def register_win(self):
        # Destroy login content
        self.login_lf.destroy()

        # ================================================ Register section ============================================
        # Register container
        self.register_lf = tk.LabelFrame(self.main_lf, bg="#FFFFFF")
        self.register_lf.pack(side="right", padx=20, pady=20)

        # Creating widgets
        ttk.Label(self.register_lf, text="Register", style="h1.TLabel").grid(column=0, row=0, columnspan=1, pady=10)

        ttk.Label(self.register_lf, text="User Name", style="h1_footnote.TLabel").grid(column=0, row=1, pady=10,
                                                                                       sticky="w")

        self.register_user_name_entry = ttk.Entry(self.register_lf, width=40)
        self.register_user_name_entry.grid(column=1, row=1, padx=5)

        # Focuses cursor on username entry
        self.register_user_name_entry.focus()

        ttk.Label(self.register_lf, text="Password", style="h1_footnote.TLabel").grid(column=0, row=2, pady=10,
                                                                                      sticky="w")

        self.register_password_entry = ttk.Entry(self.register_lf, width=40)
        self.register_password_entry.grid(column=1, row=2, padx=5)

        ttk.Label(self.register_lf, text="Email", style="h1_footnote.TLabel").grid(column=0, row=3, padx=5,
                                                                                   sticky="w")

        self.register_email_entry = ttk.Entry(self.register_lf, width=40)
        self.register_email_entry.grid(column=1, row=3, pady=5)

        # Button for cancelling registration
        self.register_cancel_b = tk.Button(self.register_lf, text="                                Cancel              "
                                                                  "                   ", font="OpenSans, 12",
                                           relief="flat", fg="#4C8404", bg="#D4DEC9", command=self.login_win)
        self.register_cancel_b.grid(column=0, row=4, columnspan=2, pady=5)

        # Button for adding people to database
        self.register_done_b = tk.Button(self.register_lf, text="                               Register               "
                                                                "                 ", font="OpenSans, 12", relief="flat",
                                         fg="#FFFFFF", bg="#4C8404", command=self.register_validation)
        self.register_done_b.grid(column=0, row=5, columnspan=2, pady=10)

    def mysql_pandas_user(self):
        try:
            self.pandasdb = mysql.connect(host=host,
                                          user=user,
                                          password=password,
                                          database="lmsdatabase",
                                          use_pure=True)
            query = "Select * from user;"
            df = pd.read_sql(query, self.pandasdb)
            self.pandasdb.close()
            print("User's dataframe")
            print(df.to_string())
        except Exception as e:
            self.pandasdb.close()
            print(str(e))

    def mysql_pandas_borrower(self):
        try:
            self.pandasdb = mysql.connect(host=host,
                                          user=user,
                                          password=password,
                                          database="lmsdatabase",
                                          use_pure=True)
            print(currentday_month)
            query = "Select loan.amount from loan where dateissued >= '" \
                    + fday_month + "' AND dateissued <= '" + currentday_month + "';"
            print(fday_month)
            df = pd.read_sql(query, self.pandasdb)
            self.pandasdb.close()
            print("Loan's dataframe")
            print(df)
            fig = Figure(figsize=(5, 5), dpi=75)
            ax1 = fig.add_subplot(111)
            ax1.plot(df, marker="o", label="amount of loans")
            ax1.set_title("Loans")
            ax1.set_xlabel("No. of loans")
            ax1.set_ylabel("Amount of loans")
            ax1.legend()

            canvas = FigureCanvasTkAgg(fig, self.home_dashboard_f)
            canvas.draw()
            canvas.get_tk_widget().pack(side="left", anchor="w", padx=10, pady=10)
        except Exception as e:
            self.pandasdb.close()
            print(e)

    def mysql_pandas_loans(self):
        Content.destroy_content(self.loan_analytics_content)
        pandasdb = mysql.connect(host=host,
                                 user=user,
                                 password=password,
                                 database="lmsdatabase",
                                 use_pure=True)
        query = "Select loan.amount from loan INNER JOIN borrower ON " \
                "loan.borrowerid=borrower.borrowerid where dateissued >= '" + self.dashboard_main_filter_from.get() + \
                "' AND dateissued <= '" + self.dashboard_main_filter_to.get() + "' AND borrower.userid = '" \
                + self.key_str + "'; "

        df = pd.read_sql(query, pandasdb)
        pandasdb.close()

        print("Loan's dataframe")
        print(df)
        total_loan_amount = df['amount'].sum()
        self.loan_amount_l.configure(text=total_loan_amount)
        self.loan_count_l.configure(text=len(df.index))

        width = self.master.winfo_screenmmwidth()

        fig = Figure(figsize=(width / 25.4, 5), dpi=75)
        ax1 = fig.add_subplot(111)
        ax1.plot(df, marker="o", label="loan amount in PHP")
        ax1.set_title("Loans")
        ax1.set_xlabel("No. of loans")
        ax1.set_ylabel("loan amounts in Philippine Peso")
        ax1.legend()

        canvas = FigureCanvasTkAgg(fig, self.loan_analytics_content)
        canvas.draw()
        canvas.get_tk_widget().pack(side="left", padx=10, pady=10, fill="both", expand=True)

    def mysql_pandas_payment(self):
        Content.destroy_content(self.payment_analytics_content)
        pandasdb = mysql.connect(host=host,
                                 user=user,
                                 password=password,
                                 database="lmsdatabase",
                                 use_pure=True)
        print(currentday_month)
        query = "Select payment.amount from payment INNER JOIN loan ON payment.loanid=loan.loanid INNER " \
                "JOIN borrower ON loan.borrowerid=borrower.borrowerid where payment.dateissued >= '" \
                + self.dashboard_main_filter_from.get() + "' AND payment.dateissued <= '" \
                + self.dashboard_main_filter_to.get() + "' AND borrower.userid = '" + self.key_str + "'; "
        df = pd.read_sql(query, pandasdb)
        pandasdb.close()
        print("Payment's dataframe")
        print(df)
        total_payment_amount = df['amount'].sum()
        print(total_payment_amount)
        self.payment_amount_l.configure(text=total_payment_amount)
        self.payment_count_l.configure(text=len(df.index))

        fig = Figure(figsize=(5, 5), dpi=75)
        ax1 = fig.add_subplot(111)
        ax1.plot(df, marker="o", label="payment amount in Philippine Peso")
        ax1.set_title("Payments")
        ax1.set_xlabel("No. of payments")
        ax1.set_ylabel("payment amount in Philippine Peso")
        ax1.legend()

        canvas = FigureCanvasTkAgg(fig, self.payment_analytics_content)
        canvas.draw()
        canvas.get_tk_widget().pack(side="left", padx=10, pady=10, fill="both", expand=True)

    def create_widgets(self):
        # Destroy window contents
        Content.destroy_content(self.master)

        # ================================================ Menu Bar Section ============================================
        menu_bar = Menu(self.master)
        self.master.config(menu=menu_bar)

        # Creating help menu
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Import", command=self.import_database)
        file_menu.add_command(label="Export", command=self.export_database_widget)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.switch_exit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Creating help menu
        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="User Manual")
        help_menu.add_separator()
        help_menu.add_command(label="Check for updates")
        menu_bar.add_cascade(label="Help", menu=help_menu)

        # ================================================ Menu Section ================================================
        self.menu_lf = tk.LabelFrame(self.master, bg="#4C8404", relief="flat")
        self.menu_lf.pack(side="left", fill="both")

        # Create variables for inactive images
        home_icon_inactive = PhotoImage(file=r"C:\Users\SSD\IdeaProjects\LMS\images\home_icon_inactive.png")
        self.home_icon_inactive_resized = home_icon_inactive.subsample(8, 8)

        loans_icon_inactive = PhotoImage(file=r"C:\Users\SSD\IdeaProjects\LMS\images\loan_icon_inactive.png")
        self.loans_icon_inactive_resized = loans_icon_inactive.subsample(8, 8)

        accounts_icon_inactive = PhotoImage(file=r"C:\Users\SSD\IdeaProjects\LMS\images\accounts_icon_inactive.png")
        self.accounts_icon_inactive_resized = accounts_icon_inactive.subsample(8, 8)

        payments_icon_inactive = PhotoImage(file=r"C:\Users\SSD\IdeaProjects\LMS\images\payments_icon_inactive.png")
        self.payments_icon_inactive_resized = payments_icon_inactive.subsample(8, 8)

        exit_icon_inactive = PhotoImage(file=r"C:\Users\SSD\IdeaProjects\LMS\images\exit_inactive.png")
        self.exit_inactive_resized = exit_icon_inactive.subsample(8, 8)

        # Create variables for active images
        home_icon_active = PhotoImage(file=r"C:\Users\SSD\IdeaProjects\LMS\images\home_icon_active.png")
        self.home_icon_active_resized = home_icon_active.subsample(8, 8)

        loans_icon_active = PhotoImage(file=r"C:\Users\SSD\IdeaProjects\LMS\images\loans_icon_active.png")
        self.loans_icon_active_resized = loans_icon_active.subsample(8, 8)

        accounts_icon_active = PhotoImage(file=r"C:\Users\SSD\IdeaProjects\LMS\images\accounts_icon_active.png")
        self.accounts_icon_active_resized = accounts_icon_active.subsample(8, 8)

        payments_icon_active = PhotoImage(file=r"C:\Users\SSD\IdeaProjects\LMS\images\payments_icon_active.png")
        self.payments_icon_active_resized = payments_icon_active.subsample(8, 8)

        # Menu buttons
        self.home_b = tk.Button(self.menu_lf, image=self.home_icon_inactive_resized, relief="flat", bg="#4C8404",
                                command=self.switch_home)
        self.home_b.pack(side="top")

        self.account_b = tk.Button(self.menu_lf, image=self.accounts_icon_inactive_resized, relief="flat", bg="#4C8404",
                                   command=self.switch_account)
        self.account_b.pack(side="top", fill="both")

        self.loan_b = tk.Button(self.menu_lf, image=self.loans_icon_inactive_resized, relief="flat", bg="#4C8404",
                                command=self.switch_loan)
        self.loan_b.pack(side="top")

        self.payment_b = tk.Button(self.menu_lf, image=self.payments_icon_inactive_resized, relief="flat", bg="#4C8404",
                                   command=self.switch_payment)
        self.payment_b.pack(side="top", fill="both")

        exit_b = tk.Button(self.menu_lf, image=self.exit_inactive_resized, relief="flat", bg="#4C8404",
                           command=self.switch_exit)
        exit_b.pack(side="top", fill="both")

        # Content Container
        self.body_lf = tk.LabelFrame(self.master, relief="flat")
        self.body_lf.pack(side="left", fill="both", expand="true")

        # ================================================ Toolbar Section =============================================
        toolbar_lf = tk.LabelFrame(self.body_lf, bg="#FFFFFF", relief="flat")
        toolbar_lf.pack(side="top", fill="x", ipadx=100)

        ttk.Label(toolbar_lf, text="P2P Lending Management System",
                  style="heading.TLabel").pack(side="left", padx=5, pady=5)

        ttk.Label(toolbar_lf, text="|", style="heading.TLabel").pack(side="left")

        add_people_b = tk.Button(toolbar_lf, text="Add borrower", font="OpenSans, 10", fg="#FFFFFF",
                                 bg="#4C8404", relief="flat", command=self.add_people)
        add_people_b.pack(side="left", padx=5, pady=5)

        generate_contract_b = tk.Button(toolbar_lf, text="Generate Contract", font="OpenSans, 10", fg="#FFFFFF",
                                        bg="#4C8404", relief="flat", command=self.generate_contract)
        generate_contract_b.pack(side="left", padx=5, pady=5)

        export_data_b = tk.Button(toolbar_lf, text="Export Data", font="OpenSans, 10", fg="#FFFFFF",
                                  bg="#4C8404", relief="flat", command=self.export_database_widget)
        export_data_b.pack(side="left", padx=5, pady=5)

        ttk.Label(toolbar_lf, text="|", style="heading.TLabel").pack(side="left")

        link_small_claims_l = ttk.Label(toolbar_lf, text="Delinquent borrowers? Click here.",
                                        cursor="hand2", style="link.TLabel")
        link_small_claims_l.pack(side="left")

        ttk.Label(toolbar_lf, text="|", style="h1_footnote.TLabel").pack(side="left")

        link_fair_debt_l = ttk.Label(toolbar_lf, text="Read: Fair Debt Collection Practices Act",
                                     cursor="hand2", style="link.TLabel")
        link_fair_debt_l.pack(side="left")

        logout_b = tk.Button(toolbar_lf, text="Logout", font="OpenSans, 10", relief="flat", bg="#FFFFFF",
                             fg="green", highlightcolor="#2C441D", command=self.login_win)
        logout_b.pack(side="right", pady=5)

        ttk.Label(toolbar_lf, text=(lms_version, "|"),
                  style="h1_footnote.TLabel").pack(side="right", anchor="w", pady=5)

        # Contents container
        self.content_lf = tk.LabelFrame(self.body_lf, relief="flat")
        self.content_lf.pack(side="left", fill="both", expand="true")

        # Initialize switch_home method for the default content
        self.switch_home()

        # Create tooltip
        tt.create_ToolTip(add_people_b, "Click to add borrower account")
        tt.create_ToolTip(generate_contract_b, "Click to generate contract")
        tt.create_ToolTip(export_data_b, "Click to export data")

        tt.create_ToolTip(self.home_b, "Click to switch to home section")
        tt.create_ToolTip(self.account_b, "Click to switch to accounts section")
        tt.create_ToolTip(self.loan_b, "Click to switch to loans section")
        tt.create_ToolTip(self.payment_b, "Click to switch to payment section")
        tt.create_ToolTip(exit_b, "Click to exit ")

        link_small_claims_l.bind("<Button-1>", lambda e: webbrowser.open_new_tab(url_small_claims))
        link_fair_debt_l.bind("<Button-1>", lambda e: webbrowser.open_new_tab(url_fair_debt))

    def switch_home(self):
        # Destroy content_lf
        Content.destroy_content(self.content_lf)

        # Scrollable home container
        self.home_f = ScrollableFrame(self.content_lf)

        # ================================================ Loan Analytics ==============================================
        # Containers for loan analytics
        loans_analytics_f = tk.Frame(self.home_f.scrollable_frame, relief="flat", bg="#FFFFFF")
        loans_analytics_f.pack(side="top", fill="both", padx=10, pady=5, expand=True)

        # ================================================ Filter section ==============================================
        loan_analytics_filter_lf = tk.LabelFrame(loans_analytics_f, bg="#FFFFFF")
        loan_analytics_filter_lf.pack(side="top", fill="both", padx=10, pady=10, ipady=10, expand=True)

        # Content for payment analytics
        ttk.Label(loan_analytics_filter_lf, text="Filter",
                  style="h1_title.TLabel").grid(column=0, row=0, rowspan=2, columnspan=2, pady=5, sticky="w")

        filter_analytics_b = tk.Button(loan_analytics_filter_lf, text="Filter Analytics",
                                       font="OpenSans, 10", fg="#FFFFFF",
                                       bg="#4C8404", relief="flat", command=self.filter_analytics)
        filter_analytics_b.grid(column=2, row=0, rowspan=2)

        filter_default_b = tk.Button(loan_analytics_filter_lf, text="Default filters",
                                     font="OpenSans, 10", fg="#4C8404",
                                     bg="#D4DEC9", relief="flat", command=self.switch_home)
        filter_default_b.grid(column=3, columnspan=2, row=0, rowspan=2)

        ttk.Label(loan_analytics_filter_lf, text="Date from",
                  style="body.TLabel").grid(column=0, row=2, padx=2.5, sticky="w")

        self.dashboard_main_filter_from = DateEntry(loan_analytics_filter_lf, width=15,
                                                    date_pattern="MM/dd/yy", borderwidth=2)
        self.dashboard_main_filter_from.grid(column=1, columnspan=2, row=2, padx=2.5, sticky="w")

        ttk.Label(loan_analytics_filter_lf, text="to", style="body.TLabel").grid(column=3, row=2, padx=2.5, sticky="w")

        self.dashboard_main_filter_to = DateEntry(loan_analytics_filter_lf, width=15,
                                                  date_pattern="MM/dd/yy", borderwidth=2)
        self.dashboard_main_filter_to.grid(column=4, columnspan=2, row=2, padx=2.5, sticky="w")

        # Insert values to Date Entry
        self.dashboard_main_filter_from.delete(0, "end")
        self.dashboard_main_filter_from.insert(0, fday_month)

        self.dashboard_main_filter_to.delete(0, "end")
        self.dashboard_main_filter_to.insert(0, currentday_month)

        # ================================================ Menu section ================================================
        loan_analytics_menu = tk.LabelFrame(loans_analytics_f, bg="#FFFFFF", relief="flat")
        loan_analytics_menu.pack(side="top", fill="both", expand=True)

        # Content for payment analytics
        ttk.Label(loan_analytics_menu, text="Loan Analytics",
                  style="heading.TLabel").grid(column=0, row=1, columnspan=2, pady=5, sticky="w")

        # Dashboard information
        ttk.Label(loan_analytics_menu, text="Total loan amount:",
                  style="body.TLabel").grid(column=0, row=2, columnspan=2, pady=5, sticky="w")

        self.loan_amount_l = ttk.Label(loan_analytics_menu, style="body_content.TLabel")
        self.loan_amount_l.grid(column=2, row=2, pady=5, sticky="w")

        ttk.Label(loan_analytics_menu, text="Number of loans:",
                  style="body.TLabel").grid(column=0, row=3, columnspan=2, pady=5, sticky="w")

        self.loan_count_l = ttk.Label(loan_analytics_menu, style="body_content.TLabel")
        self.loan_count_l.grid(column=2, row=3, pady=5, sticky="w")

        # ================================================ Content section =============================================
        self.loan_analytics_content = tk.LabelFrame(loans_analytics_f, bg="#FFFFFF", relief="flat")
        self.loan_analytics_content.pack(side="top", fill="both", expand=True)

        # Initialize method for loans analytics
        self.mysql_pandas_loans()

        # Wrap contents to allow scrollable frame function
        self.home_f.pack(side="top", fill="both", expand=True)

        # Button for showing more dashboards
        self.show_more_dashboard_b = tk.Button(self.home_f.scrollable_frame, text="Show more analytics",
                                               font="OpenSans, 10", fg="#FFFFFF", bg="#4C8404", relief="flat",
                                               command=self.show_more_analytics)
        self.show_more_dashboard_b.pack(side="bottom", fill="both", expand=True, padx=10, pady=10)

        # Create tooltip
        tt.create_ToolTip(filter_analytics_b, "Click to implement custom filters ")
        tt.create_ToolTip(filter_default_b, "Click to implement default filters")

        # Configure button state
        self.state_button()
        self.home_b.configure(image=self.home_icon_active_resized)

    def show_more_analytics(self):
        # ================================================ Payment Analytics ===========================================
        # Containers for payment analytics
        payment_analytics_f = tk.Frame(self.home_f.scrollable_frame, bg="#FFFFFF", relief="flat")
        payment_analytics_f.pack(side="top", padx=10, pady=5, fill="both", expand=True)

        payment_analytics_menu = tk.LabelFrame(payment_analytics_f, bg="#FFFFFF", relief="flat")
        payment_analytics_menu.pack(side="top", pady=10, fill="both", expand=True)

        self.payment_analytics_content = tk.LabelFrame(payment_analytics_f, bg="#FFFFFF", relief="flat")
        self.payment_analytics_content.pack(side="top", pady=10, fill="both", expand=True)

        # Content for payment analytics
        ttk.Label(payment_analytics_menu, text="Payment Analytics",
                  style="heading.TLabel").grid(column=0, row=0, columnspan=2, pady=5, sticky="w")

        # Dashboard information
        ttk.Label(payment_analytics_menu, text="Total payment amount",
                  style="body.TLabel").grid(column=0, row=2, columnspan=2, pady=5, sticky="w")

        self.payment_amount_l = ttk.Label(payment_analytics_menu, style="body_content.TLabel")
        self.payment_amount_l.grid(column=2, row=2, pady=5, sticky="w")

        ttk.Label(payment_analytics_menu, text="Number of payments",
                  style="body.TLabel").grid(column=0, row=3, columnspan=2, pady=5, sticky="w")

        self.payment_count_l = ttk.Label(payment_analytics_menu, style="body_content.TLabel")
        self.payment_count_l.grid(column=2, row=3, pady=5, sticky="w")

        # Initialize method for payment analytics
        self.mysql_pandas_payment()

        self.show_more_dashboard_b.configure(text="Show less analytics", command=self.switch_home)

    def switch_account(self):
        # Destroy content_lf
        Content.destroy_content(self.content_lf)

        # Profile container
        self.account_lf = tk.LabelFrame(self.content_lf, relief="flat")
        self.account_lf.pack(fill="both", expand=True)

        # Profile view database container
        self.account_database_view_lf = tk.LabelFrame(self.account_lf, bg="#FFFFFF", relief="flat")
        self.account_database_view_lf.pack(side="top", pady=10, fill="both")

        # ================================================ Filter section ==============================================
        filter_lf = tk.LabelFrame(self.account_database_view_lf, bg="#FFFFFF")
        filter_lf.pack(side="top", fill="both", padx=10, pady=10, ipady=5, expand=True)

        # Content for payment analytics
        ttk.Label(filter_lf, text="Accounts Datasheet", style="h1_title.TLabel").pack(side="top", anchor="nw", padx=10)

        filter_cb_lf = tk.LabelFrame(filter_lf, bg="#D4DEC9", relief="flat")
        filter_cb_lf.pack(side="top", anchor="sw", ipadx=5, padx=10)

        ttk.Label(filter_cb_lf, text="Filter", style="filter.TLabel").grid(column=0, row=0, sticky="w")

        filter_account_value = ['Borrower ID', 'Alphabetical', 'Date']
        self.filter_account_cb = ttk.Combobox(filter_cb_lf, width=15, state="readonly", font="8",
                                              values=filter_account_value)
        self.filter_account_cb.current(0)
        self.filter_account_cb.bind("<<ComboboxSelected>>", self.filter_account_cb_clicked)
        self.filter_account_cb.grid(column=1, row=0, columnspan=2, sticky="e")

        # ================================================ Datasheet section ===========================================
        self.account_database_view_f = tk.Frame(self.account_database_view_lf, relief="flat")
        self.account_database_view_f.pack(side="top", fill="both")

        self.account_database_view_scr = tk.Scrollbar(self.account_database_view_f)
        self.account_database_view_scr.pack(side="right", fill="y")

        # Create tree
        self.account_borrower_lb = ttk.Treeview(self.account_database_view_f, style="default.Treeview",
                                                yscrollcommand=self.account_database_view_scr.set)

        self.account_database_view_scr.configure(command=self.account_borrower_lb.yview)

        # Define column
        self.account_borrower_lb["columns"] = ("Borrower ID", "Name", "Address", "Age", "Gender", "Date created")

        # Format column
        self.account_borrower_lb.column("#0", width=0, stretch="no")
        self.account_borrower_lb.column("Borrower ID", anchor="center", width=50)
        self.account_borrower_lb.column("Name", anchor="w", width=80)
        self.account_borrower_lb.column("Address", anchor="w", width=120)
        self.account_borrower_lb.column("Age", anchor="center", width=50)
        self.account_borrower_lb.column("Gender", anchor="center", width=50)
        self.account_borrower_lb.column("Date created", anchor="center", width=50)

        # Create headings
        self.account_borrower_lb.heading("#0", text="", anchor="w")
        self.account_borrower_lb.heading("Borrower ID", text="Borrower ID", anchor="center")
        self.account_borrower_lb.heading("Name", text="Name", anchor="w")
        self.account_borrower_lb.heading("Address", text="Address", anchor="w")
        self.account_borrower_lb.heading("Age", text="Age", anchor="center")
        self.account_borrower_lb.heading("Gender", text="Gender", anchor="center")
        self.account_borrower_lb.heading("Date created", text="Date created", anchor="center")

        self.account_borrower_lb.pack(side="left", fill="both", expand=True)

        # Bind the treeview to database_view_info method
        self.account_borrower_lb.bind("<ButtonRelease-1>", self.database_view_account_info)

        # Initialize method for viewing accounts database
        self.database_view_account("Borrower ID")

        # Profile view database container
        self.account_content_view_lf = tk.LabelFrame(self.account_lf, bg="#FFFFFF", relief="flat")
        self.account_content_view_lf.pack(side="top", pady=10, fill="both")

        ttk.Label(self.account_content_view_lf, text="Account Information",
                  style="heading.TLabel").grid(column=0, row=0, columnspan=2, pady=5, sticky="w")

        ttk.Label(self.account_content_view_lf, text="No information available",
                  style="body.TLabel").grid(column=0, row=1, padx=5, pady=5, sticky="w")

        # Configure button state
        self.state_button()
        self.account_b.configure(image=self.accounts_icon_active_resized)

    def database_view_account(self, filter_value):
        if filter_value == "Alphabetical":
            self.database_connect()
            self.mycursor.execute("SELECT borrower.borrowerid, borrower.name, borrower.address, borrower.age,"
                                  "borrower.gender, borrower.created "
                                  "FROM borrower where userid = ' "
                                  + self.key_str + "' ORDER BY borrower.name;")
        elif filter_value == "Date":
            self.database_connect()
            self.mycursor.execute("SELECT borrower.borrowerid, borrower.name, borrower.address, borrower.age,"
                                  "borrower.gender, borrower.created "
                                  "FROM borrower where userid = ' "
                                  + self.key_str + "' ORDER BY borrower.created;")
        else:
            self.database_connect()
            self.mycursor.execute("SELECT borrower.borrowerid, borrower.name, borrower.address, borrower.age,"
                                  "borrower.gender, borrower.created "
                                  "FROM borrower where userid = ' "
                                  + self.key_str + "' ORDER BY borrower.borrowerid;")

        borrowers = self.mycursor.fetchall()
        print(borrowers)

        # Clear treeview
        Content.clear_treeview(self.account_borrower_lb)

        # Create configure for striped rows
        self.account_borrower_lb.tag_configure("oddrow", background="#FFFFFF")
        self.account_borrower_lb.tag_configure("evenrow", background="#FAFAFA")
        count = 0
        for record in borrowers:
            if count % 2 == 0:
                self.account_borrower_lb.insert(parent="", index="end", iid=count, text="",
                                                values=(record[0], record[1], record[2], record[3], record[4],
                                                        record[5]), tags=("oddrow",))
            else:
                self.account_borrower_lb.insert(parent="", index="end", iid=count, text="",
                                                values=(record[0], record[1], record[2], record[3], record[4],
                                                        record[5]), tags=("evenrow",))
            count += 1

        self.db1.commit()
        self.mycursor.close()
        self.db1.close()

    def filter_account_cb_clicked(self, event):
        if self.filter_account_cb.get() == "Date":
            self.database_view_account("Date")
        else:
            self.database_view_account("Alphabetical")
        print(event)

    def switch_loan(self):
        # Destroy content_lf
        Content.destroy_content(self.content_lf)

        # Loan container
        self.loan_lf = tk.LabelFrame(self.content_lf, relief="flat")
        self.loan_lf.pack(fill="both", expand=True)

        # Loan view database container
        self.loan_database_view_lf = tk.LabelFrame(self.loan_lf, bg="#FFFFFF", relief="flat")
        self.loan_database_view_lf.pack(side="top", pady=10, fill="both")

        # ================================================ Filter section ==============================================
        filter_lf = tk.LabelFrame(self.loan_database_view_lf, bg="#FFFFFF")
        filter_lf.pack(side="top", fill="both", padx=10, pady=10, ipady=5, expand=True)

        # Content for loans analytics
        ttk.Label(filter_lf, text="Loan Datasheet", style="h1_title.TLabel").pack(side="top", anchor="nw", padx=10)

        filter_cb_lf = tk.LabelFrame(filter_lf, bg="#D4DEC9", relief="flat")
        filter_cb_lf.pack(side="top", anchor="sw", ipadx=5, padx=10)

        ttk.Label(filter_cb_lf, text="Filter", style="filter.TLabel").grid(column=0, row=0, sticky="w")

        filter_loan_value = ['Loan ID', 'Alphabetical', 'Status', 'Date']
        self.filter_loan_cb = ttk.Combobox(filter_cb_lf, width=15, state="readonly", font="8", values=filter_loan_value)
        self.filter_loan_cb.current(2)
        self.filter_loan_cb.bind("<<ComboboxSelected>>", self.filter_loan_cb_clicked)
        self.filter_loan_cb.grid(column=1, row=0, columnspan=2, sticky="e")

        # ================================================ Loan view section ===========================================
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
                                            "Status", "Balance")

        # Format column
        self.loan_borrower_lb.column("#0", width=0, stretch="no")
        self.loan_borrower_lb.column("Loan ID", anchor="center", width=50)
        self.loan_borrower_lb.column("Name", anchor="w", width=80)
        self.loan_borrower_lb.column("Amount", anchor="center", width=50)
        self.loan_borrower_lb.column("Interest", anchor="center", width=50)
        self.loan_borrower_lb.column("(n) days", anchor="center", width=50)
        self.loan_borrower_lb.column("Date issued", anchor="center", width=50)
        self.loan_borrower_lb.column("Status", anchor="center", width=50)
        self.loan_borrower_lb.column("Balance", anchor="center", width=50)

        # Create headings
        self.loan_borrower_lb.heading("#0", text="", anchor="w")
        self.loan_borrower_lb.heading("Loan ID", text="Loan ID", anchor="center")
        self.loan_borrower_lb.heading("Name", text="Name", anchor="w")
        self.loan_borrower_lb.heading("Amount", text="Amount", anchor="center")
        self.loan_borrower_lb.heading("Interest", text="Interest (%)", anchor="center")
        self.loan_borrower_lb.heading("(n) days", text="Interest per (n) days", anchor="center")
        self.loan_borrower_lb.heading("Date issued", text="Date issued", anchor="center")
        self.loan_borrower_lb.heading("Status", text="Status", anchor="center")
        self.loan_borrower_lb.heading("Balance", text="Balance", anchor="center")

        self.loan_borrower_lb.pack(side="left", fill="both", expand=True)

        # Bind the treeview to database_view_info method
        self.loan_borrower_lb.bind("<ButtonRelease-1>", self.database_view_loan_info)

        # Initialize method for viewing accounts database
        self.database_view_loan("Status")

        # ================================================ Loan info section ===========================================
        self.loan_content_view_lf = tk.LabelFrame(self.loan_lf, bg="#FFFFFF", relief="flat")
        self.loan_content_view_lf.pack(side="top", pady=10, fill="both")

        ttk.Label(self.loan_content_view_lf, text="Loan Information",
                  style="heading.TLabel").grid(column=0, row=0, columnspan=2, pady=5, sticky="w")

        ttk.Label(self.loan_content_view_lf, text="No information available",
                  style="body.TLabel").grid(column=0, row=1, padx=5, pady=5, sticky="w")

        # Configure button state
        self.state_button()
        self.loan_b.configure(image=self.loans_icon_active_resized)

    def database_view_loan(self, filter_value):
        if filter_value == "Loan ID":
            self.database_connect()
            self.mycursor.execute("SELECT loan.loanid, borrower.name, loan.amount, loan.interest, loan.days,"
                                  " loan.dateissued, loan.status, borrower.userid, loan.balance"
                                  " FROM loan INNER JOIN borrower ON"
                                  " loan.borrowerid=borrower.borrowerid "
                                  "where borrower.userid = '" + self.key_str + "' ORDER BY loan.loanid;")
        elif filter_value == "Alphabetical":
            self.database_connect()
            self.mycursor.execute("SELECT loan.loanid, borrower.name, loan.amount, loan.interest, loan.days,"
                                  " loan.dateissued, loan.status, borrower.userid, loan.balance"
                                  " FROM loan INNER JOIN borrower ON"
                                  " loan.borrowerid=borrower.borrowerid "
                                  "where borrower.userid = '" + self.key_str + "' ORDER BY borrower.name;")
        elif filter_value == "Date":
            self.database_connect()
            self.mycursor.execute("SELECT loan.loanid, borrower.name, loan.amount, loan.interest, loan.days,"
                                  " loan.dateissued, loan.status, borrower.userid, loan.balance"
                                  " FROM loan INNER JOIN borrower ON"
                                  " loan.borrowerid=borrower.borrowerid "
                                  "where borrower.userid = '" + self.key_str + "' ORDER BY loan.dateissued;")
        else:
            self.database_connect()
            self.mycursor.execute("SELECT loan.loanid, borrower.name, loan.amount, loan.interest, loan.days,"
                                  " loan.dateissued, loan.status, borrower.userid, loan.balance"
                                  " FROM loan INNER JOIN borrower ON"
                                  " loan.borrowerid=borrower.borrowerid "
                                  "where borrower.userid = '" + self.key_str + "' ORDER BY loan.status;")

        loans = self.mycursor.fetchall()

        print(loans)

        # Clear treeview
        Content.clear_treeview(self.loan_borrower_lb)

        # Create configure for striped rows
        self.loan_borrower_lb.tag_configure("oddrow", background="#FFFFFF")
        self.loan_borrower_lb.tag_configure("evenrow", background="#FAFAFA")
        count = 0
        for record in loans:
            if count % 2 == 0:
                self.loan_borrower_lb.insert(parent="", index="end", iid=count, text="",
                                             values=(record[0], record[1], record[2], record[3], record[4],
                                                     record[5], record[6], record[8]),
                                             tags=("oddrow",))
            else:
                self.loan_borrower_lb.insert(parent="", index="end", iid=count, text="",
                                             values=(record[0], record[1], record[2], record[3], record[4],
                                                     record[5], record[6], record[8]),
                                             tags=("evenrow",))
            count += 1

        self.db1.commit()
        self.mycursor.close()
        self.db1.close()

    def filter_loan_cb_clicked(self, event):
        if self.filter_loan_cb.get() == "Loan ID":
            self.database_view_loan("Loan ID")
        elif self.filter_loan_cb.get() == "Alphabetical":
            self.database_view_loan("Alphabetical")
        else:
            self.database_view_loan("Status")
        print(event)

    def switch_payment(self):
        # Destroy content_lf
        Content.destroy_content(self.content_lf)

        # Payment container
        self.payment_lf = tk.LabelFrame(self.content_lf, relief="flat")
        self.payment_lf.pack(fill="both", expand=True)

        # Payment view database container
        self.payment_database_view_lf = tk.LabelFrame(self.payment_lf, bg="#FFFFFF", relief="flat")
        self.payment_database_view_lf.pack(side="top", pady=10, fill="both")

        # ================================================ Filter section ==============================================
        filter_lf = tk.LabelFrame(self.payment_database_view_lf, bg="#FFFFFF")
        filter_lf.pack(side="top", fill="both", padx=10, pady=10, ipady=5, expand=True)

        # Content for payment analytics
        ttk.Label(filter_lf, text="Payment Datasheet", style="h1_title.TLabel").pack(side="top", anchor="nw", padx=10)

        filter_cb_lf = tk.LabelFrame(filter_lf, bg="#D4DEC9", relief="flat")
        filter_cb_lf.pack(side="top", anchor="sw", ipadx=5, padx=10)

        ttk.Label(filter_cb_lf, text="Filter", style="filter.TLabel").grid(column=0, row=0, sticky="w")

        filter_payment_value = ['Loan ID', 'Alphabetical', 'Date']
        self.filter_payment_cb = ttk.Combobox(filter_cb_lf, width=15, state="readonly", font="8",
                                              values=filter_payment_value)
        self.filter_payment_cb.current(2)
        self.filter_payment_cb.bind("<<ComboboxSelected>>", self.filter_payment_cb_clicked)
        self.filter_payment_cb.grid(column=1, row=0, columnspan=2, sticky="e")

        # ================================================ Datasheet section ===========================================
        self.payment_database_view_f = tk.Frame(self.payment_database_view_lf, relief="flat")
        self.payment_database_view_f.pack(side="top", fill="both")

        self.payment_database_view_scr = tk.Scrollbar(self.payment_database_view_f)
        self.payment_database_view_scr.pack(side="right", fill="y")

        # Create tree
        self.payment_borrower_lb = ttk.Treeview(self.payment_database_view_f, style="default.Treeview",
                                                yscrollcommand=self.payment_database_view_scr.set)

        self.payment_database_view_scr.configure(command=self.payment_borrower_lb.yview)

        # Define column
        self.payment_borrower_lb["columns"] = ("Payment ID", "Loan ID", "Name", "Loan principal", "Payment",
                                               "Remaining balance", "Date issued")

        # Format column
        self.payment_borrower_lb.column("#0", width=0, stretch="no")
        self.payment_borrower_lb.column("Payment ID", anchor="center", width=80)
        self.payment_borrower_lb.column("Loan ID", anchor="center", width=80)
        self.payment_borrower_lb.column("Name", anchor="w", width=120)
        self.payment_borrower_lb.column("Loan principal", anchor="center", width=80)
        self.payment_borrower_lb.column("Remaining balance", anchor="center", width=80)
        self.payment_borrower_lb.column("Payment", anchor="center", width=80)
        self.payment_borrower_lb.column("Date issued", anchor="center", width=80)

        # Create headings
        self.payment_borrower_lb.heading("#0", text="", anchor="w")
        self.payment_borrower_lb.heading("Payment ID", text="Payment ID", anchor="center")
        self.payment_borrower_lb.heading("Loan ID", text="Loan ID", anchor="center")
        self.payment_borrower_lb.heading("Name", text="Name", anchor="w")
        self.payment_borrower_lb.heading("Loan principal", text="Loan principal", anchor="center")
        self.payment_borrower_lb.heading("Payment", text="Payment", anchor="center")
        self.payment_borrower_lb.heading("Remaining balance", text="Remaining balance", anchor="center")
        self.payment_borrower_lb.heading("Date issued", text="Date issued", anchor="center")

        self.payment_borrower_lb.pack(side="left", fill="both", expand=True)

        # Bind the treeview to database_view_info method
        # self.payment_borrower_lb.bind("<ButtonRelease-1>", self.database_view_account_info)

        # Initialize method for viewing accounts database
        self.database_view_payment("Date")

        # Profile view database container
        self.payment_content_view_lf = tk.LabelFrame(self.payment_lf, bg="#FFFFFF", relief="flat")
        self.payment_content_view_lf.pack(side="top", pady=10, fill="both")

        ttk.Label(self.payment_content_view_lf, text="Payment Information",
                  style="heading.TLabel").grid(column=0, row=0, columnspan=2, pady=5, sticky="w")

        ttk.Label(self.payment_content_view_lf, text="No information available",
                  style="body.TLabel").grid(column=0, row=1, padx=5, pady=5, sticky="w")

        # Configure button state
        self.state_button()
        self.payment_b.configure(image=self.payments_icon_active_resized)

    def database_view_payment(self, filter_value):
        if filter_value == "Alphabetical":
            self.database_connect()
            self.mycursor.execute("SELECT payment.paymentid, payment.loanid, borrower.name, loan.amount, "
                                  "payment.amount, loan.balance, payment.dateissued"
                                  " FROM payment INNER JOIN loan ON payment.loanid=loan.loanid "
                                  "INNER JOIN borrower ON loan.borrowerid=borrower.borrowerid where borrower.userid = "
                                  "'" + self.key_str + "' ORDER BY borrower.name;")
        elif filter_value == "Loan ID":
            self.database_connect()
            self.mycursor.execute("SELECT payment.paymentid, payment.loanid, borrower.name, loan.amount, "
                                  "payment.amount, loan.balance, payment.dateissued"
                                  " FROM payment INNER JOIN loan ON payment.loanid=loan.loanid "
                                  "INNER JOIN borrower ON loan.borrowerid=borrower.borrowerid where borrower.userid = "
                                  "'" + self.key_str + "' ORDER BY payment.loanid;")
        else:
            self.database_connect()
            self.mycursor.execute("SELECT payment.paymentid, payment.loanid, borrower.name, loan.amount, "
                                  "payment.amount, loan.balance, payment.dateissued"
                                  " FROM payment INNER JOIN loan ON payment.loanid=loan.loanid "
                                  "INNER JOIN borrower ON loan.borrowerid=borrower.borrowerid where borrower.userid = "
                                  "'" + self.key_str + "' ORDER BY payment.dateissued;")

        payments = self.mycursor.fetchall()
        print(payments)

        # Clear treeview
        Content.clear_treeview(self.payment_borrower_lb)

        # Create configure for striped rows
        self.payment_borrower_lb.tag_configure("oddrow", background="#FFFFFF")
        self.payment_borrower_lb.tag_configure("evenrow", background="#FAFAFA")
        count = 0
        for record in payments:
            if count % 2 == 0:
                self.payment_borrower_lb.insert(parent="", index="end", iid=count, text="",
                                                values=(record[0], record[1], record[2], record[3], record[4],
                                                        record[5], record[6]), tags=("oddrow",))
            else:
                self.payment_borrower_lb.insert(parent="", index="end", iid=count, text="",
                                                values=(record[0], record[1], record[2], record[3], record[4],
                                                        record[5], record[6]), tags=("evenrow",))

            count += 1

        self.db1.commit()
        self.mycursor.close()
        self.db1.close()

    def filter_payment_cb_clicked(self, event):
        if self.filter_payment_cb.get() == "Alphabetical":
            self.database_view_payment("Alphabetical")
        elif self.filter_payment_cb.get() == "Date":
            self.database_view_payment("Date")
        else:
            self.database_view_payment("Loan ID")
        print(event)

    def switch_exit(self):
        exit_yes_no = messagebox.askyesno(title="Exit", message="Are you sure you want to exit?")
        if exit_yes_no:
            self.master.destroy()
        else:
            pass

    def login_validation(self):
        if not self.login_username_entry.get():
            self.invalid_input()
        else:
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

    def register_validation(self):
        if not self.register_user_name_entry.get():
            self.invalid_input()
        if not self.register_password_entry.get():
            self.invalid_input()
        if not self.register_email_entry.get():
            self.invalid_input()
        else:
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

    def invalid_input(self):
        messagebox.showerror("Error", "Invalid input")
        # Destroy window contents
        Content.destroy_content(self.master)
        # Initializes login_win
        self.login_win()

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
        self.add_people_lf = tk.LabelFrame(self.add_people_top, padx=20, pady=20, bg="#FFFFFF", relief="flat")
        self.add_people_lf.pack(anchor="center", expand=True, fill="both")

        # Creating widgets

        ttk.Label(self.add_people_lf, text="Add Borrower",
                  style="h1.TLabel").grid(column=0, row=0, columnspan=2, pady=10, sticky="w")

        ttk.Label(self.add_people_lf, text="Name", style="h1_footnote.TLabel").grid(column=0, row=1, padx=5, pady=5,
                                                                                    sticky="w")

        self.add_people_name_entry = ttk.Entry(self.add_people_lf, width=50)
        self.add_people_name_entry.grid(column=1, row=1, padx=5, pady=5, sticky="w")

        # Focuses cursor on add name entry
        self.add_people_name_entry.focus()

        ttk.Label(self.add_people_lf, text="Address", style="h1_footnote.TLabel").grid(column=0, row=2, padx=5, pady=5,
                                                                                       sticky="w")

        self.add_people_address_entry = ttk.Entry(self.add_people_lf, width=50)
        self.add_people_address_entry.grid(column=1, row=2, padx=5, pady=5, sticky="w")

        ttk.Label(self.add_people_lf, text="Age", style="h1_footnote.TLabel").grid(column=0, row=3, padx=5, pady=5,
                                                                                   sticky="w")

        self.age_spinbox = ttk.Spinbox(self.add_people_lf, from_=0, to=200, width=5)
        self.age_spinbox.grid(column=1, row=3, padx=5, pady=5, sticky="w")

        # Combobox for gender
        ttk.Label(self.add_people_lf, text="Gender", style="h1_footnote.TLabel").grid(column=0, row=4, padx=5, pady=5,
                                                                                      sticky="w")
        self.gender_combobox = ttk.Combobox(self.add_people_lf, width=10)
        self.gender_combobox['values'] = "Male", "Female", "Others"
        self.gender_combobox.grid(column=1, row=4, padx=5, pady=5, sticky="w")
        self.gender_combobox.current(0)

        # Button for adding people to database
        cancel_add_people_b = tk.Button(self.add_people_lf, text="Add Borrower", font="OpenSans, 12", fg="#FFFFFF",
                                        bg="#4C8404", relief="flat", command=self.finish_add_people)
        cancel_add_people_b.grid(column=0, row=5, padx=5, pady=5)

        # Button for adding people to database
        finish_add_people_b = tk.Button(self.add_people_lf, text="Cancel", font="OpenSans, 12", fg="#4C8404",
                                        bg="#D4DEC9", relief="flat", command=self.add_people_top.destroy)
        finish_add_people_b.grid(column=1, row=5, padx=5, pady=5, sticky="w")

    def issue_loan(self):
        # Create instance
        self.add_people_top = tk.Toplevel(self.master)
        # self.add_people_top.geometry("500x280")
        self.add_people_top.title("Issue loan")
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
        self.issue_loan_date_de = DateEntry(self.issue_loan_lf, width=15, background='green', date_pattern="MM/dd/yy",
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
        cancel_issue_loan_b = tk.Button(self.issue_loan_lf, text="Done", font="OpenSans, 12", fg="#FFFFFF",
                                        bg="#4C8404", relief="flat", command=self.finish_issue_loan)
        cancel_issue_loan_b.grid(column=0, row=5, padx=5, pady=5)

        # Button for adding people to database
        finish_issue_loan_b = tk.Button(self.issue_loan_lf, text="Cancel", font="OpenSans, 12", fg="#4C8404",
                                        bg="#FFFFFF", relief="flat", command=self.add_people_top.destroy)
        finish_issue_loan_b.grid(column=1, row=5, padx=5, pady=5, sticky="w")

    def finish_add_people(self):
        date_now = datetime.now()
        date_now.strftime("%m/%d/%Y")
        try:
            self.database_connect()
            self.mycursor.execute(
                "INSERT INTO borrower (userid, name, address, age, created, gender) VALUES (%s, %s,%s,"
                "%s,%s,%s)",
                (self.key, self.add_people_name_entry.get(), self.add_people_address_entry.get(),
                 self.age_spinbox.get(), date_now, self.gender_combobox.get()))
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
        # Computation for balance
        balance = (int(self.issue_loan_interest_sb.get()) / 100) * (int(self.issue_loan_amount_sb.get()))
        balance = balance + int(self.issue_loan_amount_sb.get())
        balance = str(balance)
        print(balance)

        # Computation for balance due date
        date_issued = datetime.strptime(self.issue_loan_date_de.get(), "%x")
        date_issued_plus_delta_time = date_issued + timedelta(days=int(self.issue_loan_days_sb.get()))
        print("Due Date: ", date_issued_plus_delta_time)

        try:
            self.database_connect()

            self.mycursor.execute(
                "INSERT INTO loan (borrowerid, userid, amount, interest, days, created, dateissued, status, balance, "
                "duedate)"
                " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (self.borrower_key_str, self.key_str, self.issue_loan_amount_sb.get(),
                 self.issue_loan_interest_sb.get(), self.issue_loan_days_sb.get(), datetime.now(),
                 self.issue_loan_date_de.get(), self.status_combobox.get(), balance, date_issued_plus_delta_time))

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

    def export_database_widget(self):
        # Create instance
        self.export_data_top = tk.Toplevel(self.master)
        self.export_data_top.title("Export data")
        # export_data_top.geometry("500x400")
        self.export_data_top.configure(bg="#4C8404")
        self.export_data_top.resizable(False, False)

        # ================================================ Checkbox for available tables ===============================
        # Export data container
        export_data_lf = tk.LabelFrame(self.export_data_top, padx=20, pady=20, bg="#FFFFFF", relief="flat")
        export_data_lf.pack(side="top", padx=15, pady=15, fill="both", expand=True)

        ttk.Label(export_data_lf, text="Available tables", style="body_content.TLabel").grid(column=0, row=0,
                                                                                             padx=5, sticky="w")

        borrower_cb = tk.Checkbutton(export_data_lf, text="Borrowers", variable=self.borrower_value, onvalue=1,
                                     offvalue=0, bg="#FFFFFF")
        borrower_cb.grid(column=0, row=1, padx=5, sticky="w")

        loan_cb = tk.Checkbutton(export_data_lf, text="Loans", variable=self.loan_value, onvalue=1, offvalue=0,
                                 bg="#FFFFFF")
        loan_cb.grid(column=0, row=2, padx=5, sticky="w")

        payment_cb = tk.Checkbutton(export_data_lf, text="Payments", variable=self.payment_value, onvalue=1, offvalue=0,
                                    bg="#FFFFFF")
        payment_cb.grid(column=0, row=3, padx=5, sticky="w")

        # Buttons for export
        export_csv_b = tk.Button(export_data_lf, text="Export as csv", font="OpenSans, 10", fg="#FFFFFF",
                                 bg="#4C8404", relief="flat", command=self.export_as_csv)
        export_csv_b.grid(column=0, row=4, padx=5, pady=5, sticky="w")

        export_excel_b = tk.Button(export_data_lf, text="Export as excel", font="OpenSans, 10", fg="#FFFFFF",
                                   bg="#4C8404", relief="flat")
        export_excel_b.grid(column=2, row=4, padx=5, sticky="w")

        # Disables underlying window
        self.export_data_top.grab_set()

        self.export_data_top.mainloop()

    def import_database(self):
        read_guide = tkinter.messagebox.askquestion("Import file", "Do you want to read importing guide before"
                                                                   " proceeding to file dialog?")
        if read_guide == "yes":
            os.startfile(r"Guide for importing database.pdf")
        else:
            import_filename = filedialog.askopenfilename(title="Open a file", initialdir="/")
            col_list = ["NAME"]
            import_df = pd.read_excel(import_filename, usecols=col_list)
            pd.set_option("display.max_rows", None)
            # Create new dataframe with UPPERCASE values
            upper_df = import_df.apply(lambda x: x.astype(str).str.upper())
            # Drop values duplicate values
            upper_df.drop_duplicates(subset="NAME", keep="first", inplace=True)
            print(upper_df)
            print(import_df.isnull().sum())

    def export_as_csv(self):
        pandasdb = mysql.connect(host=host,
                                 user=user,
                                 password=password,
                                 database="lmsdatabase",
                                 use_pure=True)

        if self.borrower_value.get() == 1:
            query1 = "Select * from lmsdatabase.borrower where userid = '" + self.key_str + "';"
            df1 = pd.read_sql(query1, pandasdb)
            print(df1)
            save_file = filedialog.asksaveasfile(filetypes=[('CSV file', '*.csv')], defaultextension='CSV file',
                                                 title="Save data")
            df1.to_csv(save_file, index=False)

            save_file.close()

            print("Borrower CSV is exported successfully")
        if self.loan_value.get() == 1:
            query1 = "Select * from lmsdatabase.loan where userid = '" + self.key_str + "';"
            df2 = pd.read_sql(query1, pandasdb)
            print(df2)
            save_file1 = filedialog.asksaveasfile(filetypes=[('CSV file', '*.csv')], defaultextension='CSV file',
                                                  title="Save data")
            df2.to_csv(save_file1, index=False)
            save_file1.close()
            print("Loan CSV is exported successfully")
        if self.payment_value.get() == 1:
            query1 = "SELECT payment.paymentid, payment.amount, payment.balance, payment.dateissued," \
                     " loan.loanid FROM lmsdatabase.payment  INNER JOIN loan ON payment.loanid =" \
                     " loan.loanid where loan.userid = '" + self.key_str + "'; "
            df2 = pd.read_sql(query1, pandasdb)
            print(df2)
            save_file1 = filedialog.asksaveasfile(filetypes=[('CSV file', '*.csv')], defaultextension='CSV file',
                                                  title="Save data")
            df2.to_csv(save_file1, index=False)
            save_file1.close()
            print("Loan CSV is exported successfully")
        else:
            print("Borrower table is not checked")

        pandasdb.close()
        self.export_data_top.destroy()

    def register_payment(self):
        # Create instance
        self.add_people_top = tk.Toplevel(self.master)
        # self.add_people_top.geometry("500x280")
        self.add_people_top.title("Register payment")
        self.add_people_top.configure(bg="#FFFFFF")

        # Loan info container
        self.rp_info_lf = tk.LabelFrame(self.add_people_top, padx=20, pady=20, relief="flat", background="#FFFFFF")
        self.rp_info_lf.pack(side="top", expand=True, fill="both")

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

        ttk.Label(self.rp_info_lf, text="Date issued",
                  style="body.TLabel").grid(column=0, row=7, columnspan=2, padx=5, pady=5, sticky="w")

        self.loan_content_date_issued_cal = DateEntry(self.rp_info_lf, width=12, background='green',
                                                      date_pattern="MM/dd/yyyy", foreground='white', borderwidth=2)
        self.loan_content_date_issued_cal.grid(column=1, row=7, columnspan=2, padx=5, pady=5, sticky="w")

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
        self.rp_info_balance_l.configure(text=values[7])
        self.rp_info_recommend_pay_l.configure(text=(int(values[7]) / 100) * int(values[3]))
        # Register payment buttons container
        self.rp_buttons_lf = tk.LabelFrame(self.add_people_top, padx=20, pady=20, relief="flat", background="#FFFFFF")
        self.rp_buttons_lf.pack(side="top", expand=True, fill="both")

        # Button for registering payment
        self.register_payment_done_b = tk.Button(self.rp_buttons_lf, text="Done", font="OpenSans, 10",
                                                 fg="#FFFFFF", bg="#4C8404", relief="flat",
                                                 command=self.finish_register_payment)
        self.register_payment_done_b.grid(column=0, row=0, padx=50, pady=5, sticky="w")

        # Button for updating a record
        self.register_payment_cancel_b = tk.Button(self.rp_buttons_lf, text="Cancel", font="OpenSans, 10",
                                                   fg="#FFFFFF", bg="#4C8404", relief="flat",
                                                   command=self.add_people_top.destroy)
        self.register_payment_cancel_b.grid(column=1, row=0, padx=50, pady=5, sticky="e")

        # Disables underlying window
        self.add_people_top.grab_set()

        self.add_people_top.mainloop()

    def finish_register_payment(self):
        balance = int(self.rp_info_balance_l.cget("text")) + int(self.rp_info_payment_entry.get())
        try:
            self.database_connect()

            self.mycursor.execute(
                "INSERT INTO payment (loanid, amount, balance, dateissued) VALUES (%s, %s, %s, %s)",
                (self.loan_id, self.rp_info_payment_entry.get(), balance, self.loan_content_date_issued_cal.get()))

            self.db1.commit()
            self.db1.close()
            self.mycursor.close()

            # Compute balance
            self.compute_balance()

            # Destroy add_people_top form
            self.add_people_top.destroy()

            # Show a messagebox for successfully adding people
            messagebox.showinfo("Register payment", "Payment registered successfully")

            # Updates loan window
            self.switch_loan()
        except Exception as e:
            # Deletes all entries from ttk.Entry
            Content.delete_entry(self.master)
            # Show a messagebox for unsuccessfully adding people
            messagebox.showerror("Register payment", "Did not succeed in registering payment")
            print("Could not connect to lmsdatabase")
            print(e)

    def compute_balance(self):
        try:
            # Grab record number
            selected = self.loan_borrower_lb.focus()

            # Grab record values
            values = self.loan_borrower_lb.item(selected, "values")

            balance_total = int(values[7]) - int(self.rp_info_payment_entry.get())

            self.database_connect()

            print(values[7], self.rp_info_payment_entry.get())

            if int(values[7]) <= int(self.rp_info_payment_entry.get()):
                self.mycursor.execute(
                    "UPDATE loan SET balance = 0, status = 'Fully Amortized' WHERE loanid = '" + self.loan_id + "';")
            else:
                self.mycursor.execute(
                    "UPDATE loan SET balance = '" + str(balance_total) + "' WHERE loanid = '" + self.loan_id + "';")

            print(self.loan_id)
            self.db1.commit()
            self.db1.close()
            self.mycursor.close()

            # Update account window
            self.switch_loan()

        except Exception as e:
            # Show a messagebox for unsuccessfully adding people
            messagebox.showerror("Register payment", "Did not succeed in registering payment")
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

        self.loan_content_date_issued_e = ttk.Entry(self.loan_content_view_lf, width=40)
        self.loan_content_date_issued_e.grid(column=1, row=5, columnspan=2)

        # Combobox for loan
        ttk.Label(self.loan_content_view_lf, text="Status", style="body.TLabel").grid(column=0, row=6, padx=5, pady=5,
                                                                                      sticky="w")

        self.loan_content_status_cb = ttk.Combobox(self.loan_content_view_lf, width=15)
        self.loan_content_status_cb['values'] = "Active", "Fully Amortized", "Default"
        self.loan_content_status_cb.grid(column=1, row=6, sticky="w")
        # self.loan_content_status_cb.current(0)

        # Grab record number
        selected = self.loan_borrower_lb.focus()

        # Grab record values
        values = self.loan_borrower_lb.item(selected, "values")

        # Get loan id
        self.loan_id = values[0]
        print("Loan ID:", self.loan_id)

        # Insert values to entry widgets
        self.loan_content_name_l.configure(text=values[1])
        self.loan_content_amount_e.insert(0, values[2])
        self.loan_content_interest_e.insert(0, values[3])
        self.loan_content_interest_pd_e.insert(0, values[4])
        self.loan_content_date_issued_e.insert(0, values[5])
        self.loan_content_status_cb.insert(0, values[6])

        # Instantiate method that automates adding balance based on the due date
        self.automate_adding_balance()

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

        ttk.Label(self.loan_content_view_lf, text="Remaining days until next interest:",
                  style="body.TLabel").grid(column=3, row=1, padx=5, pady=5, sticky="w")

        self.time_rem_interest_l = ttk.Label(self.loan_content_view_lf, text=self.remaining_days,
                                             style="body_content.TLabel")
        self.time_rem_interest_l.grid(column=4, row=1, padx=5, pady=5, sticky="w")

        print(event)

    def automate_adding_balance(self):
        # Computation for balance due date
        date_issued = datetime.strptime(self.loan_content_date_issued_e.get(), "%x")
        date_issued_plus_delta_time = date_issued + timedelta(days=int(self.loan_content_interest_pd_e.get()))
        print("Due Date: ", date_issued_plus_delta_time)
        self.remaining_days = date_issued_plus_delta_time - datetime.today()
        print(self.remaining_days.total_seconds())

        self.database_connect()
        self.mycursor.execute("SELECT loan.status FROM lmsdatabase.loan WHERE loan.loanid = '" + self.loan_id + "';")
        status = self.mycursor.fetchone()
        status = ''.join(status)

        # Condition for automating
        if self.remaining_days.total_seconds() <= 0 and status != "Fully Amortized":
            self.mycursor.execute("SELECT loan.interest, loan.balance, loan.days"
                                  " FROM lmsdatabase.loan WHERE loan.loanid = '"
                                  + self.loan_id + "';")
            result = self.mycursor.fetchall()
            print(result)

            # Updates the database
            for record in result:
                # Computes balance
                balance = ((record[0] / 100) * record[1])
                balance = balance + record[1]

                new_due_date = date_issued_plus_delta_time + timedelta(days=int(record[2]))
                print("New date: ", new_due_date)
                self.mycursor.execute("UPDATE lmsdatabase.loan SET loan.balance = '"
                                      + str(balance) + "', loan.duedate = '"
                                      + str(new_due_date) + "' WHERE loan.loanid = '" + self.loan_id + "';")
                self.db1.commit()

            self.db1.close()
            self.mycursor.close()
        else:
            print("Next interest not due today")

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
        self.account_content_name_e.insert(0, values[1])
        self.account_content_address_e.insert(0, values[2])
        self.account_content_age_e.insert(0, values[3])
        self.account_content_gender_e.insert(0, values[4])

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
        self.mycursor.execute("SELECT loanid FROM loan where borrowerid = '" + self.borrower_key_str + "';")
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
        # Computation for balance due date
        date_issued = datetime.strptime(self.loan_content_date_issued_e.get(), "%x")
        date_issued_plus_delta_time = date_issued + timedelta(days=int(self.loan_content_interest_pd_e.get()))
        print("Due Date: ", date_issued_plus_delta_time)

        self.database_connect()
        self.mycursor.execute(
            "UPDATE loan SET amount = '" + self.loan_content_amount_e.get() + "', interest = '"
            + self.loan_content_interest_e.get() + "', days = '"
            + self.loan_content_interest_pd_e.get() + "', dateissued = '"
            + self.loan_content_date_issued_e.get() + "', status = '"
            + self.loan_content_status_cb.get() + "', duedate = '"
            + str(date_issued_plus_delta_time) + "' WHERE loanid = '" + self.loan_id + "';")

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

    def state_button(self):
        self.home_b.configure(image=self.home_icon_inactive_resized)
        self.loan_b.configure(image=self.loans_icon_inactive_resized)
        self.account_b.configure(image=self.accounts_icon_inactive_resized)
        self.payment_b.configure(image=self.payments_icon_inactive_resized)

    def filter_analytics(self):
        # Initialize methods for displaying analytics
        self.mysql_pandas_loans()
        self.mysql_pandas_payment()

    @staticmethod
    def generate_contract():
        tkinter.messagebox.showinfo("Note!", "We are in no way affiliated with the website or its developers.\n"
                                             "Here is the link for our recommended website:\n"
                                             "(https://www.wonder.legal/ph/creation-modele/loan-agreement-ph)\n")
        webbrowser.open_new(r"https://www.wonder.legal/ph/creation-modele/loan-agreement-ph")


if __name__ == '__main__':
    win = tk.Tk()
    initialize = Window(win)

    win.mainloop()
