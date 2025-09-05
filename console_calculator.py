import math

def addition(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def multiplication(a,b):
    return a * b

def division(a,b):
    if b == 0:
        print("Error: divided by 0")
        return a
    return a / b

def modulo(a,b):
    return a % b

def power(a,b):
    return a ** b

def extraction(a,b):
    return a ** (1/b)

def factorial(a):
    a = int(a)
    if a < 0:
        print("Error: factorial of negative number")
        return 1
    if a <= 1:
        return 1
    else:
        x = 1
        while a > 1:
            x *= a
            a -= 1
        return x

def menu(a):
    print("Your number is: " + str(a))
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. /")
    print("5. %")
    print("6. ^")
    print("7. sqrt")
    print("8. !")
    print("9. Delete all")
    print("10. Quit")
    while True:
        try:
            m = int(input("Choose your action:"))
            if m < 1 or m > 10:
                print("Incorrect action")
                continue
            break
        except ValueError:
            print("Incorrect action")
    
    if m < 8:
        while True:
            try:
                b = float(input("Input number: "))
                break
            except ValueError:
                print("Invalide number")
    if m == 1:
        r = addition(a,b)
    elif m == 2:
        r = subtraction(a,b)
    elif m == 3:
        r = multiplication(a,b)
    elif m == 4:
        r = division(a,b)
    elif m == 5:
        r = modulo(a,b)
    elif m == 6:
        r = power(a,b)
    elif m == 7:
        r = extraction(a,b)
    elif m == 8:
        print("\n\n")
        r = factorial(a)
    elif m == 9:
        print("\n\n")
        return menu(0)
    elif m == 10:
        print("Ended")
        return
    print("\n\n")
    menu(r)

menu(0)