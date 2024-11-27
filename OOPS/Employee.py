class Person:
    def setvalue(self,fname,lname,age,loc):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.loc=loc
    def printvalue(self):
        print(self.fname,self.lname,self.age,self.loc)

person1=Person()
person1.setvalue('joe','V',22,'TVM')
person1.printvalue()

person2=Person()
person2.setvalue('Rishi','K',35,'EKM')
person2.printvalue()