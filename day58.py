class Person:
    def __init__(self, n, o):
        print("hellos")
        self.name = n
        self.occ = o
    def info(self):
        print(f"{self.name} is a {self.occ}")
a = Person("om", "software developer")
b = Person("vidya", "coder")       
a.info()
b.info()
