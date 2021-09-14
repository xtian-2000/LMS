import tkinter as tk
from tkinter import ttk


# Create class that handles destroying, and disabling contents of main window


class Content(tk.Tk, ttk.LabelFrame, ttk.Entry):

    def destroy_content(self):
        for child in self.winfo_children():
            child.destroy()

    def delete_entry(self):
        for widget in self.winfo_children():
            if isinstance(widget, ttk.Entry):
                widget.delete(0, "end")


