#class method as alternative constructor
class Emp:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromstr(cls, string):
        return cls(string.split("-")[0], string.split("-")[1]) #classmethod banake tools bana diye kaam karne ke liye yeh fromstr likho and faat se ouput ready
    
e1 = Emp("om", 1000000)
print(e1.name)
print(e1.salary)
        
string = "ommi-9000000"        
e2 = Emp.fromstr(string)
print(e2.name)
print(e2.salary)