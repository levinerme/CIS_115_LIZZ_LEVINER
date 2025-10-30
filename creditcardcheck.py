ccNum =input("Enter your credit card number.")

def validateCreditCard(ccNum):
    reversingccNum = ccNum[::-1]
    cardNumbers = [int(x) for x in ccNum]

for i in range (1, len(input), 2):
    input[i] *=2

    if input[i] >9:
        input[i] =input[i] % 10 + 1
    total = sum(input)
    return total % 10 == 0    

if total == 0:
    print(f"The credit card number {ccNum} is valid!")
else:
    print(f"Invalid credit card number {ccNum} entered. Please try again.")
validateCreditCard(ccNum)