for i in range(-2,-5,-1):
    print(i,end=',')

#ANSWER
#  -2,-3,-4


print()
for l in 'jhon':
    if l=='0':
        pass
    print(l,end=',')
#ANSWER
#j,h,o,n,


print()
for i in range(2,2):
    if(i%2==0):
        print('Hello')
    else:
        print('luminar')
else:
    print('hai')
#ANSWER
#hai
#REASON ==> In for loop i does not reach the upper limit. So i does not have a value . Therefore for loop does not work


print()
x=0
for i in range(10):
    for j in range(-1,-10,-1):
        x+=1
print(x)
#ANSWER ==> 90

print()

a,b=12,5
if a+b:
    print('hello\n')
else:
    print('hai\n')
#ANSWER ==> hello  Since the value of if condition is not ZERO. the if condition will work as long as value of if condition is non-zero



