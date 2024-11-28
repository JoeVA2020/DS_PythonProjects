# f=open("C:/Users/joeva/Documents/PY_DS/movies_cleaned_pandas.csv",'r')
# dic={}
# count=0
# for i in f:
#     data=i.rstrip('\n').split(',')
#     id=int(data[0])
#     movie=data[1]
#     year=data[2]
#     rating=float(data[3])
#     length=data[-1]

#1. Find row count
#     if id not in dic:
#         count+=1
# print(count)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#4. find maximum rated 5 movies

# for i in f:
#     data = i.rstrip('\n').split(',')
#     dic[data[0]]=float(data[3])
# dic=dict(sorted(dic.items(),key=lambda item: item[1],reverse=True))
# s=0
# lst=[]
# for k,v in dic.items():
#     if s==5:
#         break
#     lst.append(k)
#     s+=1
# f=open("C:/Users/joeva/Documents/PY_DS/movies_cleaned_pandas.csv",'r')
# for i in f:
#     data = i.rstrip('\n').split(',')
#     id=data[0]
#     if id in lst:
#         print(data[1:4])
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``
#5 finding minimum rated 5 movies
# f=open("C:/Users/joeva/Documents/PY_DS/movies_cleaned_pandas.csv",'r')
# dic={}
# for i in f:
#     data = i.rstrip('\n').split(',')
#     dic[data[0]]=float(data[3])
# dic=dict(sorted(dic.items(),key=lambda item: item[1]))
# s=0
# lst=[]
# for k,v in dic.items():
#     if s==3:
#         break
#     lst.append(k)
#     s+=1
# f=open("C:/Users/joeva/Documents/PY_DS/movies_cleaned_pandas.csv",'r')
# for i in f:
#     data = i.rstrip('\n').split(',')
#     id=data[0]
#     if id in lst:
#         print(data[1:4])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#6 Each year movie release count
# f=open("C:/Users/joeva/Documents/PY_DS/movies_cleaned_pandas.csv",'r')
# dic={}
# for i in f:
#     data=i.rstrip('\n').split(',')
#     year=data[2]
#     if year not in dic:
#         dic[year]=1
#     else:
#         dic[year]+=1
# dic=dict(sorted(dic.items(),key=lambda item: item[1],reverse=True))
# for k,v in dic.items():
#     print(k,':',v)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
#7 Each rating count

# f=open("C:/Users/joeva/Documents/PY_DS/movies_cleaned_pandas.csv",'r')
# dic={}
# for i in f:
#     data=i.rstrip('\n').split(',')
#     rating=data[3]
#     if rating not in dic:
#         dic[rating]=1
#     else:
#         dic[rating]+=1
# dic=dict(sorted(dic.items(),key=lambda item: item[1],reverse=True))
# for k,v in dic.items():
#     print(k,':',v)
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 8 Year =  2008 and rating above 3 find row count
# f=open("C:/Users/joeva/Documents/PY_DS/movies_cleaned_pandas.csv",'r')
# dic={}
# count=0
# for i in f:
#     data=i.rstrip('\n').split(',')
#     year=data[2]
#     rating=float(data[3])
#     if year=='2008'and rating > 3:
#         count+=1
# print(count)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#9 Find 1 movie with maximum duration: name year rating duration
# f=open("C:/Users/joeva/Documents/PY_DS/movies_cleaned_pandas.csv",'r')
# dic={}
# for i in f:
#     data = i.rstrip('\n').split(',')
#     dic[data[0]]=float(data[-1])
# dic=dict(sorted(dic.items(),key=lambda item: item[1], reverse=True))
# s=0
# lst=[]
# for k,v in dic.items():
#     if s==1:
#         break
#     lst.append(k)
#     s+=1
# f=open("C:/Users/joeva/Documents/PY_DS/movies_cleaned_pandas.csv",'r')
# for i in f:
#     data = i.rstrip('\n').split(',')
#     id=data[0]
#     if id in lst:
#         print(data[1:5])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# find min rating 1 movie with name year rating duration
# f=open("C:/Users/joeva/Documents/PY_DS/movies_cleaned_pandas.csv",'r')
# dic={}
# for i in f:
#     data = i.rstrip('\n').split(',')
#     dic[data[0]]=float(data[3])
# dic=dict(sorted(dic.items(),key=lambda item: item[1]))
# s=0
# lst=[]
# for k,v in dic.items():
#     if s==1:
#         break
#     lst.append(k)
#     s+=1
# f=open("C:/Users/joeva/Documents/PY_DS/movies_cleaned_pandas.csv",'r')
# for i in f:
#     data = i.rstrip('\n').split(',')
#     id=data[0]
#     if id in lst:
#         print(data[1:5])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 11 Rating year above 4 and release year above 2005

f=open("C:/Users/joeva/Documents/PY_DS/movies_cleaned_pandas.csv",'r')
dic={}
count=0
for i in f:
    data=i.rstrip('\n').split(',')
    year=data[2]
    rating=float(data[3])
    if year>'2005'and rating > 4:
        count+=1
print(count)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
# 12  2008 movie count
f=open("C:/Users/joeva/Documents/PY_DS/movies_cleaned_pandas.csv",'r')
dic={}
count=0
for i in f:
    data=i.rstrip('\n').split(',')
    year=data[2]
    rating=float(data[3])
    if year=='2008':
        count+=1
print(count)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 13 Movies 1975 - 2000 count
f=open("C:/Users/joeva/Documents/PY_DS/movies_cleaned_pandas.csv",'r')
dic={}
count=0
for i in f:
    data=i.rstrip('\n').split(',')
    year=data[2]
    rating=float(data[3])
    if year>='1975'and year <='2000':
        count+=1
print(count)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#14 Movies 1975 - 2000 and rating above 3.5
f=open("C:/Users/joeva/Documents/PY_DS/movies_cleaned_pandas.csv",'r')
dic={}
count=0
for i in f:
    data=i.rstrip('\n').split(',')
    year=data[2]
    rating=float(data[3])
    if year>='1975'and year <='2000'and rating>3.5:
        count+=1
print(count)