# File: calculator.py
# Description: A simple calculator to demonstrate Git workflow and Python basics.
# Author: Soumya Subhashri Sahoo

def add(x, y):
    """
    Adds two numbers.
    Parameters:
        x (float): First number
        y (float): Second number
    Returns:
        float: The sum of x and y
    """
    return x + y

def subtract(x, y):
    """
    Subtracts the second number from the first.
    """
    return x - y

def multiply(x, y):
    """
    Multiplies two numbers.
    """
    return x * y

def divide(x, y):
    """
    Divides x by y.
    Includes error handling for division by zero.
    """
    if y == 0:
        return "Error! Division by zero."
    return x / y

def main():
    """
    Main function to run the calculator application.
    Handles user input and displays results.
    """
    print("--- Mini Calculator ---")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    
    choice = input("Enter choice(1/2/3/4): ")

    
    if choice in ('1', '2', '3', '4'):
        try:
            # Use float to allow decimal calculations
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            return

        
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            result = divide(num1, num2)
            if result == "Error! Division by zero.":
                 print(result)
            else:
                 print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid Input")


if __name__ == "__main__":
    main()