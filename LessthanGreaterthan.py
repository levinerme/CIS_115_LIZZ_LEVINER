num1 = input("What's the first number? ")
num2 = input("whats the second number? ")
sum = int(num1) + int(num2)
print("your total sum is {0}". format(sum))

num3 = input("What's your third number? ")

divided = int(sum) / int(num3)
print("Your total after being divided is {0}". format(divided))

if divided > 0:
    print ("The mathematical operation is >0 ")     

elif divided < 0:
    print("The mathematical operation is <= 0")