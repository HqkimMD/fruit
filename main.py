from function import display_fruit_price
print("-----------------------------")
print("Fruit that we have TODAY!!!! ")
print("-----------------------------")
print("Orange | Mango | Watermelon")
# print("What type of fruit that you want to buy? =>>")
fruit_type = input("What type of fruit that you want to buy? =>>")
# print("How many kg. to buy? =>>")
weight = float(input("How many kg. to buy? =>>"))

result = display_fruit_price(fruit_type, weight)
print("price is ",result,"฿")
