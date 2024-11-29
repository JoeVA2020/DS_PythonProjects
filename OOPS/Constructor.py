class Person:
    def __init__(self,fname,lname,age,loc):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.loc=loc
    def printvalue(self):
        print(self.fname,self.lname,self.age,self.loc)


person1=Person('joe','v',22,'tvm')
person1.printvalue()

person2=Person('ben','simon',32,'ekm')
person2.printvalue()

