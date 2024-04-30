#lambda funtion sikhenge usme kya hai ki one line meh mini code bana sakte ho yeh niche wala toh regular sab likhte aaisa hai
def double(x):
    return(x*2)
print(double(5))

double = lambda x : x*2                             #yeh sab single line wale banaye 
print(double(5))
avg = lambda x, y,z : (x + y + z) / 3
print(avg(12, 7, 15))
cube = lambda x : x*x*x
print(cube(12))

def appl(fx, value):             #function meh function dalke bhi aaise kar sakte upar single line cube code banaya hai tabhi yeh create ho saka
    return 6 + fx(value)
print(appl(cube, 2))