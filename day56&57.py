#OOP - object oriented programming
class Person:
    name = "om"
    occupation = "Software Developer"
    def info(self):
     print(f"{self.name} is a {self.occupation}")
a = Person()
a.info()