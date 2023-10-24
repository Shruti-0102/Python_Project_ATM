import sqlite3 as db

# Connect to the database
con = db.connect("ATM.db")
cursor = con.cursor()

def WithdrawMoney():

    try:

        acc_no = int(input("Enter account number: "))
        pin = int(input("Please Enter Your PIN: "))
        # Check if the account number and PIN are valid using a parameterized query
        cursor.execute("SELECT * FROM USER WHERE acc_no = ? AND U_PIN = ?", (acc_no, pin))
        user = cursor.fetchone()

        if user:
            amt = int(input("Enter the amount You want to Withdraw: "))
            # Retrieve the current balance using a parameterized query
            cursor.execute("SELECT U_bal FROM USER WHERE acc_no = ?", (acc_no,))
            current_balance = cursor.fetchone()[0]

            if amt > current_balance:
                print("Insufficient balance. Withdrawal failed.")
            else:
                updated_balance = current_balance - amt
                # Update the balance in the database using a parameterized query
                cursor.execute("UPDATE USER SET U_bal = ? WHERE acc_no = ?", (updated_balance, acc_no))
                con.commit()
                print(f"Money Withdrawn Successfully. Your Updated Balance is Rs.{updated_balance}")
        else:
            print("Invalid account number or PIN")
    except Exception as e:
        print("Invalid Input")



