words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
lst=[]
for i in words:
    if (len(i)>3 and 'e' in i):
        lst.append(len(i))
print(lst)
square=list(map(lambda num:num**2,lst))
print('Squared:',square)
filtered=list(filter(lambda num:num%2==0,lst))
print('Filtered',filtered)
final=list(filter(lambda num:num%2==0,square))
print('Final',final)