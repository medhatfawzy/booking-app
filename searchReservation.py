#!/usr/bin/python3
from tkinter import Toplevel, CENTER, RIGHT, messagebox, Entry, PhotoImage, END
from tkinter.ttk import Button, Label, Treeview
from awesometkinter.bidirender import add_bidi_support, render_text
from os import path

from databaseAPI import DataBaseAPI

class Search(Toplevel):
    def __init__(self, root):
        super().__init__()
        self.root = root
        self.initUI()
    def initUI(self):
        self.title("البحث عن نزيل")
        self.transient(self.root)
        # Centering the widget
        width = int(self.winfo_screenwidth() / 2)
        height = int(self.winfo_screenheight() / 2)
        x_left = int(self.winfo_screenwidth() / 2 - width / 2)
        y_top = int(self.winfo_screenheight() / 2 - height / 2)
        self.geometry(f"{width}x{height}+{x_left}+{y_top}")
        # creating the entry width for all the entries
        entry_width:int = 40
        # creating the name entry and label
        self.name_entry = Entry(self, width=entry_width)
        self.name_label = Label(self, text=render_text("الأسم:"))
        add_bidi_support(self.name_entry)
        # creating the phone number entry and label
        self.phone_number_entry = Entry(self, width=entry_width)
        self.phone_number_label = Label(self, text=render_text("رقم الهاتف:"))
        add_bidi_support(self.phone_number_entry)
        # creating the search button
        self.search_icon = PhotoImage(file=path.join("imgs","search16.png"))
        self.search_btn = Button(self, text=render_text("بحث"),
                                image=self.search_icon, compound=RIGHT, command=self.searchGuest)
        # the distance from the left for the label and the entry
        relx_label:float = 0.7
        relx_entry:float = 0.4
        # putting things on the screen
        self.name_label.place(relx=relx_label, rely=0.2, anchor="w")
        self.name_entry.place(relx=relx_entry, rely=0.2, anchor=CENTER)
        self.phone_number_label.place(relx=relx_label, rely=0.4, anchor="w")
        self.phone_number_entry.place(relx=relx_entry, rely=0.4, anchor=CENTER)
        self.search_btn.place(relx=0.5, rely=0.8, anchor=CENTER)

    def searchGuest(self) -> None:
        '''
        This is the function that is activated when the user click the search button
        '''
        guest_data = {
            'name': self.name_entry.get(),
            'phone_number': self.phone_number_entry.get()
        }
        guest_reservations, is_blacklisted = DataBaseAPI.searchReservation(self, guest_data)
        ResultsTree(self.root, guest_reservations)
        # These two line are used to close the Toplevel()
        self.destroy()
        self.update()

class ResultsTree(Toplevel):
    def __init__(self, root, guest_reservations):
        super().__init__()
        self.root = root
        self.guest_reservations = guest_reservations
        self.initUI()
    def initUI(self):
        self.title("حجوزات النزيل")
        self.transient(self.root)
        # Centering the widget
        width = int(self.winfo_screenwidth() / 1.5)
        height = int(self.winfo_screenheight() / 1.5)
        x_left = int(self.winfo_screenwidth() / 2 - width / 2)
        y_top = int(self.winfo_screenheight() / 2 - height / 2)
        self.geometry(f"{width}x{height}+{x_left}+{y_top}")

        columns = ["name", "phone_number", "arrival_date", "departure_date", "rental_unit"]
        results_tree = Treeview(self, columns=columns, show='headings')
        results_tree.heading('name', text=render_text("الأسم"), anchor=CENTER)
        results_tree.heading('phone_number', text=render_text("رقم الهاتف"))
        results_tree.heading('arrival_date', text=render_text("تاريخ الوصول"))
        results_tree.heading('departure_date', text=render_text("تاريخ المغادرة"))
        results_tree.heading('rental_unit', text=render_text("الوحدة السكنية"))
        for reservation in self.guest_reservations:
            results_tree.insert('', END, values=(render_text(reservation[0]),
                                                render_text(reservation[1]),
                                                render_text(reservation[2]),
                                                render_text(reservation[3])
                                                ))
        close_btn = Button(self, text=render_text("إغلاق"), command=self.closeWindow)

        results_tree.place(relx=0.1, rely=0.1)
        close_btn.place(relx=0.5, rely=0.9, anchor=CENTER)
    def closeWindow(self):
        self.destroy()
        self.update()
