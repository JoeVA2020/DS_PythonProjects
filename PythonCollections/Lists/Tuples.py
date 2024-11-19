#   TUPLES

tu=()   #empty tuple
tu1=tuple()     #empty tuple

#two methods to create tuples
# 1 using variable name and using ()
# 2 using variable name and tuple() function

# tu=(10,20,2.5,'bigdata','python',True,False)
# print(tu)
#   OUTPUT (10, 20, 2.5, 'bigdata', 'python', True, False)  ==> Support Heterogeneous data

# tu=(10,20,2.5,20,'bigdata','python','bigdata',True,False)
# print(tu)
# OUTPUT (10, 20, 2.5, 20, 'bigdata', 'python', 'bigdata', True, False) ==> Support duplicate data


# ==> insertion order is preserved
#
# ==> Tuple is immutable

tu=(10,15,20,25,30,35,40,45)
lst=list(tu)
lst[2]=55
tu=tuple(lst)
print(tu)
