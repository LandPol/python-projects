import random

def roll():
    n = random.randint(1, 6)
    return n

def menu():
    while True:
        print("\n Welcome to Dice Roll Simulator 🎲 \n")
        a = input("Press ENTER to roll the dice or type 'q' to quit: ")
        if a == 'q':
            break
        else:
            while True:
                r = roll()
                print(f"You rolled a {r} 🎲")
                n = input("Roll again? (y/n): ")
                if n != 'y':
                    break
        break
menu()