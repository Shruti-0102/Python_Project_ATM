import sqlite3 as db
import about, pin_gen, bal_check, cash_withdrawal, transfer, transactions, deposit
import os

title = '''
 ____ ____ ____ ____ ____ ____ _________ ____ ____ ____ 
||B |||H |||A |||R |||A |||T |||       |||A |||T |||M ||
||__|||__|||__|||__|||__|||__|||_______|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|
'''
con = db.connect("ATM.db")
cursor = con.cursor()

con.execute('''CREATE TABLE IF NOT EXISTS USER(
  acc_no INT(20) PRIMARY KEY, 
  mob_no INT(12), 
  U_name VARCHAR(20), 
  U_bal FLOAT(100), 
  U_pin INT(4))''')

con.commit()

con.execute('''CREATE TABLE IF NOT EXISTS USER_TRANSACTIONS (
  sender_a_no INT(30),
  receiver_a_no INT(30),
  amount INT(20),
  updated_balance INT(20),
  Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, 
  FOREIGN KEY(sender_a_no)REFERENCES USER(u_account_number),
  FOREIGN KEY(receiver_a_no)REFERENCES USER(u_account_number))''')

con.commit()
'''
con.execute("INSERT INTO USER VALUES(987654321, 8770567779, 'SATYAJIT DEY', 74821.39, 0000)")
con.execute("INSERT INTO USER VALUES(987654322, 9905454099, 'VIVEK HINGE', 65929.92, 0000)")
con.execute("INSERT INTO USER VALUES(987654323, 7773885610, 'RISHI PONGADE', 92341.03, 0000)")
con.execute("INSERT INTO USER VALUES(987654324, 8989202651, 'SHRUTI MINOCHA', 61872.45, 0000)")
con.execute("INSERT INTO USER VALUES(987654325, 9435084689, 'JANARDAN PATIL', 54723.6, 0000)")
con.execute("INSERT INTO USER VALUES(987654326, 9952567839, 'AMIT KUMAR', 87342.59, 0000)")
con.execute("INSERT INTO USER VALUES(987654327, 7659083453, 'VIKAS SINGH', 53985.12, 0000)")

con.commit()
'''
x = True

while x:
    print(title)
    print('''
Options :
1 - About 
2 - Pin Generation
3 - Cash Withdrawal
4 - Cash Transfer
5 - Check Balance
6 - Last 10 Transactions 
7 - Cash Deposit 
8 - Exit

''')

    ch = int(input("Enter your choice : "))


    if ch == 1:
        about.about()
        input("Press enter to continue")
        os.system('clear')
    elif ch == 2:
        pin_gen.GeneratePin()
        input("Press enter to continue")
        os.system('clear')
    elif ch == 3:
        cash_withdrawal.WithdrawMoney()
        input("Press enter to continue")
        os.system('clear')
    elif ch == 4:
        transfer.transfer_cash()
        input("Press enter to continue")
        os.system('clear')
    elif ch == 5:
        bal_check.bal()
        input("Press enter to continue")
        os.system('clear')
    elif ch == 6:
        transactions.transactions()
        input("Press enter to continue")
        os.system('clear')
    elif ch == 7:
        deposit.DepositMoney()
        input("Press enter to continue")
        os.system('clear')
    elif ch == 8:
        print("Thank you! Have a nice day!")
        x = False
    else:
        print("Invalid Input")
        os.system('clear')