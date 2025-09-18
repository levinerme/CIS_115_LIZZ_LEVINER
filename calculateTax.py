Taxes =float(7.25)
item =float(75.34)

math = float(75.34 * 0.0725)
TotalCost = 75.43 + math
rounded = round(TotalCost)

 
print(f"Your sales tax is {Taxes} percentage, the price of the item is {item} dollars.")
print(f"The total is {rounded} dollars.")