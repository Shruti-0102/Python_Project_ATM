import sqlite3 as db

con = db.connect("ATM.db")
cur = con.cursor()


def transactions():
    try:
        user_inp = int(input("Enter your account number: "))

        # Use ORDER BY to sort transactions by a timestamp column (replace 'timestamp_column' with the actual column name)
        cur.execute(f"SELECT * FROM USER_TRANSACTIONS WHERE sender_a_no = {user_inp} LIMIT 10")
        transactions = cur.fetchall()
        print("Sender ||  Reciever || Amount || Balance || Date & Time")
        if transactions:

            for transaction in transactions:
                print('\n')
                print(transaction)  # Replace with appropriate display format
        else:
            print("No transactions found for the user.")
    except Exception as e:
        print("Invalid Input")