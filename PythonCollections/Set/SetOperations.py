#   Set Operations

#1. Union
#2. Intersection
#3. Difference

st1={1,2,3,4,5,6,7,8,9,10}
st2={10,11,12,13,14,15,2,4,5,6,7}

st3=st1.union(st2)
print(st3)

st3=st1.intersection(st2)
print(st3)

st3=st1.difference(st2)
print(st3)
st3=st2.difference(st1)
print(st3)