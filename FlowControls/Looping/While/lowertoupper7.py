lower=int(input("lower limit:"))
upper=int(input("upper limit : "))
odd_sum=0
even_sum=0
while(lower<=upper):
    if(lower%2==0):
        even_sum+=lower
    else:
        odd_sum+=lower
    lower+=1
print("Sum of even numbers:",even_sum)
print("Sum of odd numbers:",odd_sum)