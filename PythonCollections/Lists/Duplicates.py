lst=[1,4,5,5,5,10,40,40,30,5,6,13,25,50]
lst1=[]
for i in lst:
    if i not in lst1:
        lst1.append(i)
print(lst1)