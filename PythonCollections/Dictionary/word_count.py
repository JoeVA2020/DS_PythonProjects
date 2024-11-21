#word count problem

# checks how many times a word is repeated in a sentence

#   cat bat rat bat rat cat cat bat bat rat
#   cat=3
#   bat=4
#   rat=3

line='cat bat rat bat rat cat cat bat bat rat mat bat pat'
data=line.split(' ')
dic={}
for i in data:
    if i not in dic:
        dic[i]=1
    elif i in dic:
        dic[i]+=1
for i in dic:
    print(i,":",dic[i])