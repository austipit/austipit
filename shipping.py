weight = 41.5
#Ground Shipping, price per pound changes by weight
if weight <= 2.0:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3.00 + 20
elif weight <= 10:
  cost_ground = weight * 4.00 + 20
else:
  cost_ground = weight * 4.75 + 20

print("Ground Shipping: $", cost_ground )

#Ground Shipping Premium, flat rate
cost_premium = 125.00
print("For premium ground shipping, it will be a flat rate of $",cost_premium)

#Drone Shipping, price per pound changes by weight
if weight <= 2.0:
  cost_drone = weight * 4.50 
elif weight <= 6.0:
  cost_drone = weight * 9.00
elif weight <= 10.00:
  cost_drone = weight * 12.00
else:
  cost_drone = weight * 14.25
print("For drone shipping, it will cost approximately $", cost_drone)
