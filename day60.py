class Myclass:
    def __init__(self, value):
        self._value = value
    
    def show(self):
        print(f"value is {self._value}")

    @property #getter decorater hai
    def ten_value(self):
        return 10 * self._value
    
    @ten_value.setter #getter wala defined fnc name hai woh dalke .setter karo toh set bhi kar sakte phir logic meh
    def ten_value(self, new_value):
        self._value = new_value/10

obj = Myclass(10)
print(obj.ten_value)
obj.ten_value = 2567
print(obj.ten_value)
obj.show()
