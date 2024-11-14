# Binary search
#
# STEPS
#
# 1.Sort given list
# 2.Find the lower and upper limit of the list ==> lower=0        upper=len(list)-1
# 3.Find midpoint of list ==> (upper+lower)//2
# 4. Check 3 conditions
#         A. if search>list[mid]
#                 lower=mid+1
#         B. if search<list[mid]
#                 upper=mid-1
#         C. search==list[mid]
#                 element found

#             END SEARCH
lst=[1,6,5,6,13,20,11,13,25,30,100]
lst.sort()
lower=0
upper=len(lst)-1

search=int(input("Enter search element: "))
flag=0
while(lower<=upper):
    mid=(upper+lower)//2
    if(search>lst[mid]):
        lower=mid+1
    elif(search<lst[mid]):
        upper=mid-1
    elif(search==lst[mid]):
        flag=1
        break

if(flag>0):
    print("Element found")
else:
    print("Element not found")