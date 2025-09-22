MAX=100
MIN=0
total=0
done = False

print(f'You can enter up to {MAX} numbers.')


while not done:
    UserInput = int((input("Enter a number: ")))

    if UserInput > MAX:
      print(f"Sorry, the {UserInput} you enter is out of range!")
      done = True
    # tryAgain = input("Do you want to try again?' + '(enter y for yes): ")

    elif UserInput > MIN:
      total = total + UserInput
   
print(f'The total is {total}.')
 