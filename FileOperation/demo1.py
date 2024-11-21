# f=open('C:/Users/joeva/PycharmProjects/OCT_pythonProject_1/Identifiers/demo')
f=open('DemoData','r')
lst=[]
for i in f:
    lst.append(int(i.rstrip('\n')))
print(lst)
print(sum(lst))

#rstrip : to cut certian elemints in a data from right side
#lstrip : to cut certian elemints in a data from left side

# data='hello/n'
# #data1=data.rstrip('/n') #prints hello
# #data1=data.rstrip('l/n') #prints hello
# data1=data.rstrip('lo/n') #prints he
# print(data1)