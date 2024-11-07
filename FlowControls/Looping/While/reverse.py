Num=int(input("Enter Number: "))
rev_num=0
while(Num>0):
    rev=Num%10
    rev_num=rev_num*10+rev
    Num=Num//10
print(rev_num)