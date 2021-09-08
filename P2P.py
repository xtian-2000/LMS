from addPeople import *
import mysql.connector
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

'''
mycursor.execute("CREATE DATABASE LMSdatabase")

mycursor.execute("DROP TABLE Borrower")
mycursor.execute("CREATE TABLE Borrower (borrowerID int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), "
                 "address VARCHAR(50),"
                 "created datetime, gender VARCHAR(6), age smallint(2) UNSIGNED)")



mycursor.execute("DESCRIBE Borrower")
for x in mycursor:
    print(x)
'''


def _switch_profile():
    # Profile Container

    for child in content_LF.winfo_children():
        child.destroy()

    profile_lf = tk.LabelFrame(content_LF, bg="#FFFFFF")
    profile_lf.grid(column=0, row=0)

    ttk.Label(profile_lf, text="Profile", background="#FFFFFF").pack(side="top")

    # Profile Button Container

    profile_buttons_lf = tk.LabelFrame(profile_lf, bg="#FFFFFF")
    profile_buttons_lf.pack(side="top")

    add_people_b = tk.Button(profile_buttons_lf, text="add people", command=add_people)
    add_people_b.pack(side="top")
"""


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

        profile_b = tk.Button(menu_lf, text="Profile", bg="#FFFFFF", font="Arial, 20", relief="flat")
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

"""
# Window attributes

win = tk.Tk()
win.title("P2P Lending Management System")
# getting screen width and height of display
width = win.winfo_screenwidth()
height = win.winfo_screenheight()
# setting tkinter window size
win.geometry("%dx%d" % (width, height))
win.configure(bg="#FFFFFF")

# Menu Container

menu_LF = tk.LabelFrame(win, bg="#FFFFFF")
menu_LF.pack(side="left", fill="both")

home_B = tk.Button(menu_LF, text="Home", bg="#FFFFFF", font="Arial, 20", relief="flat")
home_B.pack(side="top", padx=5, pady=5)

loan_B = tk.Button(menu_LF, text="Loans", bg="#FFFFFF", font="Arial, 20", relief="flat")
loan_B.pack(side="top", padx=5)

profile_B = tk.Button(menu_LF, text="Profile", bg="#FFFFFF", font="Arial, 20", relief="flat", command=_switch_profile)
profile_B.pack(side="top", padx=5, pady=5)

# Contents Container
content_LF = tk.LabelFrame(win, bg="#FFFFFF")
content_LF.pack(side="left", fill="both", expand="true")

# Home Container
home_LF = tk.LabelFrame(content_LF, bg="#FFFFFF")
home_LF.grid(column=0, row=0)

# Home Dashboard Container
home_dashboard_LF = tk.LabelFrame(home_LF, bg="#FFFFFF")
home_dashboard_LF.pack(side="top")

ttk.Label(home_dashboard_LF, text="Dashboard", background="#FFFFFF").pack(side="top")

win.mainloop()
"""
