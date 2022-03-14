import sqlite3

def database_connect(name, phone_number, arrival_date, departure_date, reservations):
    # Connecting to the database and creating it if it dosen't exist
    database = sqlite3.connect('reservations.db')

    # Database cursor
    cursor = database.cursor()

    # cursor.execute("""
    #                 CREATE TABLE reservations(
    #                     name text,
    #                     phone_number integer,
    #                     arrival_date text,
    #                     departure_date text
    #                 )
    # """)
    cursor.executemany("INSERT INTO reservations VALUES (?,?,?,?)", reservations)

    cursor.execute(f"""
                    INSERT INTO reservations VALUES('{name}',
                                                    '{phone_number}',
                                                    '{arrival_date}',
                                                    '{departure_date}')
    """)
    # commit changes
    database.commit()
    # close the connection
    database.close()

reservations = [('karem ragey', '01099514099', '5/5/5', '6/5/5'),
                ('ahmed saeed', '01099514099', '5/5/5', '6/5/5'),
                ('haitham shaker', '01099514099', '5/5/5', '6/5/5')]

database_connect("medhat", "01099514099", "5/5/2022", "6/5/2022", reservations)