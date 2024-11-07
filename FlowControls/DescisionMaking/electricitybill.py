# user enter amount of units
# CONDITIONS
# for first 100 units : free
# 101 to 200 : Rs 5 per unit
# Above 200 : Rs 10 per unit

units=int(input("Enter Units: "))
if(units<=100):
    cost=0
    print("No Payment")
elif(101<=units<=200):
    cost=(units-100)*5
else:
    cost=((units-200)*10)+500
print("Amount is Rs",cost)

