num=int(input('Enter number'))
prime=0
if(num>1):
    for i in range(2,num):
        if(num%i==0):
            prime=1
    if(prime==0):
        print(num,"is prime")
    else:
        print(num,"not prime")
else:
    print("not prime")
