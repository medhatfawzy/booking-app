from tkinter import messagebox
from awesometkinter.bidirender import render_text
from os import path
import sqlite3
from re import compile

# Connecting to the database and creating it if it dosen't exist
database = sqlite3.connect(path.join("data", "database.db"))
# Database cursor
cursor = database.cursor()

class DataBaseAPI:
    def searchReservation(root, guest_data:dict) -> tuple:
        if DBCheck.isInvalidInputs(root, guest_data): raise ValueError()
        name, phone_number = guest_data["name"], guest_data["phone_number"]
        cursor.execute(f"""SELECT * FROM reservations
                            WHERE name LIKE '{name}%'
                            AND phone_number LIKE '{phone_number}'""")
        reservations = cursor.fetchall()
        return reservations

    def addReservation(root, reservation:dict) -> bool:
        """
        returns true if successful or false if not
        """
        if DBCheck.isInvalidInputs(root, reservation): return False
        name, phone_number, arrival_date, departure_date = list(reservation.values())
        if DBCheck.isInBlacklist(root, reservation): return False
        if DBCheck.isDuplicateReservation(root, reservation): return False
        cursor.execute(f"""INSERT INTO reservations VALUES('{name}',
                                                        '{phone_number}',
                                                        '{arrival_date}',
                                                        '{departure_date}')""")
        # commit changes
        database.commit()
        print("data written")
        return True

    def blockGuest(root, guest_data:dict) -> bool:
        """
        returns true if successful or false if not
        """
        if DBCheck.isInvalidInputs(root, guest_data): return False
        name, phone_number, blocking_reason = guest_data["name"], guest_data["phone_number"], guest_data["blocking_reason"]
        if DBCheck.isInBlacklist(root, guest_data): return False
        cursor.execute(f"""INSERT INTO blacklist VALUES('{name}',
                                                        '{phone_number}',
                                                        '{blocking_reason}')""")
        # commit changes
        database.commit()
        print("data written")
        return True

class DBCheck():
    def isInBlacklist(root, guest_data:dict) -> bool:
        name, phone_number = guest_data["name"], guest_data["phone_number"]
        cursor.execute(f"""SELECT * FROM blacklist
                            WHERE name='{name}'
                            AND phone_number='{phone_number}'""")
        names_list = cursor.fetchall()
        if len(names_list) != 0:
            messagebox.showwarning("الأسم محظور",
                                    render_text("لأسم موجود في قائمة الحظر!"),
                                    parent=root)
            return True
        return False

    def isDuplicateReservation(root, reservation:dict) -> bool:
        name, phone_number, arrival_date, departure_date = list(reservation.values())
        cursor.execute(f"""SELECT * FROM reservations
                            WHERE name='{name}'
                            AND phone_number='{phone_number}'
                            AND arrival_date='{arrival_date}'
                            AND departure_date='{departure_date}'""")
        reservation = cursor.fetchall()
        if len(reservation) != 0:
            messagebox._show("الحجز مكرر",
                            render_text("الحجز الذي تحاول إدخاله موجود بالفعل!"),
                            parent=root)
            return True
        return False

    def isInvalidInputs(root, inputs:dict) -> bool:
        '''
        This is a helper function to check if there is an empty input field or wrong inputs
        '''
        name, phone_number = inputs["name"], inputs["phone_number"]
        # checking for empty fields
        if '' in list(inputs.values()):
            messagebox.showwarning("البيانات ناقصة",
                                render_text("برجاء إكمال كافة البيانات"),
                                parent=root)
            return True
        # checking the validity of the phone number field, the number must be an egyptian phone number
        number_re = compile(r"^01[0-2,5]\d{8}")
        if number_re.fullmatch(phone_number) is None:
            messagebox.showwarning("خطأ في رقم الهاتف",
                                    render_text("الرجاء إدخال رقم هاتف صحيح!"),
                                    parent=root)
            return True
        return False