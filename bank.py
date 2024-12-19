
#Creating a bank where we type 
# 1 for Balance check
# 2 for Deposite (where maximum amount deposited can be upto 10 lakhs per deposit.)
# 3 for Withdrawl
# 4 to Exit

EXIT = "Thankyou for choosing us."
BALANCE = 10000

def check():
    while True:
                print("Your balance is: $"+ BALANCE)
            

def deposit():
    while True:
        deposit = input("Enter the amount you want to deposit: $")
        if deposit.isdigit():
            deposit=float(deposit)
            if 0<deposit<=1000000:
                cbalance = BALANCE + deposit
                break
            else:
                print("Invalid input enter balance form (0-1000000)")
        else:
            print("Enter amount in digits!!!")
    print(str(EXIT))

def withdrawl():
    while True:
        withdrawl = input("Enter the amount you want to withdrawl: $")
        if withdrawl.isdigit():
            withdrawl = float(withdrawl)
            if 0<withdrawl<=BALANCE:
                curbalance = BALANCE-withdrawl
                print(f"Withdraw Successful!!\nYour current balance is: {curbalance}")
            else:
                curbalance = print("Infufficient Balance!!")
        else:
            print("Invalid input!!!")
    print(str(EXIT))

def exitt():
    while true:
        print(str(EXIT))

def main():
    while True:
        inp = (input(" Enter (1-4)  \n1. for Balance check\n2. for Deposite (where maximum amount deposited can be upto 10 lakhs per deposit.)\n3. for Withdrawl\n4. to Exit\nInput:"))
        if inp.isdigit():
            if inp == 1:
                check()
            elif inp == 2:
                deposit()
            elif inp == 3:
                withdrawl()
            elif inp == 4:
                exitt()
        else:
            print("Invalid input!!!")


main()