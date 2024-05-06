#inheritance in python
class emp:
    def __init__(self, id, name):
     self.id = id
     self.name = name

    def showdetails(self):
        print(f"the employee {self.id} is {self.name}")
    
class Programmer(emp): #class name change kiya and naya details bhi bhara emp ka content bhi migrate hogaya
   def showlanguage(self):
    print("the default language is Python")

e1 = emp(400, "om patel")
e1.showdetails()
e2 = emp(235, "Ronit D")
e2.showdetails()
e2 = Programmer(324, "Dublak") #programmer karke line likha tab naya details aaya kyuki naya class has all old content with new ones also
e2.showdetails()
e2.showlanguage()
