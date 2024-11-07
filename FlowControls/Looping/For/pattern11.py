# for i in range(5):
#     for j in range(6,i,-1):
#         print(j-1,end=' ')
#     print()

for i in range(5):
    for j in range(6-i):
        print(j,end=' ')
    print()

for i in range(5,0,-1):
    for j in range(i+1):
        print(j,end=' ')
    print()

# 0 1 2 3 4 5
# 0 1 2 3 4
# 0 1 2 3
# 0 1 2
# 0 1
