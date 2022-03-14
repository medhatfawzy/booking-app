#!/usr/bin/python
# Minimum python version required is 3.6
from tkinter import Toplevel, Entry, Label, Button, CENTER, messagebox
from awesometkinter.bidirender import add_bidi_support
import csv

reservation_file = "data/reservations.csv"
blacklist_file = "data/blacklist.csv"

class search():
    def __init__(self, root):
        self.root = root
        self.search_window = Toplevel(self.root)
        self.search_window.title("البحث عن نزيل")
        self.search_window.transient(root)

        # Centering the widget
        width = int(self.search_window.winfo_screenwidth() / 3)
        height = int(self.search_window.winfo_screenheight() / 3)
        x_left = int(self.search_window.winfo_screenwidth() / 2 - width / 2)
        y_top = int(self.search_window.winfo_screenheight() / 2 - height / 2)
        self.search_window.geometry(f"{width}x{height}+{x_left}+{y_top}")

        # creating the entry width for all the entries
        entry_width = 40
        # creating the name entry and label
        self.name_entry = Entry(self.search_window, width=entry_width)
        self.name_label = Label(self.search_window)
        add_bidi_support(self.name_entry)
        add_bidi_support(self.name_label)
        self.name_label.set(":الإسم")
        # creating the phone number entry and label
        self.phone_number_entry = Entry(self.search_window, width=entry_width)
        self.phone_number_label = Label(self.search_window)
        add_bidi_support(self.phone_number_entry)
        add_bidi_support(self.phone_number_label)
        self.phone_number_label.set(":الرقم")
        # creating the search button
        self.btn_search = Button(self.search_window, text="Search", command=self.searchGuest, padx=23, pady=23)

        # the distance from the left for the label and the entry
        relx_label = 0.8
        relx_entry = 0.4

        # putting things on the screen
        self.name_label.place(relx=relx_label, rely=0.2, anchor= CENTER)
        self.name_entry.place(relx=relx_entry, rely=0.2, anchor= CENTER)

        self.phone_number_label.place(relx=relx_label, rely=0.4, anchor= CENTER)
        self.phone_number_entry.place(relx=relx_entry, rely=0.4, anchor= CENTER)

        self.btn_search.place(relx=0.5, rely=0.8, anchor= CENTER)

    def searchGuest(self):
        '''
        This is the function that is activated when the user click the search button
        '''
        guest_data = {
            'name': self.name_entry.get(),
            'phone_number': self.phone_number_entry.get()
        }
        if self.emptyFileds(guest_data): return
        if self.nameBlacklisted(guest_data): return

        guest_reservations = []
        with open(reservation_file, 'r') as reservations:
            filereader = csv.reader(reservations)

            for line in filereader:
                if line[0:2] == list(guest_data.values()):
                    guest_reservations.append(line)
        print(guest_reservations)
        # These two line are used to close the Toplevel()
        self.search_window.destroy()
        self.search_window.update()

    def emptyFileds(self, guest_data):
        '''
        This is a helper function to check if there is an empty input field
        '''
        if '' in list(guest_data.values()):
            messagebox.showinfo( "أكمل البيانات",
                                    "Please fill in all the fields.",
                                    parent=self.search_window)
            return True

    def nameBlacklisted(self, guest_data):
        '''
        This helper function checks if the name we are searching for
        exists in the blacklist or not.
        '''
        with open(blacklist_file, 'r') as blacklist:
            filereader = csv.reader(blacklist)
            for line in filereader:
                if line == list(guest_data.values()):
                    messagebox.showwarning( "الأسم في قائمة الحظر",
                        "The name you are searching for is blacklisted!",
                        parent=self.search_window)
                    return True