# Created by Graeme Barbbe
# Edited by Van Nguyen
# Created on May 05 2022

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
total = size_price + toppings * 0.50
price_with_delivery = total + delivery_cost
price_HST = price_with_delivery * HST
price_with_delivery = price_with_delivery + price_HST
total_HST = total * HST
total = total + total_HST


if (size == "SMALL") or (size == "MEDIUM") or (size == "LARGE"):
	if (toppings >= 0) and (toppings <= 6):
		if (delivery == "YES") or (delivery == "NO"):
			if delivery == "YES":
				print("The total is $" + str(round(price_with_delivery, 2)))
			else:
				print("The total is $" + str(round(total, 2)))
		else: 
			print("Please enter either yes or no for if you need delivery")
	else:
		print("Please choose a valid number of toppings. We have 6 diffrent choices.")
else: 
	print("Please enter a real size. The options are small, medium or large")