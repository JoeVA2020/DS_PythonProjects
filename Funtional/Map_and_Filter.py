#map

#filter


#map ==>

#[1,2,3,4,5,6,7,8,9,10] ==> [1,4,9,16,25,...,100]

# Used to apply functions to elements in a list
# SYNTAX ==> variable_name=list(map(function,iterable))

#filter

# used to filter out elements from a list using certain conditions
 #[1,2,3,4,5,6,7,8,9,10] ==> [2,4,6,8,10]
# SYNTAX ==> list(filter(function,iterable))

lst1=[1,2,3,4,5,6,7,8,9,10]

# f=map(square,lst)
# print(f)

# f=list(map(lambda num:num**2,lst))
# print(f)

# f=list(map(lambda num:num**3,lst1))
# print(f)

# f=list(filter(lambda num:num%2==0,lst1))
# print(f)

f=list(filter(lambda num:num%2!=0,lst1))
m=list(map(lambda num:num**2,f))
print(m)