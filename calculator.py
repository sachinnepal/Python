operator = input("Enter an operator (+ - * /): ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
    print(f"Result: {result}")

elif operator == "-":
    result = num1 - num2
    print(f"Result: {result}")

elif operator == "*":
    result = num1 * num2
    print(f"Result: {result}")

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {result}")
    else:
        print("Error: Cannot divide by zero")

else:
    print("Operator not detected")