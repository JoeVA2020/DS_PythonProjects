f=open("Sample1",'r')
writeFile=open("Sample1_copy",'w')
for i in f:
    writeFile.write(i)