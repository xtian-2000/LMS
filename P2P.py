from addPeople import *
import mysql.connector
import tkinter as tk
from tkinter import ttk

# Connecting to mysql database
db = mysql.connector.connect(
    host="localhost",
    user="PongoDev",
    password="PongoDev44966874",
    database="LMSdatabase"
)

mycursor = db.cursor()

# mycursor.execute("CREATE DATABASE LMSdatabase")

mycursor.execute("DROP TABLE Borrower")
mycursor.execute("CREATE TABLE Borrower (borrowerID int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), "
                 "address VARCHAR(50),"
                 "created datetime, gender VARCHAR(6), age smallint(2) UNSIGNED)")

mycursor.execute("DESCRIBE Borrower")
for x in mycursor:
    print(x)

win = tk.Tk()
win.title("P2P Lending Management System")


# Menu Container

menu_LF = ttk.Labelframe(win)
menu_LF.grid(column=0, row=0)

ttk.Label(menu_LF, text="Home").grid(column=0, row=0)
ttk.Label(menu_LF, text="Loans").grid(column=0, row=1)
ttk.Label(menu_LF, text="Profile").grid(column=0, row=2)

# Contents Container
content_LF = ttk.Labelframe(win)
content_LF.grid(column=1, row=0)

profile_LF = ttk.Labelframe(content_LF)
profile_LF.grid(column=0, row=0)

ttk.Label(profile_LF, text="Profile").pack(side="top")

profile_buttons_LF = ttk.Labelframe(profile_LF)
profile_buttons_LF.pack(side="top")

add_people_B = ttk.Button(profile_LF, text="add people", command=add_people).pack(side="top")

win.mainloop()
