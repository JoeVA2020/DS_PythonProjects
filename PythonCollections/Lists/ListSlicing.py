lst=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(lst[3:7]) #   [3, 4, 5, 6]
print(lst[5:])  #   [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] From index till end
print(lst[:6])  #   [0, 1, 2, 3, 4, 5]  from 0 to index
print(lst[:])   #   prints full list

print(lst[2:8:3])       #slicing==> start: Stop: Step
                        #index=2,5
print(lst[1:8:2])       #index=1,3,5,7
print(lst[3::2])        #index=3,5,7,9,11,13,15
print(lst[:9:3])        #index=0,3,6
print(lst[::2])         #index=0,2,4,6,8,10,12,14

#   negetive indexing
# using negetive index numbers to start from tha back of the list
print(lst[-1])