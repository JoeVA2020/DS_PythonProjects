#Create a function called biggest_odd that takes a string of numbers and returns the biggest odd number in the list.
# For example, if you pass '23569' as an argument, your function should return 9. Use list comprehension..

num=235692
data=[]
for i in str(num):
    data.append(i)
data.sort()
i=-1
while data[i]%2!=0:
    i-=1
print(data[i])