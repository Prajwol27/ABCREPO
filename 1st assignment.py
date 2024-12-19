#Print '1' if a is equal to b, print '2' if a is greater than b, otherwise print '3'.
def check():
    a = int(input('Enter 1st numb'))
    b = int(input('Enter 2nd numb'))
    if a>b:
        c=print('2')
    elif a==b:
        c=print('1')
    else:
        c=print('3')
    return c


# Check whether the user input number is even or odd and display it to user

def evenodd():
    a = int(input("Enter any number: "))
    if a%2==0:
        c=print("The number is even")
    else:
        c=print("The number is odd")
    return c

#WAP that asks the user for a number iin the rage of 1 to 12
# The program should display the corresponding month , where 1=jan, 2=feb and so on

def month():
    a = int(input("Enter number from 1-12 to get correspoinding month"))
    if a==1:
        print('January')
    elif a==2:
        print('Febraury')
    elif a==3:
        print('March')
    elif a==4:
        print('April')
    elif a==5:
        print('May')
    elif a==6:
        print('June')
    elif a==7:
        print('July')
    elif a==8:
        print('August')
    elif a==9:
        print('September')
    elif a==10:
        print('October')
    elif a==2:
        print('November')
    elif a==2:
        print('December')
    else:
        print("Invalid input!!!")



#4. A school has following rules for grading system:

#a. Below 25 - F

#b. 25 to 45 - E

#c. 45 to 50 - D

#d. 50 to 60 - C

#e. 60 to 80 - B

#f. Above 80 - A 

def grade():
    a = float(input("Enter your marks: "))
    if 0<=a>25:
        print("Your grade is F.")
    elif 25<=a<45:
        print("Your grade is E")
    elif 45<=a<50:
        print("Your grade is D")
    elif 50<=a<60:
        print("Your grade is C")
    elif 60<=a<80:
        print("Your grade is B")
    elif 80<a<=100:
        print("Your grade is A")
    else:
        print("Invalid Input!!!")

#5. Write a program to check whether a number is divisible by 7 or not.

def check7():
    a = int(input("Enter an integer: "))
    if a%7==0:
        print("It is divisible by 7")
    else:
        print("It is not divisible by 7")

#6. Write a program to accept two numbers and mathematical operators and perform operation accordingly.
#Like:
#Enter First Number: 7
#Enter Second Number : 9
#Enter operator : +
#Your Answer is : 16

def operator():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = input("Enter an operator: ")
    if c == '+':
        d=a+b
        print(d)
    elif c == '-':
        d=a-b
        print(d)
    elif c == '/':
        d=a/b
        print(d)
    elif c == '%':
        d=a%b
        print(d)
    elif c == '*':
        d=a+b
        print(d)
    elif c == '*':
        d=a+b
        print(d)
    else:
        d=print("Invalid input!!")
        print(d)


#7. Write a program to display "Hello" if a number entered by user is a multiple of five, otherwise print "Bye".

def multiple():
    a = int(input("Enter any integer: "))
    if a%5==0:
        print("Hello")
    else:
        print("Bye")

#8. Write a Python program that takes an integer input n n. 
#From given number, check if it is divisible by both 3 and 5, and print "FizzBuzz" if true. 
#If the number is divisible only by 5, print "Buzz." If it is divisible only by 3, print "Fizz." 
#Finally, if the number is not divisible by either 3 or 5, print the number itself.

def divby():
    a = int(input("Enter any integer: "))
    if a%5==0 and a%3==0:
        print("FizzBuzz")
    elif a%5==0:
        print("Fizz")
    elif a%3==0:
        print("Buzz")
    else:
        print(a)



#9. Write a Python program that takes a character input and checks whether it is a vowel or consonant

def vocon():
    a = (input("Enter a character: "))
    if a.isalpha():
        if a == 'a' or 'e' or 'i' or 'o' or 'u':
            print(str(a),"is a vowel.")
        else:
            print(str(a),"is a consonant")
    else:
        print("Enter a character.")


#10. Write a Python program to input marks and determine the grade based on the following conditions:
#90-100: A
#80-89: B
#70-79: C
#Below 70: Fail

def marks():
    a = float(input("Enter marks: "))
    if 90<=a<=100:
        print("Your grade is A.")
    elif 80<=a<90:
        print("Your grade is B")
    elif 70<=a<80:
        print("Your grade is C")
    else:
        print("Fail")


#11. Write a Python program to categorize a person’s age:
#Age < 13: Child
#13 <= Age <= 19: Teenager
#Age > 19: Adult

def age():
    a = int(input("Enter your age: "))
    if a < 13:
        print("Child")
    elif 13<=a<=19:
        print("Teenager")
    elif a>19:
        print("Adult")
    else:
        print("Invalid input!!")



#12.Write a Python program to check if a given character is uppercase, lowercase, or a digit in python.


def aldig():
    a = input("Enter a character: ")
    if a.isalpha():
        if a.islower():
            print("Your character is in lowercase")
        else:
            print("Your character is in uppercase")
    else:
        print("Enter an alphabate.")




#13. Write a Python program that takes a color as input ("Red", "Yellow", "Green") and outputs the corresponding action ("Stop", "Get Ready", "Go").

def traffic():
    while True:
        a = input("Enter a colour(Red, green or yellow):" )
        if a.isalpha():
            a = a.casefold()
            if a == 'red':
                print("Stop")
            elif a == 'yellow':
                print("Get ready")
            elif a == 'green':
                print('Go')
            else:
                print("Invalid character input!!")
        else:
            print("Invalid input")





#14. Write a Python program to check eligibility for a job based on age and experience:
# Age > 18 and Experience >= 2 years: Eligible
# Otherwise: Not Eligible

def job():
    age = int(input("Enter your age: "))
    exp = int(input("Enter your experience: "))
    if age>18:
        if exp>=2:
            print("Eligible")
        else:
            print("Not eligible")
    else:
        print("Not eligible")

#15. Write a Python program to give advice based on the temperature:
# Temperature > 30°C: "It's hot, stay hydrated!"
# Temperature between 15-30°C: "Enjoy the weather!"
# Temperature < 15°C: "It's cold, wear warm clothes!"

def temp():
    a = float(input("Enter the temperature in °C: "))
    if a>30:
        print("It's hot, stay hydrated!")
    elif 15<a<=30:
        print("Enjoy the weather!")
    elif a<15:
        print("It's cold, wear warm clothes!")
    else:
        print("Invalid input!!")


#16. Write a Python program that takes a menu option ("Pizza", "Burger", "Pasta") and prints its price:
# Pizza: $10
# Burger: $7
# Pasta: $8

def menu():
    a = input("Pick one in between pizza, burger and pasta: ")
    b = (a.upper())
    if(b=="PIZZA"):
        print("$10")
    elif(b=="BURGER"):
        print("$7")
    elif(b=="PASTA"):
        print("$8")


#17. Write a Python program to select players based on height:
# Height >= 6 feet: Selected
# Height < 6 feet: Not Selected

def height():
    a = float(input("Enter your height in feet: "))
    if(a>=6):
        print("Selected.")
    else:
        print("Not Selected.")




#18. Write a Python program to check if a person is eligible to watch a movie based on their age:
# Age >= 18: Allowed
# Age < 18: Not Allowed

def anime():
    a = int(input("Enter your age in digits: "))
    if(a>=18):
        print("You can watch the movie.")
    elif(a<18):
        print("You cannot watch the movie.")



#19. Write a Python program to check login credentials:
# Username: "admin", Password: "password123"
# If correct, print "Access Granted"; otherwise, print "Access Denied."

def login():
    a = input("Enter yoru Username: ")
    b = input("Enter your Password: ")
    if(a=="admin" and b=="password123"):
        print("Access Granted.")
    else:
        print("Access Denied.")

#20. Write a Python program that takes a month number (1–12) and outputs the corresponding season:
# 12, 1, 2: "Winter"
# 3, 4, 5: "Spring"
# 6, 7, 8: "Summer"
# 9, 10, 11: "Autumn"

def month():
    a = int(input("Enter any number(1-12): "))
    if(a==1 or a==2 or a==12):
        print("Winter.")
    elif(a==3 or a==4 or a==5):
        print("Spring.")
    elif(a==6 or a==7 or a==8):
        print("Summer.")
    elif(a==9 or a==10 or a==11):
        print("Autum.")
    else:
        print("Invalid input!!")



#21. Write a Python program to check car loan eligibility:
# Salary >= 50,000 and Credit Score >= 700: "Eligible"
# Otherwise: "Not Eligible"


def loan():
    a = int(input("Enter your salary amount in digits: "))
    b = int(input("Enter your credit score in digits: "))
    if(a>=50000 and b>=700):
        print("Eligible.")
    else:
        print("Not Eligible.")






#22. Write a program to check whether the given number is in between 1 and 100 or not.


def between():
    a = int(input("Enter any number: "))
    if(a>=1 and a<=100):
        print("The number lies in between one and one hundred.")
    else:
        print("The number does not lie in between one and one hundred.")
