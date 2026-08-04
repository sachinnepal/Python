from function import ADD,SUB,DIV,MUL
import random


id = random.randint(1000,9999)
print(f"Your USER ID is: {id}")

MENU = """

1. ADD
2. SUB
3. DIV
4. MUL
5. EXIT

"""

while True:
    print(MENU)

    choice =input("Enter your choice (1-5): ")

    if choice == "1":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number (default is 10): ") or 10)
        ADD(num1, num2)

    elif choice == "2":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number (default is 5): ") or 5)
        SUB(num1, num2)

    elif choice == "3":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number (default is 2): ") or 2)
        DIV(num1, num2)

    elif choice == "4":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number (default is 3): ") or 3)
        MUL(num1, num2)

    elif choice == "5":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")
