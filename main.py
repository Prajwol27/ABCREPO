
import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 10

def deposit():
    while True:
        amount = input("Enter the amount you want to deposit? :\n")
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print("The amount must be greater than zero.")
        else:
            print("Please enter a digit.")
    return amount


def number_of_lines():
    while True:
        lines = input("Enter the amount of lines you want to bet on: (1 - " +str(MAX_LINES)+ ")? \n")
        if lines.isdigit():
            lines = int(lines)
            if 0<lines<=MAX_LINES:
                break
            else:
                print("The lines must be 1-3.")
        else:
            print("Enter the value in digit.")
    return lines

def bet_amt():
    while True:
        amount = input("Enter the amount you want to bet:("+str(MIN_BET)+"-"+str(MAX_BET)+")")
        if amount.isdigit():
            amount = int(amount)
            if 10<amount<=100:
                break
            else:
                print("Enter amount from "+str(MIN_BET)+"-"+str(MAX_BET)+".")
        else:
            print("Enter amount in numbers.")
    return amount
        
            

def main():
    balance = deposit()
    lines = number_of_lines()
    bet = bet_amt() 
    while True:
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have sufficient balance.")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines so your total bet is {total_bet}")
    print(balance, lines, bet)
    
main()

