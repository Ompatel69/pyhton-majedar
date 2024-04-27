#local variable vs global variable
x = 10 #global var che
def func1():
    global x #yeh likha toh global var 10 ko replace karke apne 4 naya global ban gaya
    x = 4
    y = 5
    print(y)#local var

func1()
print(x)

#avoid this as it is for info only keep the program simple desgin your programs smartly