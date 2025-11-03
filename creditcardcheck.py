

ccNum =input("Enter your credit card number: ")

def validateCreditCard(ccNum):
    ccNum = ccNum[::-1]

    odd_digits = 0
    even_digits = 0
    total = 0
    for x in ccNum[::2]:
        odd_digits += int(x)
    for x in ccNum[1::2]:
        x = int(x) * 2
        if x >= 10:
            even_digits += (1 + ( x % 10))
        else:
            even_digits = x
        total = odd_digits + even_digits
        
    if total % 10== 0:
      print(f"The credit card number {ccNum} is valid!")
    else:
        print(f"Invalid credit card number {ccNum} entered. Please try again.")
validateCreditCard(ccNum)
