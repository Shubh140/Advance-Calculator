
import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def square_root(x):
    if x < 0:
        return "Error! Cannot take square root of a negative number."
    else:
        return math.sqrt(x)

def exponentiation(x, y):
    return x ** y

def factorial(x):
    if x < 0:
        return "Error! Factorial of a negative number doesn't exist."
    else:
        return math.factorial(int(x))

def logarithm(x, base):
    if x <= 0:
        return "Error! Logarithm undefined for non-positive values."
    else:
        return math.log(x, base)

def sine(x, in_degrees=False):
    if in_degrees:
        x = math.radians(x)
    return math.sin(x)

def cosine(x, in_degrees=False):
    if in_degrees:
        x = math.radians(x)
    return math.cos(x)

def tangent(x, in_degrees=False):
    if in_degrees:
        x = math.radians(x)
    return math.tan(x)

def calculator():
    print("Advanced Calculator")
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Exponentiation (x^y)")
    print("7. Factorial")
    print("8. Logarithm (log base n)")
    print("9. Sine")
    print("10. Cosine")
    print("11. Tangent")

    while True:
        choice = input("Enter choice (1-11): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")

        elif choice == '5':
            num = float(input("Enter a number: "))
            print(f"√{num} = {square_root(num)}")

        elif choice == '6':
            num1 = float(input("Enter the base number: "))
            num2 = float(input("Enter the exponent: "))
            print(f"{num1}^{num2} = {exponentiation(num1, num2)}")

        elif choice == '7':
            num = int(input("Enter a number (integer): "))
            print(f"{num}! = {factorial(num)}")

        elif choice == '8':
            num = float(input("Enter the number: "))
            base = float(input("Enter the base (default is 10 if not sure): ") or 10)
            print(f"log_{base}({num}) = {logarithm(num, base)}")

        elif choice in ['9', '10', '11']:
            num = float(input("Enter the angle: "))
            angle_type = input("Is this in degrees? (yes/no): ").lower() == 'yes'

            if choice == '9':
                print(f"sin({num}) = {sine(num, angle_type)}")

            elif choice == '10':
                print(f"cos({num}) = {cosine(num, angle_type)}")

            elif choice == '11':
                print(f"tan({num}) = {tangent(num, angle_type)}")

        else:
            print("Invalid input!")

        next_calc = input("Do you want to perform another calculation? (yes/no): ")
        if next_calc.lower() != 'yes':
            break

if __name__ == "__main__":
    calculator()