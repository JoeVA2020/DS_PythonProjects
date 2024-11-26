file=open('C:/Users/joeva\Documents/PY_DS/temper.unknown')
dic={}
for i in file:
    data=i.rstrip('\n').split(',')
    district=data[0]
    temp=data[1]
    if district not in dic:
        dic[district]=temp
    else:
        if temp > dic[district]:
            dic[district]=temp

for k,v in dic.items():
    print(k,",",v)
