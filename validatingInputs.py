from tkinter import messagebox
from awesometkinter.bidirender import render_text
from re import compile
from datetime import date

def emptyFields(root, inputs:dict) -> bool:
    '''
    This is a helper function to check if there is an empty input field or wrong inputs
    '''
    # checking for empty fields
    if '' in list(inputs.values()):
        errorMssg("البيانات ناقصة", "برجاء إكمال كافة البيانات", parent=root)
        return True
def wrongPhoneNumber(root, inputs:dict):
    phone_number = inputs["phone_number"]
    # checking the validity of the phone number field, the number must be an egyptian phone number
    number_re = compile(r"^01[0-2,5]\d{8}")
    if number_re.fullmatch(phone_number) is None:
        errorMssg("خطأ في رقم الهاتف", "الرجاء إدخال رقم هاتف صحيح!", parent=root)
        return True
    return False

def invalidDates(root, reservation:dict) -> bool:
    '''
    This is a helper function to check if there is wrong inputs
    '''
    arrival_date:date = reservation["arrival_date"]
    departure_date:date = reservation["departure_date"]
    # checking the validity of the dates
    if arrival_date == departure_date:
        errorMssg("خطأ في مواعيد الحجز", "يوم الوصول هو نفس يوم المغادرة!", parent=root)
        return True
    if arrival_date > departure_date:
        errorMssg("خطأ في مواعيد الحجز", "يوم الوصول يسبق يوم المغادرة!", parent=root)
        return True
    if arrival_date < date.today():
        errorMssg("خطأ في مواعيد الحجز", "يوم الوصول هو يوم في الماضي!", parent=root)
        return True
    return False

# def isInBlacklist(root, guest_data:dict) -> bool:
#     name, phone_number = guest_data["name"], guest_data["phone_number"]
#     db.cursor.execute("SELECT name FROM blacklist WHERE name=? AND phone_number=?", (name, phone_number))
#     names_list = db.cursor.fetchall()
#     if len(names_list) != 0:
#         errorMssg("الأسم محظور", "الأسم موجود في قائمة الحظر!", parent=root)
#         return True
#     return False

# def isDuplicateReservation(root, reservation:dict) -> bool:
#     name, phone_number, arrival_date, departure_date = list(reservation.values())
#     db.cursor.execute("""SELECT name
#                         FROM reservations
#                         WHERE name LIKE ?
#                         AND phone_number=?
#                         AND arrival_date=?
#                         AND departure_date=?""", (name, phone_number, arrival_date, departure_date))
#     names_list = db.cursor.fetchall()
#     if len(names_list) != 0:
#         errorMssg("الحجز موجود", "الحجز موجود بالفعل!", parent=root)
#         return True
#     return False

def errorMssg(title="Error", Mssg="Unkown Error", parent=None):
    messagebox.showwarning(title, render_text(Mssg), parent=parent)