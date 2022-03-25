import sqlite3
from os import path
from tkinter import messagebox
from awesometkinter.bidirender import render_text

class DataBase:
    def __init__(self):
        # Connecting to the database and creating it if it dosen't exist
        self.database = sqlite3.connect(path.join("data", "database.db"))
        # Database cursor
        self.cursor = self.database.cursor()

    def searchReservation(self, root, guest_data:list) -> tuple:
        if self.isInvalidInputs(root, guest_data): raise ValueError()
        name, phone_number = guest_data
        self.cursor.execute(f"SELECT * FROM reservations WHERE name LIKE '{name}%'")
        reservations = self.cursor.fetchall()
        return reservations

    def addReservation(self, root, reservation:list) -> None:
        if self.isInvalidInputs(root, reservation): raise ValueError()
        name, phone_number, arrival_date, departure_date = reservation
        if self.isInBlacklist(root, reservation): return
        if self.isDuplicateReservation(root, reservation): return
        self.cursor.execute(f"""INSERT INTO reservations VALUES('{name}',
                                                        '{phone_number}',
                                                        '{arrival_date}',
                                                        '{departure_date}')""")
        # commit changes
        self.database.commit()
        print("data written")

    def blockGuest(self, root, guest_data:list) -> None:
        if self.isInvalidInputs(root, guest_data): raise ValueError()
        name, phone_number, blocking_reason = guest_data
        if self.isInBlacklist(guest_data): return
        self.cursor.execute(f"""INSERT INTO blacklist VALUES('{name}',
                                                            '{phone_number}',
                                                            '{blocking_reason}')""")
        # commit changes
        self.database.commit()
        print("data written")


    def isInBlacklist(self, root, guest_data:list) -> bool:
        name, phone_number = guest_data[0:2]
        self.cursor.execute(f"""SELECT * FROM blacklist
                                WHERE name='{name}'
                                AND phone_number = '{phone_number}'""")
        names_list = self.cursor.fetchall()
        if len(names_list) != 0:
            messagebox.showwarning("الأسم في قائمة الحظر",
                        render_text("لا يمكن الحجز لأسم موجود في قائمة الحظر!"),
                        parent=root)
            return True
        return False

    def isDuplicateReservation(self,root, reservation:list) -> bool:
        name, phone_number, arrival_date, departure_date = reservation
        self.cursor.execute(f"""SELECT * FROM reservations
                                WHERE name = '{name}'
                                AND phone_number = '{phone_number}'
                                AND arrival_date = '{arrival_date}'
                                AND departure_date = '{departure_date}'""")
        reservation = self.cursor.fetchall()
        if len(reservation) != 0:
            messagebox._show("الحجز مكرر",
                                    render_text("الحجز الذي تحاول إدخاله موجود بالفعل!"),
                                    parent=root)
            return True
        return False

    def isInvalidInputs(self, root, inputs:list) -> bool:
        '''
        This is a helper function to check if there is an empty input field or wrong inputs
        '''
        # checking for empty fields
        if '' in inputs:
            messagebox.showwarning("البيانات ناقصة",
                                render_text("برجاء إكمال كافة البيانات"),
                                parent=root)
            return True
        return False