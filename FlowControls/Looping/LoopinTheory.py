#Looping is used to repeat a condition to until it is fulfilled
from turtledemo.penrose import start

LOOPS
            while
            for

#basic syntax
# 1. Initialization
# 2, Condition
# 3, increment or decrement

while(condition):
    stamement

for i in range(start,end):
    statement

#Works from start to n-1

for i in range(start,stop,step):
    statement

#Nested for loop
    for i in range(1,5):
        for j in range(1, 5):
            print(j, end=" ")
        print()
# i= rows
# j= column
