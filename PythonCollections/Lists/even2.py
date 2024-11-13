lst=[]
even=[]
odd=[]

for i in range(1,100+1):
    lst.append(i)
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)

print(lst)
print(even)
print(odd)
print("SUMS")
print(sum(lst))
print(sum(even))
print(sum(odd))