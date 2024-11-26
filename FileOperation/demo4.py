#
# 1. Dancer proff: fname,lname,age
# 2. age above 50 fname,lname,age,prof
# 3.age range 25 to 40 fname,lname,age,prof
# 4.india work, fname,lname,age,prof
# 5. india work and age above 50 fname,lname,age
# 6. india work and dancer prof fname,lname,age
# 7. pilot prof fname,lname,age
# 8.pilot prof and age above 40 fname,lname,age
# 9. us work fname,lname,age
# 10. uk work and age above 50 fname,lname,age
# 11. Each proff count
# 12 Each location count
# 13 Each age group count

file1=open('C:/Users/joeva/Documents/PY_DS/customer1.txt')
dic={}
for i in file1:
    data=i.rstrip('\n').split(',')
    id=int(data[0])
    fname=data[1]
    lname=data[2]
    age=int(data[3])
    prof=data[4]
    loc=data[-1]

# 1. Dancer proff: fname,lname,age
#     if(prof=='Dancer'):
#         print(fname,lname,age)

# 2. age above 50 fname,lname,age,prof
#     if(age>50):
#         print(fname, lname, age,prof)

# 3.age range 25 to 40 fname,lname,age,prof
#     if(age>25 and age<40):
#         print(fname, lname, age, prof)

# 4.india work, fname,lname,age,prof
#     if(loc=="india"):
#         print(fname, lname, age, prof)

# 5. india work and age above 50 fname,lname,age
#     if (loc == 'india' and age>50):
#         print(fname, lname, age)
#
# # 6. india work and dancer prof fname,lname,age
#     if(loc=='india'and prof=='Dancer'):
#         print(fname, lname, age)
#
# # 7. pilot prof fname,lname,age
#     if(prof=='Pilot'):
#         print(fname,lname,age)
#
# 8.pilot prof and age above 40 fname,lname,age
#     if(prof=='Pilot'and age>40):
#         print(fname,lname,age)
# 9. us work fname,lname,age
#     if(loc=='us'):
#         print(fname,lname,age)

# 10. uk work and age above 50 fname,lname,age
#     if(loc=='us'and age>50):
#         print(fname,lname,age)

# 11. Each proff count
#     if prof not in dic:
#         dic[prof] = 1
#     else:
#         dic[prof] += 1
#print(dic)
# 12 Each location count
    if loc not in dic:
        dic[loc] = 1
    else:
        dic[loc] += 1
print(dic)

# 13 Each age group count
#     if age not in dic:
#         dic[age]=1
#     else:
#         dic[age]+=1
# print(dic)

for k,v in dic.items():
    print(k,",",v)