lst=[12,2,5,20,5,2,14,15,60,5,12]
new_lst=[]
print(lst)
sorted_lst=sorted(lst)
print("Sorted list:",sorted(lst))
smallest=min(sorted_lst)
for i in sorted_lst:
    if i != smallest and i%2==0:
        second_smallest=i
        break
print("second_smallest :",second_smallest)
for i in lst:
    if(i!=second_smallest):
        new_lst.append(i)
print("New list:",new_lst)
print("Sum of New list:",sum(new_lst))
print("New sorted list:",sorted(new_lst))

