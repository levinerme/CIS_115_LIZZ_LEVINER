num1 = input("What's your first number? ")
num2 = input("Whats your first number? ")

sum = int(num1)%int(num2)

if sum == 0:
    print("This is even operation! Your remainder is {0}.".format(sum))
elif sum > 0:
    print("This is an odd operation! Your remainder is {0}.".format(sum))