#METHOD 1

def factorial1():
    num=int(input("Enter number : "))
    fact=1
    for i in range(1,num+1):
        fact*=i
    print(fact)

factorial1()
factorial1()

#METHOD 2
def factorial2(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    print(fact)

num=int(input("Enter NUmber 2: "))
factorial2(num)

#METHOD3
def factorial3(num2):
    fact = 1
    for i in range(1, num2 + 1):
        fact *= i
    print(fact)


num2=int(input("Enter number3: "))
data=factorial3(num2)