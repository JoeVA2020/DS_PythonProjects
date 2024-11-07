salary=int(input("Enter salary "))
service=int(input('Enter years of expericence '))

if(service>=5):
    bonus=(salary*5)/100
    print("Net bonus :",bonus)
else:
    print("No Bonus available")