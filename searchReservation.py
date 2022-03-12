#!/usr/bin/python

try:
    from tkinter import *
except:
    from Tkinter import *
from awesometkinter.bidirender import add_bidi_support

class search():
    def __init__(self):
        self.search_window = Toplevel()
        self.search_window.title("البحث عن نزيل")

        width = int(self.search_window.winfo_screenwidth() / 3)
        height = int(self.search_window.winfo_screenheight() / 3)
        x_left = int(self.search_window.winfo_screenwidth() / 2 - width / 2)
        y_top = int(self.search_window.winfo_screenheight() / 2 - height / 2)

        try:
            self.search_window.geometry(f"{width}x{height}+{x_left}+{y_top}")
        except:
            self.search_window.geometry("{0}x{1}+{2}+{3}".format(width, height, x_left, y_top))

        entry_width = 40

        self.name_entry = Entry(self.search_window, width=entry_width)
        self.name_label = Label(self.search_window)
        add_bidi_support(self.name_entry)
        add_bidi_support(self.name_label)
        self.name_label.set(":الإسم")

        self.phone_number_entry = Entry(self.search_window, width=entry_width)
        self.phone_number_label = Label(self.search_window)
        add_bidi_support(self.phone_number_entry)
        add_bidi_support(self.phone_number_label)
        self.phone_number_label.set(":الرقم")


        self.btn_search = Button(self.search_window, text="search", command=self.searchGuest)

        relx_label = 0.8
        relx_entry = 0.4

        self.name_label.place(relx=relx_label, rely=0.2, anchor= CENTER)
        self.name_entry.place(relx=relx_entry, rely=0.2, anchor= CENTER)

        self.phone_number_label.place(relx=relx_label, rely=0.4, anchor= CENTER)
        self.phone_number_entry.place(relx=relx_entry, rely=0.4, anchor= CENTER)

        self.btn_search.place(relx=0.5, rely=0.8, anchor= CENTER)

    def searchGuest(self):
        guest_data = {
            'name': self.name_entry.get(),
            'phone_number': self.phone_number_entry.get(),
        }
        print(guest_data)
        self.search_window.destroy()
        self.search_window.update()
