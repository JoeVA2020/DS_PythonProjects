lower=int(input("Enter lower limit: "))
upper=int(input("Enter upper limit: "))
Sum=0
for i in range(lower,upper+1):
    if(i%2==0):
        Sum+=i
print(Sum)