import tkinter as tk
from tkinter import ttk


class Content(tk.Tk, ttk.LabelFrame, ttk.Entry, ttk.Label, tk.Button, tk.Toplevel, ttk.Treeview):

    def widget_styles(self):
        # Configure styles for widgets
        style = ttk.Style(self)

        # ================================================ Style for Treeview ========================================
        style.configure("default.Treeview", background="#D3D3D3", font=("OpenSans", 12), foreground="black"
                        , rowheight=25, bd=10, fieldbackground="#FFFFFF")
        style.configure("default.Treeview.Heading", font=("OpenSans", 12, "bold"), foreground="green")
        style.map("default.Treeview", background=[("selected", "green")])

        # ================================================ Style for Label =============================================
        style.configure('h1.TLabel', font=("Times New Roman", 20, "bold"), foreground='#4C8404', background="#FFFFFF")
        style.configure('h1_title.TLabel', font=("Times New Roman", 20, "bold"), foreground='#585456',
                        background="#FFFFFF")
        style.configure('h1_body.TLabel', font=("Times New Roman", 15), foreground='#585456',
                        background="#FFFFFF")
        style.configure('link.TLabel', font=("Times New Roman", 10, "underline"), foreground='blue',
                        background="#FFFFFF")
        style.configure('link2.TLabel', font=("Times New Roman", 10), foreground='blue',
                        background="#FFFFFF")
        style.configure('h1_footnote.TLabel', font=("Times New Roman", 12), foreground='#585456',
                        background="#FFFFFF")
        style.configure('h3.TLabel', font=("OpenSans", 10), foreground='#000000', background="#EBEBEB")
        style.configure('heading.TLabel', font=("OpenSans", 12, "bold"), foreground='green', background="#FFFFFF")
        style.configure('body.TLabel', font=("OpenSans", 10, "bold"), foreground='#000000', background="#FFFFFF")
        style.configure('body_content.TLabel', font=("OpenSans", 10), foreground='green', background="#FFFFFF")

        style.configure('featured_h1.TLabel', font=("OpenSans", 18), foreground='#4C8404', background="#FFFFFF")
        style.configure('featured_h1_big.TLabel', font=("OpenSans", 24), foreground='#585456', background="#FFFFFF")
        style.configure('featured_h2.TLabel', font=("OpenSans", 15), foreground='#585456', background="#FFFFFF")

        style.configure('featured_h1_2.TLabel', font=("OpenSans", 15), foreground='#585456', background="#FFFFFF")
        style.configure('featured_h2_2.TLabel', font=("OpenSans", 12), foreground='#585456', background="#FFFFFF")

        style.configure('filter.TLabel', font=("OpenSans", 12), foreground='#4C8404', background="#D4DEC9")
        # ================================================ Style for LabelFrame ========================================
        style.configure('forms.TLabelframe', background="#FFFFFF", bordercolor="green", borderwidth=1)

    def destroy_content(self):
        for child in self.winfo_children():
            child.destroy()

    def delete_entry(self):
        for widget in self.winfo_children():
            if isinstance(widget, ttk.Entry):
                widget.delete(0, "end")

    def delete_label(self):
        for widget in self.winfo_children():
            if isinstance(widget, ttk.Label):
                widget.configure(text=0)

    def destroy_button(self):
        for widget in self.winfo_children():
            if isinstance(widget, tk.Button):
                widget.destroy()

    def disable_entry(self):
        for widget in self.winfo_children():
            if isinstance(widget, ttk.Entry):
                widget.config(state="disabled")

    @staticmethod
    def clear_treeview(treeview=ttk.Treeview):
        for widget in treeview.get_children():
            treeview.delete(widget)


