f=open('Fruits','r')
w=open('Fruits_copy','w')
for i in f:
    if i !='apple\n':
        w.write(i)
