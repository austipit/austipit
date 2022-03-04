#Furniture Store
inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

#Length tells how many items
inventory_len = len(inventory)
#Saving the first element to first
first = inventory[0]
#Saving the last element to last
last = inventory[-1]
#Saving items 2 - 6 to a variable
inventory_2_6 = inventory[2:6]
#Save the first 3 items to variable
first_3 = inventory[0:3]
#Saving how many twin beds there are to a variable
twin_beds = inventory.count("twin bed")
#Remove the 5th element , save to variable
removed_item = inventory.pop(4)
#Insert a new item at the 10th index
inventory.insert(10, "19th Century Bed Frame")
#Sort the list 
inventory.sort()
print(inventory)
