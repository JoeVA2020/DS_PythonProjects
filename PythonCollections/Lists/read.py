# linear search algorithm

lst=[10,15,11,12,17,20,22,25,36,16,1,32,40]
element=int(input("Enter element: "))
flag=0
for i in lst:
    if i==element:
        print("element found")
        flag=1
        break
if flag==0:
    print("Element not found")

#````````````````````````````````````````````````````````

if element in lst:
    print(" found")
else:
    print("Not found")