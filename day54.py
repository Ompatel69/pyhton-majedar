#is and == operator 
#is meh woh exact memory location dekhta hai and == meh just value same ho toh true mil jata hai

a = [1,2,3]
b = [1,2,3]
print (a is b) 
print(a == b)   #value same hai but phir bhi a is b false hai kyuki yeh list hai and it can be change 

c = (1,2,3)
d = (1,2,3)
print(c is d) #ab yeh true aaya kyuki tuple hai aur yeh immutable hai isliye memory meh same location meh store hote hai which 
print(c == d) #saves memory and pata bhi chal jata ki is hai ki nae
