# Simple Calculator Function
def calculator():
    print("Welcome to the Simple Calculator!")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # User input for operation
    operation = input("Enter choice (1/2/3/4): ")

    # Input numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == '1':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operation == '2':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operation == '3':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif operation == '4':
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Error: Division by zero!")
    else:
        print("Invalid input")

# Run the calculator
calculator()
