import sqlite3 as db


def GeneratePin():
    con = db.connect("ATM.db")

    try:

        mob = int(input("Please enter your Registered Mobile Number: "))
        cursor = con.cursor()

        # Check if the mobile number exists in the database
        cursor.execute(f"SELECT * FROM USER WHERE mob_no = {mob}")
        con.commit()
        user = cursor.fetchone()

        if user:
            print("Please Proceed with Entering your New PIN")
            pin_inp = int(input("Please type your PIN here: "))

            if len(str(pin_inp)) <= 4 <= len(str(pin_inp)):
                # Update the user's PIN in the database
                cursor.execute(f"UPDATE USER SET U_pin = {pin_inp} WHERE mob_no = {mob}")
                con.commit()
                print("PIN set Successfully...")
            else:
                print("Please Enter a Valid 4-digit PIN!")
        else:
            print("Mobile Number NOT Registered, please Contact Bank Officials or Re-enter Mobile Number!")
    except Exception as e:
        print("Invalid Input")
    con.close()

