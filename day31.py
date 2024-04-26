#aaj sets padhenge usme kya haina ki set meh repeat occurence nae dikhata khali first time jo aata woh dikega see
s = {2, 4, 2, 6}
print(s)
random = {"lambo", 5.5, 12, True}
print(random)
#as you saw unordered hai kisi bhi random order meh print hoga vimp yaad rakhna index marke find nae kar sakte nahi replace
om = set()
print(type(om))
#om = {} aaisa karega toh empty dict banega not a set so yaad rakhna
for item in random:
    print(item) #for loop lagake bhi access kar sakte items in set