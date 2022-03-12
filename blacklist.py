#!/usr/bin/python
try:
    import tkinter as tk
    from tkinter import *
except:
    import Tkinter as tk
    from Tkinter import *
from awesometkinter.bidirender import add_bidi_support

class block():
    def __init__(self, root):
        self.blacklist_window = Toplevel(root)
        self.blacklist_window.title("الممنوعين من الدخول")

        width = int(self.blacklist_window.winfo_screenwidth() / 3)
        height = int(self.blacklist_window.winfo_screenheight() / 3)
        x_left = int(self.blacklist_window.winfo_screenwidth() / 2 - width / 2)
        y_top = int(self.blacklist_window.winfo_screenheight() / 2 - height / 2)

        try:
            self.blacklist_window.geometry(f"{width}x{height}+{x_left}+{y_top}")
        except:
            self.blacklist_window.geometry("{0}x{1}+{2}+{3}".format(width, height, x_left, y_top))

        entry_width = 40

        self.name_entry = Entry(self.blacklist_window, width=entry_width)
        self.name_label = Label(self.blacklist_window)
        add_bidi_support(self.name_entry)
        add_bidi_support(self.name_label)
        self.name_label.set(":الإسم")

        self.phone_number_entry = Entry(self.blacklist_window, width=entry_width)
        self.phone_number_label = Label(self.blacklist_window)
        add_bidi_support(self.phone_number_entry)
        add_bidi_support(self.phone_number_label)
        self.phone_number_label.set(":الرقم")

        self.btn_save = Button(self.blacklist_window, text="save", command=self.blockGuest)

        relx_label = 0.8
        relx_entry = 0.4

        self.name_label.place(relx=relx_label, rely=0.2, anchor= CENTER)
        self.name_entry.place(relx=relx_entry, rely=0.2, anchor= CENTER)

        self.phone_number_label.place(relx=relx_label, rely=0.4, anchor= CENTER)
        self.phone_number_entry.place(relx=relx_entry, rely=0.4, anchor= CENTER)

        self.btn_save.place(relx=0.5, rely=0.8, anchor= CENTER)

    def blockGuest(self):
        guest_data = {
            'name': self.name_entry.get(),
            'phone_number': self.phone_number_entry.get(),
        }
        print(guest_data)
        self.confirmation()
        self.blacklist_window.destroy()
        self.blacklist_window.update()

    def confirmation(self):
        tk.messagebox.askyesno( "هل تريد إضافة الإسم فعلاً",
                                "Are you sure about adding \"{0}\" to the blacklist?".format(self.name_entry.get()),
                                parent=self.blacklist_window
        )