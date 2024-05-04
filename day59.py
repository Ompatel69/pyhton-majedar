
def greet(fx):
    def mfx(*args, **kwargs):
     print("good morning")
     fx(*args, **kwargs)                                          #yeh decorator function banaya jo good morning and thanks wala lines run karta hai if  
     print("thanks for using this function")         #called using greet apne ko chahiye ki bohot sare function hai toh sab run ho uske pehle
    return mfx                                               # greet karna chahiye ijjat se toh yeh greet har fucntion ke pehle dal sakte toh run hoga
    

@greet
def hello():
   print()
def add(a, b):
    print(a + b)

hello()
#greet(add)(10,7) aaise bhi kar sakte and upar greet active hai abhi wese bhi
add(10,7)