print("Simple Calculator\n")
print("Select operations:")
print('''
        Addition (+)
        Subtraction (-)
        Multiplication (*)
        Division (/)
      ''')

choice = input("Enter choice (+, -, *, /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == "+":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")

elif choice == "-":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")

elif choice == "*":
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")

elif choice == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero!")

else:
    print("Invalid input! Please select from +, -, *, /.")