#!/usr/bin/python
try:
    import tkinter as tk
    from tkinter import *
except:
    import Tkinter as tk
    from Tkinter import *
from awesometkinter.bidirender import add_bidi_support
import csv

reservation_file = "data/reservations.csv"
blacklist = "data/blacklist.csv"

class add():
    def __init__(self, root):
        self.root = root
        self.add_window = Toplevel(self.root)
        self.add_window.title("إضافة نزيل")

        width = int(self.add_window.winfo_screenwidth() / 2.5)
        height = int(self.add_window.winfo_screenheight() / 2.5)
        x_left = int(self.add_window.winfo_screenwidth() / 2 - width / 2)
        y_top = int(self.add_window.winfo_screenheight() / 2 - height / 2)

        try:
            self.add_window.geometry(f"{width}x{height}+{x_left}+{y_top}")
        except:
            self.add_window.geometry("{0}x{1}+{2}+{3}".format(width, height, x_left, y_top))

        entry_width = 40
        self.name_entry = Entry(self.add_window, width=entry_width)
        self.name_label = Label(self.add_window)
        add_bidi_support(self.name_entry)
        add_bidi_support(self.name_label)
        self.name_label.set(":الإسم")

        self.phone_number_entry = Entry(self.add_window, width=entry_width)
        self.phone_number_label = Label(self.add_window)
        add_bidi_support(self.phone_number_entry)
        add_bidi_support(self.phone_number_label)
        self.phone_number_label.set(":الرقم")

        self.arrival_date_entry = Entry(self.add_window, width=entry_width)
        self.arrival_date_label = Label(self.add_window)
        add_bidi_support(self.arrival_date_entry)
        add_bidi_support(self.arrival_date_label)
        self.arrival_date_label.set(":تاريخ الوصول")

        self.departure_date_entry = Entry(self.add_window,width=entry_width)
        self.departure_date_label = Label(self.add_window)
        add_bidi_support(self.departure_date_entry)
        add_bidi_support(self.departure_date_label)
        self.departure_date_label.set(":تاريخ المغادرة")

        self.btn_save = Button(self.add_window, text="save", command=self.saveGuest)

        relx_label = 0.7
        relx_entry = 0.4

        self.name_label.place(relx=relx_label, rely=0.1, anchor= CENTER)
        self.name_entry.place(relx=relx_entry, rely=0.1, anchor= CENTER)

        self.phone_number_label.place(relx=relx_label, rely=0.3, anchor= CENTER)
        self.phone_number_entry.place(relx=relx_entry, rely=0.3, anchor= CENTER)

        self.arrival_date_label.place(relx=relx_label, rely=0.5, anchor= CENTER)
        self.arrival_date_entry.place(relx=relx_entry, rely=0.5, anchor= CENTER)

        self.departure_date_label.place(relx=relx_label, rely=0.7, anchor= CENTER)
        self.departure_date_entry.place(relx=relx_entry, rely=0.7, anchor= CENTER)

        self.btn_save.place(relx=0.5, rely=0.9, anchor= CENTER)

    def saveGuest(self):
        reservation_data = {
            'name': self.name_entry.get(),
            'phone_number': self.phone_number_entry.get(),
            'arrival_date': self.arrival_date_entry.get(),
            'departure_date': self.departure_date_entry.get()
        }
        if '' in list(reservation_data.values()):
            self.emptyMssg()
            return

        with open(blacklist, 'r') as blacklistfile:
            blacklist_reader = csv.reader(blacklistfile)
            guest_data = list(reservation_data.values())[0:2]
            for line in blacklist_reader:
                if line == guest_data:
                    self.nameBlacklistMssg()
                    return
        with open(reservation_file, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for line in csv_reader:
                if line == list(reservation_data.values()):
                    self.duplicateMssg()
                    return
        with open(reservation_file, 'a') as csvfile:
            csv_writer = csv.DictWriter(csvfile, fieldnames=reservation_data.keys())
            csv_writer.writerows([reservation_data])
            print("reservation added")

        self.add_window.destroy()
        self.add_window.update()

    def duplicateMssg(self):
        tk.messagebox.showinfo(  "الحجز موجود بالفعل",
                                    "Reservation already exists!",
                                    parent=self.add_window)
    def emptyMssg(self):
        tk.messagebox.showinfo( "أكمل البيانات",
                                "Please fill in the all the fields.",
                                parent=self.add_window)
    def nameBlacklistMssg(self):
        tk.messagebox.showwarning("الإسم محظور",
                                    "The name you are trying to add is blacklisted!",
                                    parent=self.add_window)
