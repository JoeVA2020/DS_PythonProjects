#dictionary
from Functions.import_keyword import data2

dic={}

#key-value pair
#Key is a identifier and each key has a value

#id:101
#fname:vinay
#lname:k
#age:28
#prof:bigdata

dic={'id':101,'fname':'vinay','lname':'k','age':28,'prof':'bigdata'}
print(dic)

dic1={'id':101,'fname':'vinay','age':28.5,'prof':True}
print(dic1)

#supports heterogeneous data
#preserves insertion order
# duplicate key not supported
# duplicate value are supported
# mutable

#Key    is used insted of index to find the value
# print(dic1['fname'])
# print(dic1['id'])

# for i in dic1:
#     print(i,":",dic1[i])

# dic1['age']=40
# dic1['fname']='Moe'
# print(dic1)
# dic1['age']+=4
# print(dic1)

# how to add new key value pair
dic1['marks']=50
print(dic1)


# We can also apply in & not in dictionary

print('fname' in dic1)      # True
print('slary' in dic1)      #false
print('fname' not in dic1)  #false

#delete key from dictionary

del dic1['id']
print(dic1)