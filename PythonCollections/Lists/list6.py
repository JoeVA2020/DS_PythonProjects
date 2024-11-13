from audioop import reverse

lst=[1,6,9,2,3,10,15,20,11,23,13,4,2]

#sort()
#   To sort in either ascending or descending order

lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)