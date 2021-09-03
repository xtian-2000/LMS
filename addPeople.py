import tkinter as tk
from tkinter import ttk


# Window for adding people's profile


def add_people():
    add_people_name = tk.StringVar
    add_people_address = tk.StringVar

    add_people_top = tk.Toplevel()
    add_people_top.geometry("500x500")
    add_people_top.title("Add people")

    ttk.Label(add_people_top, text="Borrower's Profile").grid(column=0, row=0)
    ttk.Label(add_people_top, text="Name").grid(column=0, row=1)

    add_people_name_entry = ttk.Entry(add_people_top, width=50, textvariable=add_people_name)
    add_people_name_entry.grid(column=1, row=1)

    ttk.Label(add_people_top, text="Address").grid(column=0, row=2)

    add_people_address_entry = ttk.Entry(add_people_top, width=50, textvariable=add_people_address)
    add_people_address_entry.grid(column=1, row=2)

    finish_add_people_b = ttk.Button(add_people_top, text="Add")
    finish_add_people_b.grid(column=0, row=3)

    add_people_name_entry.focus()

    add_people_top.mainloop()
