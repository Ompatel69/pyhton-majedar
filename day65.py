#STATIC METHOD
class Math:
    def __init__(self, num):
        self.num = num
    def addtonum(self, n):
        self.num = self.num + n
    
    @staticmethod  #par agar koe bade funtion meh complex math karna ho toh static bana ke rakho and then niche call kiya wese karo toh easy hoga
    def add(a, b):
        return(a + b)

a = Math(10)
print(a.num)
a.addtonum(6) #class instance meh addtonum def kiya hai and chalra yeh toh normal instance method hai
print(a.num)
print(Math.add(27, 30)) #just like this call it by calling the class name and . static def name thazz it
