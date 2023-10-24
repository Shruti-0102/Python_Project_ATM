import sqlite3 as db

con = db.connect("ATM.db")
cursor = con.cursor()


def transfer_cash():

    try:
        sender_account_no = input("Enter your account number: ")
        cursor.execute(f"SELECT U_name FROM USER WHERE acc_no = ?", (sender_account_no,))
        sender_present = cursor.fetchone()
        con.commit()

        pin = int(input("Enter your PIN: "))
        cursor.execute("SELECT U_pin FROM USER WHERE acc_no = ?", (sender_account_no,))
        acc_pin = cursor.fetchone()

        con.commit()

        if sender_present:
            if pin == int(acc_pin[0]):  # The fetched PIN is a tuple, so we use [0] to get the actual PIN.
                receiver_account_no = input("Enter the receiver's account number: ")
                cursor.execute(f"SELECT * FROM USER WHERE acc_no = ?", (receiver_account_no,))
                reciever_present = cursor.fetchone()
                con.commit()

                if reciever_present:
                    amount = float(input("Enter the amount to transfer: "))
                    cursor.execute(f"SELECT U_bal FROM USER WHERE acc_no = ?", (sender_account_no,))
                    bal_sender = cursor.fetchone()
                    con.commit()

                    bal_receiver = cursor.execute(f"SELECT U_bal FROM USER WHERE acc_no = ?", (receiver_account_no,))
                    bal_receiver = cursor.fetchone()
                    con.commit()


                    if int(amount) <= float(bal_sender[0]):
                        sender_new_bal = float(bal_sender[0]) - amount
                        receiver_new_bal = float(bal_receiver[0]) + amount

                        cursor.execute("UPDATE USER SET U_bal = ? WHERE acc_no = ?", (sender_new_bal, sender_account_no))
                        cursor.execute("UPDATE USER SET U_bal = ? WHERE acc_no = ?",
                                       (receiver_new_bal, receiver_account_no))
                        con.commit()

                        print("Transfer Successfully Done!!!")
                        print(f'Your new balance: Rs.{sender_new_bal}')

                        cursor.execute(f"INSERT INTO USER_TRANSACTIONS ('sender_a_no', 'receiver_a_no', 'amount', 'updated_balance') VALUES({sender_account_no},{receiver_account_no}, {amount}, {sender_new_bal})")
                        con.commit()

                    else:
                        print("Insufficient Balance.")
                else:
                    print("Receiver's account does not exist.")
            else:
                print("Incorrect PIN.")
        else:
            print("Account not found.")

    except Exception as e:
        print("Invalid Input")