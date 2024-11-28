class Empoyee:
    prof="Engineer"
    company_name='Liminar Tecnolabs'
    def setvalue(self,id,fname,lname,age):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
    def printvalue(self):
        print(self.id,self.fname,self.lname,self.age,Empoyee.prof,Empoyee.company_name)

emp1=Empoyee()
emp1.setvalue(102,'john','cox',28)
emp1.printvalue()

emp2=Empoyee()
emp2.setvalue(103,'john','doe',22)
emp2.printvalue()

emp3=Empoyee()
emp3.setvalue(103,'homer','simpson',24)
emp3.printvalue()

emp4=Empoyee()
emp4.setvalue(104,'tom','michel',35)
emp4.printvalue()

emp5=Empoyee()
emp5.setvalue(105,'lace','p',20)
emp5.printvalue()



