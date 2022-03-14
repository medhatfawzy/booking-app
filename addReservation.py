#!/usr/bin/python
# Minimum python version required is 3.6
from tkinter import Toplevel, Entry, Label, Button, CENTER, messagebox
from awesometkinter.bidirender import add_bidi_support
import csv

reservation_file = "data/reservations.csv"
blacklist_file = "data/blacklist.csv"

class add():
    def __init__(self, root):
        self.root = root
        self.add_window = Toplevel(self.root)
        self.add_window.title("إضافة نزيل")

        # Centering the widget
        width = int(self.add_window.winfo_screenwidth() / 2.5)
        height = int(self.add_window.winfo_screenheight() / 2.5)
        x_left = int(self.add_window.winfo_screenwidth() / 2 - width / 2)
        y_top = int(self.add_window.winfo_screenheight() / 2 - height / 2)
        self.add_window.geometry(f"{width}x{height}+{x_left}+{y_top}")

        # creating the entry width for all the entries
        entry_width = 40
        # creating the name entry and label
        self.name_entry = Entry(self.add_window, width=entry_width)
        self.name_label = Label(self.add_window)
        add_bidi_support(self.name_entry)
        add_bidi_support(self.name_label)
        self.name_label.set(":الإسم")
        # creating the phone number entry and label
        self.phone_number_entry = Entry(self.add_window, width=entry_width)
        self.phone_number_label = Label(self.add_window)
        add_bidi_support(self.phone_number_entry)
        add_bidi_support(self.phone_number_label)
        self.phone_number_label.set(":الرقم")
        # creating the arrival date entry and label
        self.arrival_date_entry = Entry(self.add_window, width=entry_width)
        self.arrival_date_label = Label(self.add_window)
        add_bidi_support(self.arrival_date_entry)
        add_bidi_support(self.arrival_date_label)
        self.arrival_date_label.set(":تاريخ الوصول")
        # creating the departure date entry and label
        self.departure_date_entry = Entry(self.add_window,width=entry_width)
        self.departure_date_label = Label(self.add_window)
        add_bidi_support(self.departure_date_entry)
        add_bidi_support(self.departure_date_label)
        self.departure_date_label.set(":تاريخ المغادرة")
        # creating the save button
        self.btn_save = Button(self.add_window, text="Save", command=self.saveGuest)

        # the distance from the left for the label and the entry
        relx_label = 0.7
        relx_entry = 0.4

        # putting things on the screen
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
        '''
        This is the function that is activated when the user click the save button
        '''
        reservation_data = {
            'name': self.name_entry.get(),
            'phone_number': self.phone_number_entry.get(),
            'arrival_date': self.arrival_date_entry.get(),
            'departure_date': self.departure_date_entry.get()
        }
        if self.emptyFields(reservation_data): return
        if self.nameBlacklisted(reservation_data): return
        if self.duplicateReservation(reservation_data): return

        with open(reservation_file, 'a') as csvfile:
            csv_writer = csv.DictWriter(csvfile, fieldnames=reservation_data.keys())
            csv_writer.writerows([reservation_data])
            print("reservation added")
        # These two line are used to close the Toplevel()
        self.add_window.destroy()
        self.add_window.update()

    def emptyFields(self, reservation_data):
        '''
        This is a helper function to check if there is an empty input field
        '''
        if '' in list(reservation_data.values()):
            messagebox.showinfo( "أكمل البيانات",
                                "Please fill in all the fields.",
                                parent=self.add_window)
            return True

    def nameBlacklisted(self, reservation_data):
        '''
        This helper function checks if the name we are trying to create a reservation for
        exists in the blacklist or not.
        '''
        with open(blacklist_file, 'r') as blacklist:
            blacklist_reader = csv.reader(blacklist)
            guest_data = list(reservation_data.values())[0:2]
            for line in blacklist_reader:
                if line == guest_data:
                    messagebox.showwarning("الإسم محظور",
                                    "The name you are trying to add is blacklisted!",
                                    parent=self.add_window)
                    return True

    def duplicateReservation(self, reservation_data):
        '''
        This helper function checks if the reservation is already added
        '''
        with open(reservation_file, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for line in csv_reader:
                if line == list(reservation_data.values()):
                    messagebox.showinfo(  "الحجز موجود بالفعل",
                                    "Reservation already exists!",
                                    parent=self.add_window)
                    return True