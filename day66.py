class Employee:
    companyName = "Om Buildcon" #class variable meh define kiya hai isliye by default sabme yeh aayega kyuki yeh common wale hai isliye yaha define kiya hai
    noofemployee = 0
    def __init__(self, name):
     self.name = name
     self.raise_amount = 1.2
     Employee.noofemployee += 1
    def showdetails(self):
     print(f"the name of employee is {self.name} in  {self.noofemployee} sized {self.companyName} with raiseamount {self.raise_amount}")

emp1 = Employee("OM")
emp1.showdetails()
Employee.showdetails(emp1)
emp2 = Employee("nigesh")
emp2.raise_amount = 2.2 
Employee.showdetails(emp2)