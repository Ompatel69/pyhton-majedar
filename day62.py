#public private protected convection hai python kuch enforce nae karta simple hai agar __(private) dalke kiya toh automatically mangling kar deta program
#and khali single _(protected) dalke kiya toh indication hai ki aap kar sakte private protected and public is accessible n private is not accesible directly 
#indirectly sab hota hai lets see

class emp:
    def __init__(self):
        self.__name = "om"
        
a = emp()
#print(a.__name) directly access nae hua
print(a._emp__name) #indirectly access hogaya
        