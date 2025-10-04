import random

def chooseRange():
    print("Choose range")
    while True:
        try:
            start = int(input("Starting value: "))
            end = int(input("Ending value: "))
            if 0 < start < end:
                break
            else:
                print("Invalid values.")
        except ValueError:
            print("ERROR: Invalid value.")
    return start, end

def chooseNumber(start, end):
    n = random.randint(start, end)
    return n

def checkGuessed(n, number):
    if n == number:
        print("Your answer is correct!")
        return True
    elif n < number:
        print("Your number is lower.")
    else:
        print("Your number is higher.")
    return False
    

def game():
    print("--- Guessing number game ---")
    start, end = chooseRange()
    number = chooseNumber(start, end)
    c = 1
    while True:
        while True:
            try:
                n = int(input("\nInput your guess: "))
                break
            except ValueError:
                print("ERROR: Invalid value.")
        if checkGuessed(n, number):
            print(f"It takes you {c} attempt/s")
            break
        else:
            c += 1


game()