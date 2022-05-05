import math

size = input("What size: ")
toppings = int(input("Enter amount of toppings: "))
delivery = input("Do you need delivery: ")
size = size.upper()
delivery = delivery.upper()

if size == "SMALL":
	size_price = 5
elif size == "MEDIUM":
	size_price = 10
else:
	size_price = 15

HST = 0.13
delivery_cost = 11
price_delivery = (size_price + (toppings * 0.67) + delivery_cost) * 0.13
price_no_delivery = (size_price + (toppings * 0.67)) * 0.13

if (size == "SMALL") or (size == "MEDIUM") or (size == "LARGE"):
	if (toppings >= 0) and (toppings <= 6):
		if delivery == "YES":
			print("The total is", price_delivery)
		else:
			print("The total is", price_no_delivery)
	else:
		print("Please choose a valid number of toppings. We have 6 diffrent choices.")
else: 
	print("Please enter a real size. The options are small, medium or large")