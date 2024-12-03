#Method_3 : Range of elements added to a list based on more than one condition

#SYNTAx == var=[print1 if condition else print2 range]
#           var=[print1 if condition else print2 if condition2 else print3 range]
# can not use elif
# 1 to 50 range even square, odd cube

# lst=(i**2 if i%2==0 else i**3 for i in range(1,51))
# print(lst)

 # 1 to 30 if even even if odd print odd
# lst=[(i,'even') if i%2==0 else (i,'odd') for i in range(1,51)]
# print(lst)

# 1 to 50
# 1 to 15 small
# 16 to 35 medium
# 36 to 50 large

lst=[(i,'small') if 0<=i<=15 else (i,'medium') if 16<=i<=35 else (i,'large')for i in range(1,51)]
print(lst)