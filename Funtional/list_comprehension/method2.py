
#Method_2 : Range of elements added to a list based on one condition

# SYNTAX==> var=[print range if condition ]
# 1 to 50 even numbers
# lst=[i for i in range(1,51) if i%2==0]
# print(lst)

# 1 to 30 divisble by 5
# lst=[i for i in range(1,31) if i%5==0]
# print(lst)

# 1 to 25 range odd square
# lst=[i**2 for i in range(1,26) if i%2!=0]
# print(lst)

# lst=[(i,i**2) for i in range(1,26) if i%2!=0]
# print(lst)

# 1 to 50 range divisible by 2 and 5
lst=[i for i in range(1,51) if (i%5==0)and(i%2==0)]
print(lst)
