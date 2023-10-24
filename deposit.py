import sqlite3 as db


con = db.connect("ATM.db")
cursor = con.cursor()

def DepositMoney():


    try:
        acc_no = int(input("Enter account number: "))
        pin = int(input("Please Enter Your PIN: "))

        cursor.execute("SELECT * FROM USER WHERE acc_no = ? AND U_PIN = ?", (acc_no, pin))
        user = cursor.fetchone()

        if user:
            amt = int(input("Enter the amount You want to Deposit: "))
            print("Please insert cash into the machine")
            input("Press ENTER when done")

            cursor.execute("SELECT U_bal FROM USER WHERE acc_no = ?", (acc_no,))
            current_balance = cursor.fetchone()[0]

            updated_balance = current_balance + amt

            cursor.execute("UPDATE USER SET U_bal = ? WHERE acc_no = ?", (updated_balance, acc_no))
            con.commit()
            print(f"Money Deposited Successfully. Your Updated Balance is Rs.{updated_balance}")
        else:
            print("Invalid account number or PIN")
    except db.Error as e:
        print(f"Database error: {e}")
        print("Invalid PIN")



