def calculate_bmi(h,w):
    h /= 100
    bmi = round(w / (h ** 2), 2)
    return bmi

def menu():
    while True:
        print("\n --- BMI Calculator --- \n")
        while True:
            try:
                w = float(input("Input your weight (kg): "))
                break
            except ValueError:
                print("ERROR: Invalid value")
        while True:
            try:
                h = float(input("Input your height (cm): "))
                break
            except ValueError:
                print("ERROR: Invalid value")
        bmi = calculate_bmi(h, w)
        feedback = ""
        if bmi < 18.5:
            feedback = "Underweight"
        elif 18.5 <= bmi < 25:
            feedback = "Normal weight"
        elif 25 <= bmi < 30:
            feedback = "Overweight"
        else:
            feedback = "Obesity"
        
        print("Your BMI is: " + str(bmi) + " and you are: " + feedback)

        again = input("\n Do you want to calculate again? (y/n): ").lower()
        if again != "y":
            print("Goodbye")
            break

menu()