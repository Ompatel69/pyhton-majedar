#set methods sikhenge aaaaj
name = {"om", "brim", "trim", "scream", "rimm"}
name2 = {"om", "primm", "cream", "trim", "strimm"}
name3 = name.union(name2)#do set ko mix kiya 
print(name3)
'''name.update(name2)#set 1 ko update kar diya with new values of set 2 name2 pehle dalta woh woh set update hota can update any set
print(name, name2)'''
name4 = name.intersection(name2) #ntersection_update karke same union jaisa update bhi kar sakte
print(name4)
name5 = name.symmetric_difference(name2) #common values nae print hoti
print(name5)
print(name.isdisjoint(name2))#do sets meh same values wala kuch found hua toh false varna unique hai dono sets toh true
name6 ={"om", "brim", "trim"}
print(name.issuperset(name6))#dekha yeh name6 ki sab values already original name set meh hai isliye name superset hai name6 ka
city = {"mumbai", "delhi", "hyderabad"}
city.add("kolkata")
print(city)
city.remove("kolkata")
print(city) #self explain and pop element use kar sakte any random item will get popin the  set
city2 = {"ha", "na"}
del city2#delete hogaya 
random = {"la", "ha", "tata"}
random.clear()
print(random)