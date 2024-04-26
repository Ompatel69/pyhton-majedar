
#finnally ka importance
def func1():
    try:
        l = [10, 2, 5, 16]
        i = int(input("Enter the index number: "))
        print(l[i])
        return 1
    except:
        print("some error occured")
        return 0 
    
    finally:
        print("amar hu meh")
x = func1()

print(x)
#done