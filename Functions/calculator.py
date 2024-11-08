def add(num1,num2):
    sum=num1+num2
    print(sum)
def sub(num1,num2):
    sum=num1-num2
    print(sum)
def mul(num1,num2):
    sum=num1*num2
    print(sum)
def div(num1,num2):
    sum=num1/num2
    print(sum)

def numbers():
     num1 = int(input("Enter number 1: "))
     num2 = int(input("Enter number 2: "))
     return num1,num2


print(" 1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
choice=int(input("Enter Choice : "))
if choice==1:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    add(num1,num2)
elif choice==2:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    sub(num1, num2)
elif choice==3:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    mul(num1, num2)
elif choice==4:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    div(num1, num2)
else:
    print("Choose Valid option")