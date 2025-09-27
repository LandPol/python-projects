import random

numbers = ['0','1','2','3','4','5','6','7','8','9']

lowercase_letters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]

uppercase_letters = [
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]

special_characters = [
    '!','@','#','$','%','^','&','*','(',')','-','_',
    '=','+','[',']','{','}',';',':','"',"'","\\",'|',
    ',','.','<','>','/','?','~','`'
]

def generate_password(c, l):
    pas = ""
    while l > 0:
        char_list = random.choice(c)
        pas = pas + random.choice(char_list)
        l -= 1
    return pas


def menu():
    while True:
        print("\n --- Password Generator --- \n")
        while True:
            try:
                l = int(input("Input password length (6 to 12): "))
                break
            except ValueError:
                print("Error: Invalid value")
        if l > 12 or l < 6:
            print("Invalid length")
            menu()
            break
        else:
            char_sets = []
            print("Choose what your password should include")
            while True:
                try:
                    n = int(input("Numbers (1 yes): "))
                    break
                except ValueError:
                    print("Error: Invalid action")
            if n == 1:
                char_sets.append(numbers)
            while True:
                try:
                    n = int(input("Lowercase letters (1 yes): "))
                    break
                except ValueError:
                    print("Error: Invalid action")
            if n == 1:
                char_sets.append(lowercase_letters)
            while True:
                try:
                    n = int(input("Uppercase letters (1 yes): "))
                    break   
                except ValueError:
                    print("Error: Invalid action")
            if n == 1:
                char_sets.append(uppercase_letters)
            while True:
                try:
                    n = int(input("Special characters (1 yes): "))
                    break
                except ValueError:
                    print("Error: Invalid action")
            if n == 1:
                char_sets.append(special_characters)

            print(generate_password(char_sets, l))

menu()
