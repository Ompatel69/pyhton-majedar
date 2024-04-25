#aaj dictionary sikhege 
dict = { "Om":"Patel"} #key value pairs banae aur print meh access kiya key ko toh value aagaya
print(dict["Om"])
print(dict)

dict2 = { 911 : "porsche",
          458 : "ferrari",
          "aventador" : "lamborghini"}
print(dict2)
#print(dict2[912]) #aise acces karoge toh error dega
print(dict2.get(912)) #isme dictionary name with .get karke access karenka try kiya toh none aya and not error
print(dict2.keys()) #same .values type karoge toh values milegi
for key in dict2.keys():
    print(dict2[key])