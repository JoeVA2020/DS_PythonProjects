pattern='ABDFGBASDFGBNC'
dic={}
for i in pattern:
    if i not in dic:
        dic[i]=1
    else:
        print(i,"is first recursive character")
        break