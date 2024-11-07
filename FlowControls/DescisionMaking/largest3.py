# Read 3 numbers from users and find 2nd largest number

Num1=int(input("Enter Number 1 : "))
Num2=int(input("Enter Number 2 : "))
Num3=int(input("Enter Number 3 : "))

# if((Num1>Num2)&(Num1<Num3)|(Num1<Num2)&(Num1>Num3)):
#     print(Num1,"is second Largest")
# elif((Num2>Num1)&(Num2<Num3)|(Num2<Num1)&(Num2>Num3)):
#     print(Num2, "is second Largest")
# else:
#     print(Num3, "is second Largest")

#    ALTERNATIVE USING NESTED IF

if(Num1>Num2)&(Num1>Num3):
    if(Num2>Num3):
        print(Num2, "is second Largest")
    else:
        print(Num3, "is second Largest")
elif(Num2>Num1)&(Num2>Num3):
    if(Num1>Num3):
        print(Num1, "is second Largest")
    else:
        print(Num3, "is second Largest")
elif(Num3>Num1)&(Num3>Num2):
    if(Num1>Num2):
        print(Num1, "is second Largest")
    else:
        print(Num2, "is second Largest")
