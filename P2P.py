from addPeople import *
import mysql.connector
from MenuSwitch import Switch
import tkinter as tk
from tkinter import ttk

"""
# Connecting to mysql database
db = mysql.connector.connect(
    host="localhost",
    user="PongoDev",
    password="PongoDev44966874",
    database="LMSdatabase"
)
mycursor = db.cursor()
mycursor.execute("CREATE DATABASE LMSdatabase")

mycursor.execute("DROP TABLE Borrower")
mycursor.execute("CREATE TABLE Borrower (borrowerID int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), "
                 "address VARCHAR(50),"
                 "created datetime, gender VARCHAR(6), age smallint(2) UNSIGNED)")



mycursor.execute("DESCRIBE Borrower")
for x in mycursor:
    print(x)
"""

global content_lf


class Window:

    def __init__(self):
        # Create instance
        self.win = tk.Tk()

        # Add a title
        self.win.title("P2P Lending Management System")
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        self.win.geometry("%dx%d" % (width, height))
        self.win.configure(bg="#FFFFFF")

        # Add widgets
        self.create_widgets()

        # Method for creating widgets

    def create_widgets(self):
        # Menu container
        menu_lf = tk.LabelFrame(self.win, bg="#FFFFFF")
        menu_lf.pack(side="left", fill="both")

        home_b = tk.Button(menu_lf, text="Home", bg="#FFFFFF", font="Arial, 20", relief="flat")
        home_b.pack(side="top", padx=5, pady=5)

        loan_b = tk.Button(menu_lf, text="Loans", bg="#FFFFFF", font="Arial, 20", relief="flat")
        loan_b.pack(side="top", padx=5)

        profile_b = tk.Button(menu_lf, text="Profile", bg="#FFFFFF", font="Arial, 20", relief="flat",
                              command=MenuSwitch)
        profile_b.pack(side="top", padx=5, pady=5)

        # Contents container
        content_lf = tk.LabelFrame(self.win, bg="#FFFFFF")
        content_lf.pack(side="left", fill="both", expand="true")

        # Home container
        home_lf = tk.LabelFrame(content_lf, bg="#FFFFFF")
        home_lf.grid(column=0, row=0)

        # Home dashboard container
        home_dashboard_lf = tk.LabelFrame(self.win, bg="#FFFFFF")
        home_dashboard_lf.pack(side="top")

        ttk.Label(home_dashboard_lf, text="Dashboard", background="#FFFFFF").pack(side="top")


window = Window()
window.win.mainloop()
