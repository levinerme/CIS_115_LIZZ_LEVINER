num1 = input("What's your first number? ")
num2 = input("What's your second number? ")
diff = int(num1) - int(num2)

print("You total after being subtracted is {0}".format(diff))

if diff < 0:
    print("Invaild! The value is less than zero!")

elif diff > 0:
    print("The values enetered were vaild intergers")

