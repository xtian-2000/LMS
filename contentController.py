from tkinter import ttk

# Create class that handles destroying, and disabling contents of main window


class Content(ttk.LabelFrame):

    def destroy_content(self):
        for child in self.winfo_children():
            child.destroy()
