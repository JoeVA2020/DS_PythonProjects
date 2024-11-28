class Student:
    coll='AEC'
    def setvalue(self,id,fname,lname,age):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
    def printvalue(self):
        print(self.id,self.fname,self.lname,self.age,Student.coll)

person1=Student()
person1.setvalue(1,'joe','v',22,)
person1.printvalue()

person2=Student()
person2.setvalue(2,'ben','simon',32)
person2.printvalue()

person3=Student()
person3.setvalue(3,'ash','james',22)
person3.printvalue()

person4=Student()
person4.setvalue(4,'peter','griffin',29,)
person4.printvalue()

person5=Student()
person5.setvalue(5,'antony','hamlin',21)
person5.printvalue()