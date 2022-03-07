hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#to find the average price of a cut
total_price = 0
#loop through prices_list , add each price to variable
for price in prices:
  total_price += price
#find the average
average_price = total_price / len(prices)
#print the average price!
print("Average Haircut Price: $" + str(average_price))

new_prices = [price - 5 for price in prices]
print(new_prices)

#revenue.
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue: $" +str(total_revenue))
#average daily revenue
average_daily_revenue = total_revenue / 7
print("Average Daily Revenue: $" +str(average_daily_revenue))
# cuts under $30 to attract more customers, conditional list comprehension 
cuts_under_30 = [
  hairstyles[i]
  for i in range(len(hairstyles))
  if new_prices[i] < 30
]
print( "Here are the cuts under $30: " + str(cuts_under_30))


