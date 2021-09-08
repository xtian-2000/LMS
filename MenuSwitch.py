import tkinter as tk
from tkinter import ttk
from addPeople import *
from P2P import content_lf


class Switch:
    def __init__(self):
        self.content_lf = content_lf
        for child in self.content_lf.winfo_children():
            child.destroy()

    def switch_profile(self):
        # Profile Container
        profile_lf = tk.LabelFrame(self.content_lf, bg="#FFFFFF")
        profile_lf.grid(column=0, row=0)

        ttk.Label(profile_lf, text="Profile", background="#FFFFFF").pack(side="top")

        # Profile Button Container

        profile_buttons_lf = tk.LabelFrame(profile_lf, bg="#FFFFFF")
        profile_buttons_lf.pack(side="top")

        add_people_b = tk.Button(profile_buttons_lf, text="add people", command=AddPeople)
        add_people_b.pack(side="top")
