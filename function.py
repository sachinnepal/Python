

def ADD(num1, num2=10):
    sum = num1 + num2
    print(f"Sum of {num1} and {num2} is: {sum}")

def SUB(num1, num2=5):
    diff = num1 - num2
    print(f"Difference of {num1} and {num2} is: {diff}")    

def DIV(num1, num2=2):
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        return
    quotient = num1 / num2
    print(f"Quotient of {num1} and {num2} is: {quotient}")

def MUL(num1, num2=3):
    product = num1 * num2
    print(f"Product of {num1} and {num2} is: {product}")

