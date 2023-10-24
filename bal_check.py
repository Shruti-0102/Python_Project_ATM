import sqlite3 as db


def get_user_balance(acc_no):

    try:
        conn = db.connect('ATM.db')
        cur = conn.cursor()

        cur.execute('SELECT U_bal FROM USER WHERE acc_no = ?', (acc_no,))
        result = cur.fetchone()

        conn.close()

        if result:
            return result[0]
        else:
            return None
    except Exception as e:
        print("Invalid Input")


def bal():
    try:
        acc_no = input("Enter your account number : ")
        balance = get_user_balance(acc_no)

        if balance is not None:
            print(f'Your balance is: Rs.{balance:.2f}')
        else:
            print('User not found.')
    except Exception as e:
        print("Invalid Input")