num1 = int(input("What's your first number?: "))
num2 = int(input("What's your second number?: "))

def max(num1, num2):

    if (num1 > num2):
        print(f"Your first number {num1}  is greater than your second number {num2}!")
    elif (num1 < num2):
        print(f"Your second number {num2}  is greater than your first number {num1}!")
max(num1, num2)