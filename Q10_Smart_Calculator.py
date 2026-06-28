# Q10: Smart Calculator & Data Manager

import math
import random

history = {}

# Function for Basic Arithmetic
def basic_arithmetic():
    try:
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))

        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = int(input("Choose Operation: "))

        if choice == 1:
            result = num1 + num2
            operation = "Addition"

        elif choice == 2:
            result = num1 - num2
            operation = "Subtraction"

        elif choice == 3:
            result = num1 * num2
            operation = "Multiplication"

        elif choice == 4:
            if num2 == 0:
                print("Division by zero is not allowed.")
                return
            result = num1 / num2
            operation = "Division"

        else:
            print("Invalid Choice!")
            return

        print("Result:", result)
        history[operation] = result

    except ValueError:
        print("Invalid Input!")


# Function for Scientific Calculations
def scientific_calculation():
    try:
        print("\n1. Square Root")
        print("2. Power")

        choice = int(input("Choose Option: "))

        if choice == 1:
            num = float(input("Enter Number: "))
            result = math.sqrt(num)
            print("Square Root:", result)
            history["Square Root"] = result

        elif choice == 2:
            base = float(input("Enter Base: "))
            exponent = float(input("Enter Exponent: "))
            result = math.pow(base, exponent)
            print("Answer:", result)
            history["Power"] = result

        else:
            print("Invalid Choice!")

    except ValueError:
        print("Invalid Input!")


# Function for Random Numbers
def random_numbers():
    try:
        start = int(input("Enter Starting Number: "))
        end = int(input("Enter Ending Number: "))

        num = random.randint(start, end)

        print("Random Number:", num)

        history["Random Number"] = num

    except ValueError:
        print("Invalid Input!")


# View History
def view_history():

    if len(history) == 0:
        print("No History Available.")

    else:
        print("\nCalculation History")
        for key, value in history.items():
            print(key, ":", value)


# Main Program
while True:

    print("\n===== Smart Calculator =====")
    print("1. Basic Arithmetic")
    print("2. Scientific Calculation")
    print("3. Generate Random Number")
    print("4. View History")
    print("5. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        basic_arithmetic()

    elif choice == 2:
        scientific_calculation()

    elif choice == 3:
        random_numbers()

    elif choice == 4:
        view_history()

    elif choice == 5:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")