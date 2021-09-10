from tkinter import ttk, END, Entry
import tkinter

# Create class that handles destroying, and disabling contents of main window


class Content(tkinter.Tk, ttk.LabelFrame, ttk.Entry):

    def destroy_content(self):
        for child in self.winfo_children():
            child.destroy()

    def delete_entry(self):
        self.delete(0, END)


print("f")