print("********************\nWelcome to the our ATM Machines \n********************")

print("""
Transactions:

1. Balance Inquiry
2. Deposit
3. Deposit Money

You can exit the program with the 'q' key.

""")

balance  = 1000 # Your balance is 1000

while True:
    transaction = input("Please enter the transaction: ")

    if (transaction == "q"):
        print("We wait again....")
        break
    elif (transaction == "1"):
        print(f"Your balance {balance} £")

    elif (transaction == "2"):
        amount = int(input("The amount you want to deposit: "))

        balance += amount

        print(f"Your balance {balance} £")

    elif (transaction == "3"):
        amount = int(input("The amount you want to withdraw: "))
        if (balance - amount < 0 ):
            print("You cannot withdraw this much money because your balance is not enough for this amount...")
            print(f"Your balance {balance} £")
            continue
        balance -= amount
        print(f"Your balance {balance} £")

    else:
        print("Please enter a valid transaction.")
