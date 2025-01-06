
perfect_lst=[]
for i in range(1,10000):
    input_num=i
    perfect_sum=0
    for j in range(1,input_num):
        if(input_num % j == 0):
            perfect_sum=perfect_sum+j
    if(perfect_sum==input_num):
        perfect_lst.append(input_num)
print("perfect numbers in the range from 1 to10000 :",perfect_lst)
print('SUM of perfect numbers :',sum(perfect_lst))
avg=sum(perfect_lst)/len(perfect_lst)
print('AVG of perfect numbers :',avg)
print('Smallest of perfect numbers :',min(perfect_lst))
print('Largest of perfect numbers :',max(perfect_lst))