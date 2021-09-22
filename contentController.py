import tkinter as tk
# Create class that handles destroying, and disabling contents of main window

from tkinter import ttk


class Content(tk.Tk, ttk.LabelFrame, ttk.Entry, ttk.Label, tk.Button, tk.Toplevel):

    def widget_styles(self):
        # Configure styles for widgets
        style = ttk.Style(self)
        style.configure("default.Treeview", background="#D3D3D3", font=("OpenSans", 12), foreground="black"
                        , rowheight=25, bd=10, fieldbackground="#FFFFFF")
        style.configure("default.Treeview.Heading", font=("OpenSans", 12, "bold"), foreground="green")
        style.map("default.Treeview", background=[("selected", "green")])

        style.configure('h1.TLabel', font=("OpenSans", 20, "bold"), foreground='green', background="#EBEBEB")
        style.configure('h3.TLabel', font=("OpenSans", 10), foreground='#000000', background="#EBEBEB")
        style.configure('heading.TLabel', font=("OpenSans", 12, "bold"), foreground='green', background="#FFFFFF")
        style.configure('body.TLabel', font=("OpenSans", 10), foreground='#000000', background="#FFFFFF")

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


