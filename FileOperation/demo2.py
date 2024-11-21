f=open('DemoData','r')
dic={}
for i in f:
    word=i.rstrip('\n').rstrip(',').split(' ')
    for j in word:
        if j not in dic:
            dic[j]=1
        else:
            dic[j]+=1
sorted(dic)
print(dic)
