def printWordList():
    word=["Apples", "Bananas", "Pears", "Carrots"]

    counter = 0
    for i in word:
       print(i)
       counter += 1

    print(f"You looped  {counter} times")
printWordList()