#Global Freight Calculator
#inputs

sender = input("Please Input Your Name:")
type_of_item = input("Type Item Name:")
isFragile = input("Is the item Fragile? (T/F) : ")
isRush = input("Is the item Rush? (T/F) : ")
weight = float(input("Enter Weight in kg : "))
distance = float(input("Enter Distance in km : "))
is_express = input("Is the shipment via Express? (T/F) : ")
is_international = input("Is the shipment via International? (T/F) : ")

#Base Cost

base_cost = (weight * 2.50) + (distance * 0.15)	

#Pricing Tiers

if weight <= 2.0 and distance <= 100 and not is_express and not is_international:
    total = 0.00

elif is_international and is_express:
    total = (base_cost * 1.40) + 50

elif is_express or (is_international and weight > 20):
    total = (base_cost * 1.20) + 25

elif weight > 30 or distance > 1000:
    total = base_cost + 30

else:
    total = base_cost


print("========== SHIPPING COST ==========")
print("Sender Name:", sender)
print("Item Name:", type_of_item)
print("Item weight:", weight)
print("Base Cost:", base_cost)
print("TOTAL COST: $", total)


