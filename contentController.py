import tkinter as tk
from tkinter import ttk


# Create class that handles destroying, and disabling contents of main window


class Content(tk.Tk, ttk.LabelFrame, ttk.Entry, ttk.Label, tk.Button):

    def destroy_content(self):
        for child in self.winfo_children():
            child.destroy()

    def delete_entry(self):
        for widget in self.winfo_children():
            if isinstance(widget, ttk.Entry):
                widget.delete(0, "end")

    def background_change_label(self, background: object):
        for widget in self.winfo_children():
            if isinstance(widget, ttk.Label):
                widget.configure(background=background)

    def background_change_labelframe(self, bg: object):
        for widget in self.winfo_children():
            if isinstance(widget, tk.LabelFrame):
                widget.configure(bg=bg)

    def background_change_button(self, bg: object):
        for widget in self.winfo_children():
            if isinstance(widget, tk.Button):
                widget.configure(bg=bg)

    def underline_button_none(self):
        for widget in self.winfo_children():
            if isinstance(widget, tk.Button):
                widget.configure(font="arial 20 underline")
                print("success")

    def underline_button(self, widget=tk.Button):
        widget.configure(font="arial 20 underline")
