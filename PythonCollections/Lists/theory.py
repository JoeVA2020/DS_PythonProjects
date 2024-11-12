# lists
#SYNTAX
variable_name=[]

lst=[]   #empty list

lst1=list() #function

#can input multiple datatypes

lst2=[1,2.7,3,4,'joe','bigData']
print(lst2)

#   LIST supports heterogeneous data
#   Insertion order is reserved ==> i.e data is printed in the same order

lst3=[1,2.50,1234567890741,'luminar',True,False]
print(lst3)



lst4=[10,10,10,20,20,'luminar','luminar',True,True]
print(lst4)

#   Supports duplicate values

#INDEX
lst=[10,20,30,40,50,60,70,80,90]
#    0  1   2  3  4  6 ......n-1
#particular elements
print(lst[4])
print(lst[1])
print(lst[7])
print(lst[-1])


print()
lst[4]=100
print(lst)
print()


lst[0]=1
print(lst)
print()


lst[5]='python'
print(lst)
print()