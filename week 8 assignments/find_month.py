def search(month):
  month = ["Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
  search =input("What's your month?")

if search in month:
  print(f"we found {search} was found in the months list. Search Successful!")
else:
  print("We could not find {search} in months list.")
