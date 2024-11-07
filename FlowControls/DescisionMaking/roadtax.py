# #calculate road tax
# #read price from user
# if> 1lakh put 15 % as tax
# betwm 1L and 50000 10%
# below 50000 : 5%tax

price=int(input("Enter BIKE COST : "))

if(price>100000):
    tax=(price*15)/100
elif(50000<=price<=100000):
    tax = (price * 10) / 100
else:
    tax = (price * 5) / 100
print("Tax amount is :", tax)