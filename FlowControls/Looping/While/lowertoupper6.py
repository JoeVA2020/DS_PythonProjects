lower=int(input("lower limit:"))
upper=int(input("upper limit : "))
sum=0
while(lower<=upper):
    if(lower%2!=0):
        sum+=lower
    lower+=1
print(sum)