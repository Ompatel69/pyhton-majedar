#classmethod decorater
class Employee:
    company = "Apple"
    def show(self):
        print(f"the employee name is {self.name} and the company is {self.company}")
    
    @classmethod #class method lagaya ab cls name change karega globally rather than for that specific instance
    def changecompany(cls, newcompany):
        cls.company = newcompany
    
e1 = Employee()
e1.name = "om"
e1.show()
e1.changecompany("NASA") #isne toh instance meh company name change kar diya as shown below
e1.show() 
print(Employee.company) #but jab employee ka company name pucha toh apple hi aaya kyuki class name default apple hai usko agar global change dena hai toh upar dekh
e1.show()

#before output
'''the employee name is om and the company is Apple
the employee name is om and the company is NASA
Apple'''
#after output
'''the employee name is om and the company is Apple
the employee name is om and the company is NASA
NASA
the employee name is om and the company is NASA'''