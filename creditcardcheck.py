ccNum =input("Enter your credit card number.")

def validateCreditCard(ccNum):
    ccNum = ccNum[::-1]
    ccNum = [int(x) for x in ccNum]

for i in range (1, len(ccNum)):
    ccNum [i] *=2

    if ccNum[i] >9:
        ccNum[i] =ccNum[i] % 10 + 1  

    total = sum(ccNum)
    return(total % 10) == 0

if total == 0:
    print(f"The credit card number {ccNum} is valid!")
else:
    print(f"Invalid credit card number {ccNum} entered. Please try again.")
validteCreditCard(ccNum)
