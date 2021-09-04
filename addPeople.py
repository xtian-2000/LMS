import tkinter as tk
from tkinter import ttk
import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="PongoDev",
    password="PongoDev44966874",
    database="LMSdatabase"
)

mycursor = db.cursor()


# Window for adding people's profile


def add_people():
    global add_people_name_entry
    global add_people_address_entry
    global age_spinbox
    global gender_combobox

    add_people_top = tk.Toplevel()
    add_people_top.geometry("500x500")
    add_people_top.title("Add people")

    ttk.Label(add_people_top, text="Borrower's Profile").grid(column=0, row=0)
    ttk.Label(add_people_top, text="Name").grid(column=0, row=1)

    add_people_name_entry = ttk.Entry(add_people_top, width=50)
    add_people_name_entry.grid(column=1, row=1)

    ttk.Label(add_people_top, text="Address").grid(column=0, row=2)

    add_people_address_entry = ttk.Entry(add_people_top, width=50)
    add_people_address_entry.grid(column=1, row=2)

    ttk.Label(add_people_top, text="Age").grid(column=0, row=3)

    age_spinbox = ttk.Spinbox(add_people_top, from_=0, to=200, width=5, command=_spin)
    age_spinbox.grid(column=1, row=3)

    # Combobox for gender

    ttk.Label(add_people_top, text="Gender").grid(column=0, row=4)
    gender_combobox = ttk.Combobox(add_people_top, width=10)
    gender_combobox['values'] = "Male", "Female", "Others"
    gender_combobox.grid(column=1, row=4)
    gender_combobox.current(0)

    # Button for adding people to database

    finish_add_people_b = ttk.Button(add_people_top, text="Add", command=_finish_add_people)
    finish_add_people_b.grid(column=0, row=5)

    add_people_name_entry.focus()

    add_people_top.mainloop()


# Spinbox callback for age


def _spin():
    value = age_spinbox.get()


# Add people to database


def _finish_add_people():
    mycursor.execute("INSERT INTO Borrower (name, address, created, age, gender) VALUES (%s,%s,%s,%s,%s)",
                     (add_people_name_entry.get(), add_people_address_entry.get(), datetime.now(), age_spinbox.get(),
                      gender_combobox.get()))
    db.commit()

