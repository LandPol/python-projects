def kmToMiles(x):
    x *= 0.621371
    return x
    
def milesToKm(x):
    return x * 1.60934

def CtoF(x):
    return x * 9 / 5 + 32

def FtoC(x):
    return (x - 32) * 5 / 9

def menu():
    while True:
        print("\n--- Python Unit Converter ---\n")
        print("Convert: ")
        print("1. Km to Miles")
        print("2. Miles to Km")
        print("3. C to F")
        print("4. F to C")
        print("5. End")
        while True:
            try:
                m = int(input("Choose mode: "))
                break
            except ValueError:
                print("Error: Invalid mode")
        if m > 0 and m < 6:
            if m != 5:
                while True:
                    try:
                        x = float(input("Input your value: "))
                        break
                    except ValueError:
                        print("Error: Invalid value")
            result = None
            match m:
                case 1: result = kmToMiles(x)
                case 2: result = milesToKm(x)
                case 3: result = CtoF(x)
                case 4: result = FtoC(x)
                case 5:
                    print("Exiting...")
                    break
            if result is not None:
                result = round(result, 2)
                print("Your converted value is: " + str(result) + "\n\n")
        else:
            print("Invalid mode. Try again\n\n")

menu()