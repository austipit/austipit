#store name
lovely_loveseat_description = ("Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.")

#loveseat price
lovely_loveseat_price = 254.00

#more inventory, and prices
stylish_settee_description = ("Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.")
stylish_settee_price = 180.50
luxurious_lamp_description = ("Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.")
luxurious_lamp_price = 52.15

#sales tax
sales_tax = .088

# first customer
customer_one_total = 0.0

#description of purchase, itemization
customer_one_itemization = ""

# c1 purchasing lovely loveseat at 254
customer_one_total += lovely_loveseat_price

#adding description of loveseat to itemization
customer_one_itemization += lovely_loveseat_description

# also adding luxuriouslamp to c1
customer_one_total += luxurious_lamp_price

#adding description of luxlamp to itemization
customer_one_itemization += luxurious_lamp_description

#calculate sales tax
customer_one_tax = customer_one_total * sales_tax

#add sales tax to customer's total
customer_one_total += customer_one_tax

print("Customer One Items")
print(customer_one_itemization)
print("\n")

print("Customer One Total:")
print(customer_one_total)

