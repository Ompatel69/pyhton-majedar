#Map Filter & Reduce banaya hai
def cube(x):
    return x*x*x
print(cube(2))

l = [2,15,3,65,43,7]
'''newl = []                                    #yeh wala toh usual                                                
for item in l:                                #method hogaya karneka
    newl.append(cube(item))
print(newl)'''

newl = (list(map(cube, l)))                   # map karke apan ne mini code banaya hai upar wala long hai yeh short hai
print(newl)                                   

'''def filter_funtion(a):
    return a > 13
nayalist = (list(filter(filter_funtion, l))) #yeh wala filter funtion hai default type
print(nayalist)'''


nayalist = (list(filter(lambda x : x > 13, l))) #yeh wala filter funtion hai mini type apne ko define karke sab karneka jarurat nae pada
print(nayalist)                                 #lamnda karke direct udhar hi logic likh diya upar cube wala bhi aaise kar sakte def ka jarurat nae tha cube wale meh

#reduce
from functools import reduce
numbers = [2,5,6,4,3]
sum = (reduce(lambda x, y: x + y , numbers))      #reduce func ko import karna padta hai normally def karke bhi logic dal sakte
print(sum)