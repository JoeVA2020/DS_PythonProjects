totalClass=int(input("Total number of classes held: "))
attendClass=int(input("Number of classes attended: "))
attendance=(attendClass/totalClass)*100
print("Attendace is :",attendance,"%")
if(attendance>=75):
    print("Allowed to attend exam")
else:
    print("Not allowed to attend")
