# Your code below:
#pizza toppings
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
#prices of toppings
prices = [2, 6 ,1, 3, 2, 7 , 2]
#number of times 2 appears
num_two_dollar_slices = prices.count(2)
#Length of toppings list 
num_pizzas = len(toppings)
#string
print("We sell " + str(num_pizzas) + " different kinds of pizza!")
#two dimensional list
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
#blank space
print("\n")
#print(pizza_and_prices)
#sort price
pizza_and_prices.sort()
print(pizza_and_prices)
#store first element
cheapest_pizza = pizza_and_prices[0]
#print(cheapest_pizza)
priciest_pizza = pizza_and_prices[-1]
#print(priciest_pizza)
pizza_and_prices.pop()
#print(pizza_and_prices)
#add new item at index, 
print("\n")
pizza_and_prices.insert(4, [2.5, "peppers"])
print(pizza_and_prices)
#slice 3 cheapest pizzas 
three_cheapest = pizza_and_prices[:3]
print("\n")
print("Three cheapest pizzas " + str(three_cheapest))



