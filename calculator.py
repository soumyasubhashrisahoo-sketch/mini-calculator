# File: calculator.py
# Description: A simple calculator to demonstrate Git workflow and Python basics.
# Author: Ayush Kumar Nayak

def add(a, b):
    """ Returns the sum of two numbers. """
    return a + b

def subtract(a, b):
    """ Returns the difference between two numbers. """
    return a - b

def multiply(a, b):
    """ Returns the product of two numbers. """
    return a * b

def divide(a, b):
    """ 
    Returns the division of a by b. 
    Prevents crash on division by zero.
    """
    if b == 0:
        return "Cannot divide by zero."
    return a / b

def run_calculator():
    """
    Primary execution loop for the calculator.
    Cycles until the user decides to exit.
    """
    while True:
        print("\n" + "="*25)
        print("   BASIC MATH TOOL   ")
        print("="*25)
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("Q. Quit Program")
        print("-" * 25)

        user_choice = input("Select an operation (1-4 or Q): ").lower()

        if user_choice == 'q':
            print("Exiting calculator. Goodbye!")
            break

        if user_choice in ('1', '2', '3', '4'):
            try:
                val1 = float(input("Input first number:  "))
                val2 = float(input("Input second number: "))
            except ValueError:
                print("Error: Please enter valid numeric digits only.")
                continue # Skips the rest of the loop and starts over

            if user_choice == '1':
                print(f"\nResult: {val1} + {val2} = {add(val1, val2)}")
            
            elif user_choice == '2':
                print(f"\nResult: {val1} - {val2} = {subtract(val1, val2)}")
            
            elif user_choice == '3':
                print(f"\nResult: {val1} * {val2} = {multiply(val1, val2)}")
            
            elif user_choice == '4':
                output = divide(val1, val2)
                if output == "Cannot divide by zero.":
                    print(f"\nError: {output}")
                else:
                    print(f"\nResult: {val1} / {val2} = {output}")
        else:
            print("\nInvalid selection. Please choose 1, 2, 3, 4, or Q.")

if __name__ == "__main__":
    run_calculator()