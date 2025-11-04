
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
	"Description":"Mac Book Pro 15 inch
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

whichID = input("Enter the product ID you would like add to your shopping cart!")

ProductAttributes={
  "1", "usb_k981",	"$12.00", " ",	"USB 128 GB drive", "1000",
  "2",	"mbpro_490",	"$2900.00",	" ",	"Mac Book Pro 15 inch",	"45",
  "3",	"chip_1010",	"$48.00", " ", "Arduino microprocessor",	"325",
  "4",	"cam_78",	"$156.00"	 " ",	"Ring Camera Model 78",	"98",
  "5",	"smt_tv_100",	"$359.00",	" ",	"TCL Smart TV.", 	"225",
}
headersA = ["Product ID", "SKU", "Price", "QTY", "Description", "Qty on Hand"]

#example of adding in product quanity
#whatQTY=input("blahblahblah)
#usb["quantity"]=(3)


