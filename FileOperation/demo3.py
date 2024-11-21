file1=open('C:/Users/joeva/Documents/PY_DS/sample4.txt')
# for i in file1:
#     print(i)

# age above 23 fname,lname,age,phn
#chennai work fname,lname,age
#age above 23 & loc chennai fname,lname,age



# for i in file1:
#     data=i.rstrip('\n').split(',')
#     age=int(data[3])
#     if age>23:
#         print(data[1:5])

# print("chennai work fname,lname,age\n")
# for i in file1:
#     data=i.rstrip('\n').split(',')
#     loc=data[5]
#     if loc=='Chennai':
#         print(data[1:5])

print("age above 23 & chennai work fname,lname,age\n")
for j in file1:
    data=j.rstrip('\n').split(',')
    age=int(data[3])
    loc=data[5]
    if loc=='Chennai'and age>23:
         print(data[1:4])