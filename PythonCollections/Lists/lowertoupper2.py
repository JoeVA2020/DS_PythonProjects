lst=[]
lower=int(input("enter lower limit: "))
upper=int(input("Enter upper limit: "))

for i in range(lower,upper+1):
    if(i%2==0):
        lst.append(i)
print(lst)