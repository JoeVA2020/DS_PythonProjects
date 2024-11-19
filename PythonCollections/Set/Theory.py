from xmlrpc.client import boolean

st={}   #this is empty dictionary, When values are added it becomes a set
print(type(st))

# To create an empty set we need to use set() function
st1=set()
print(st1)

st={15,20,2.2,'bigdata','cow',True,False}
print(st)
# ==> Does not support duplicate values
# ==> Heterogeneous
# ==> Does not preserve insertion order
# ==> set is mutable
