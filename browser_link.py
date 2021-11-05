import webbrowser
import tkinter
from tkinter import ttk, messagebox


class Browser:
    def __init__(self, link, message):
        self.link = link
        self.message = message
        print(message)
        """
        link = "https://www.wonder.legal/ph/creation-modele/loan-agreement-ph"
        tkinter.messagebox.showinfo("Note!", "We are in no way affiliated with the website or its developers.\n"
                                             "Here is the link for our recommended website:\n"
                                             "(https://www.wonder.legal/ph/creation-modele/loan-agreement-ph)\n")
                                             """
        tkinter.messagebox.showinfo("Note!", "We are in no way affiliated with the website or its developers.\n"
                                             "Here is the link for our recommended website:\n"
                                             "(%s)\n" % link)
        webbrowser.open_new(link)
