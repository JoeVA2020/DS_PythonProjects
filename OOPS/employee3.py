

class Person:
    def presonal_data(self,fname,lname,age,loc):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.loc=loc

class Employee(Person):
    def professional_data(self,id,prof,exp,salary):
        self.id=id
        self.prof=prof
        self.exp=exp
        self.salary=salary
    def print_data(self):
        print(self.id,self.fname,self.lname,self.age,self.prof,self.salary,self.exp,self.loc)

emp1=Employee()
emp1.professional_data(214236,'job',2,21000)
emp1.presonal_data('joe','v',22,'tvm')
emp1.print_data()