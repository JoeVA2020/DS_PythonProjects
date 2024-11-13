lst=[15,11,5,6]
print(lst)
#append  : Function To add a new element to the list
#        : Can only add one element at a time

lst.append(20)
print(lst)

lst.append(25)
print(lst)

lst.append(30)
print(lst)

#extend : to add multiple elements togetther

lst.extend([12,13,45,67])
print(lst)

print()
print()
#insert() : To insert a element at certain location

lst=[1,2,3,4]
print(lst)
lst.insert(1,10)
print(lst)
lst.insert(2,'bigdata')
print(lst)