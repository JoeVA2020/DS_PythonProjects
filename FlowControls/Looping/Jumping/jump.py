#Jumping statements

print("\nbreak")
#break     ==> to exit a loop
for i in range(0,50):
    if(i==25):
        break
    print(i,end=' ')

print("\ncontinue")
#continue  ==> to skip a condition
for i in range(0,50):
    if(i==25):
        continue
    print(i,end=' ')

#pass      ==> Do nothing
print('\npass')
for i in range(0,50):
    if (i==25):
        pass
    print(i,end=' ')

print()