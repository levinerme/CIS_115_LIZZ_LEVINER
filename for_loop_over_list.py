def getMyList():
    MyList= [10,20,30,40,50,60]

    counter = 0
    for i in MyList:
       print(i)
       counter += 1

    print(f"You looped  {counter} times")
getMyList()