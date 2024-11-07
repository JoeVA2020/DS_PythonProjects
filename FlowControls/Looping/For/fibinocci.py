Num=int(input('Enter number: '))
num1=0
num2=1
sum=0
for i in range(Num):
    print(sum,end=' ')
    num1 = num2
    num2 = sum
    sum=num1+num2


