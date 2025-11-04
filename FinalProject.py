
print("	---------------------------------------------------------------\n"\
"	                           PRODUCT CATALOG\n"\
"	---------------------------------------------------------------\n"\
"	1      |    USB Drive(128 GB)                        |   $12.00\n"\
"	2      |   Mac Book Pro(15 inch)                     |   $2900.00\n"\
"	3      |   Arduino 1010(with blue tooth)             |   $48.00\n"\
"	4      |   Ring Camera(wireless)                     |   $156.00\n"\
"	5      |   Smart TV(TCL 70 inch)                     |   $359.00\n"\
"	----------------------------------------------------------------")
# Make an individualdictionary object for each product?
usb_drive = {
	"ProductID": 1,
	"SKU": "usb_k981",
	"Price": 12.00,
	"Quantity": 0,
	"Description": "USB 128 GB drive.",
	"Stock": 1000
}
Mac_Book_pro = {
	"ProductID":2,
	"SKU":"mbpro_490",
	"Price":2900.00,
	"Quantity":0,
	"Description":"Mac Book Pro 15 inch",
	"Stock":45
}
Arduino_1010 ={
	"ProductID":3,
	"SKU":"chip_1010"
	"Price":48.00,
	"Quantity":0,
	"Description":"Arduino microprocessor",
	"Stock":325
}
Ring_camera={
	"ProductID":4,
	"SKU":"cam_78",
	"Price":156.00,
	"Quantity":0,
	"Description":"Ring CameraModel 78",
	"Stock":98
}
Smart_TV={
	"ProductID":5,
	"SKU":"smt_tv_100",
	"Price":359.00,
	"Quantity":0,
	"Description":"TCL Smart TV",
	"Stock":225
}

EnteredID = input("Enter the product ID you would like add to your shopping cart!")
Quantity =input(f"Enter quanity for product{eneteredID}: ")
Greedy =input("“Would you like to add another product (y or n)?”)

			  
#example of adding in product quanity
#whatQTY=input("blahblahblah)
#usb["quantity"]=(3)




