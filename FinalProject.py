print("---------------------------------------------------------------\n"\
"	                           PRODUCT CATALOG\n"\
"	---------------------------------------------------------------\n"\
"	1      |    USB Drive(128 GB)                        |   $12.00\n"\
"	2      |   Mac Book Pro(15 inch)                     |   $2900.00\n"\
"	3      |   Arduino 1010(with blue tooth)             |   $48.00\n"\
"	4      |   Ring Camera(wireless)                     |   $156.00\n"\
"	5      |   Smart TV(TCL 70 inch)                     |   $359.00\n"\
"	----------------------------------------------------------------")
# Make an individualdictionary object for each product?

products = {
	"1" : {
		"ProductID": 1,
		"SKU": "usb_k981",
		"Price": 12.00,
		"Quantity": 0,
		"Description": "USB 128 GB drive.",
		"Stock": 1000
	},
	"2": {
		"ProductID":2,
		"SKU":"mbpro_490",
		"Price":2900.00,
		"Quantity":0,
		"Description":"Mac Book Pro 15 inch",
		"Stock":45
	},
	"3" : {
		"ProductID":3,
		"SKU":"chip_1010",
		"Price":48.00,
		"Quantity":0,
		"Description":"Arduino microprocessor",
		"Stock":325
	},
	"4": {
		"ProductID":4,
		"SKU":"cam_78",
		"Price":156.00,
		"Quantity":0,
		"Description":"Ring CameraModel 78",
		"Stock":98
	},
	"5": {
		"ProductID":5,
		"SKU":"smt_tv_100",
		"Price":359.00,
		"Quantity":0,
		"Description":"TCL Smart TV",
		"Stock":225
	}
}
quantity_limits={
		1:5,
		2:3,
		3:10,
		4:4,
		5:2
	}
	
boughtItems={}
def AddtoCart():
	enteredID = input("Enter the product ID you would like add to your shopping cart!: ")
	Quantity =input(f"Enter quantity for product {enteredID}: ")
	if enteredID in boughtItems:
		boughtItems[enteredID] = int(Quantity) 

	limit = quantity_limits.get(enteredID, None)
	if limit and Quantity > limit:
		print(f"You can't purchase more than {limit} of {enteredID}")
		quantity = limit
	if enteredID in boughtItems:
		print(f"{enteredID} is already in your cart! {boughtItems[enteredID]}")
	
	boughtItems.update({enteredID:{"Quantity": Quantity}})

	Greedy =input("Would you like to add another product? (y/n): ")
	if Greedy == "n" :
		checkout= input("Are you ready to check out? (y/n): ")
		if checkout == "y" :				
			Checkout()
	if Greedy == "y":
		AddtoCart()

total = 0.0
for productID, Quantity in boughtItems.items():
	product = product[productID]
	itemPrices=product['Price']
	math= product['Price'] * Quantity
	total+=math


def validateCreditCard(ccNum):
	Expiration = input("Enter the expiration date on your card:")
	CVV = input("Please enter your CVV: ")
	odd_digits = 0
	even_digits = 0
	ccNum = ccNum[::-1]

	for x in ccNum[::2]:
	     	odd_digits += int(x)
			 		 
	for x in ccNum[1::2]:
		x = int(x) * 2
		if x >= 10:
			even_digits += (1 + (x % 10))
		else:
	    		even_digits += x
	total = odd_digits + even_digits

	if total % 10 == 0:
		print(f"The credit card number {ccNum[::-1]} is valid!")
	else:
		print(f"Invalid credit card number {ccNum[::-1]} entered. Please try again.")


def Checkout():
	print("---------------------------------------------------------------\n"\
	"	                      CHECKOUT PAGE\n"\
	"---------------------------------------------------------------\n")
	firstName =input("Enter your First Name: ")
	lastName =input("Enter your Last Name: ")
	address=input("Enter your address: ")
	city=input("Enter your city: ") 
	state=input("Enter your state: ")
	zipCode=input("Enter your Zipcode: ")
	email=input("Enter your Email: ")
	phone=input("Enter your Phone number: ")
	ccNum =input("Enter your credit card number (no spaces): ")
	validateCreditCard(ccNum)

	print("--------------------------------------------------------------\n"\
	"		   	Billing/Shipping Information\n"\
	"---------------------------------------------------------------------")
	print(firstName)
	print(lastName)
	print(address)
	print(city)
	print(state)
	print(zipCode)
	print(email)
	print(phone)
	print("-----------------------------------------------------------------\n"\
	"                          Shopping Cart Information\n"\
	"-----------------------------------------------------------------------------\n"\
	" ------------------------------------------------------------------------------\n"\
	" ******************************************************************************\n"\
	"  SKU~~~~~~~~~~~~~~~Qty~~~~~~~~~~~~Price~~~~~~~~Description~~~~~~~~~~~~~Total\n")
	for productID, item_data in boughtItems.items():
		product = products[productID]
		sku = product['SKU']
		qty = item_data['Quantity']
		price = product['Price']
		description = product['Description']
		cost_total = float(price) * int(qty)
		print(f"{sku}~~~~~~~~~{qty}~~~~~~~~~${price}~~~~~{description}~~~~~~~~~${cost_total:.2f}")
if __name__ == "__main__":
	AddtoCart()