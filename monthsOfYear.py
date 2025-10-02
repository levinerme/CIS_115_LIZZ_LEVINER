startMonth = int(input("What's the starting month? "))
endMonth = int(input("What's your ending month? "))

def months_of_year(startMonth, endMonth):
    months = ["Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
    
    if 0 <= startMonth <= 11 and endMonth <=12:
        return months[startMonth:endMonth]
    else:
        print("How many months do you think there are?")
    print(f"Your months are: {months_of_year(startMonth, endMonth)} ")
months_of_year(startMonth, endMonth)
