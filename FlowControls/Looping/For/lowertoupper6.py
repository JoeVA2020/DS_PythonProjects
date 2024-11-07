lower=int(input("Enter lower limit: "))
upper=int(input("Enter upper limit: "))
Sum_odd=0
Sum_even=0
for i in range(lower,upper+1):
    if(i%2==0):
        Sum_even+=i
    else:Sum_odd+=i
print("Even Sum =",Sum_even)
print("Odd Sum =",Sum_odd)