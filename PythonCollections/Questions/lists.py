# lst=[15,20,25,30,35,40,50]
# print(lst[-2]+lst[-0]+lst[1])
#Ans: 75  Negetive 0 is 0

#Convert lst=[15,3,10,6,9,7] to [35, 47, 40, 44, 41, 43]
lst=[15,3,10,6,9,7]
lst_sum=sum(lst)
lst2=[]
for i in lst:
    lst2.append(lst_sum-i)
print(lst2)