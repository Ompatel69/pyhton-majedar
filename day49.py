'''f = open("myfile.txt", "r")
#print(f)
text = f.read()                        #dekha read mode
print(text)
f.close()'''

'''f = open("myfile2.txt", "a")
f.write(" , my nigga")                #write mode with a karke karega toh append mode meh chalega 
f.close()'''

with open("myfile3.txt", "w") as f:     #with karke karega toh f.close() use karneka ka jarurat nae hai
    f.write("helloss")
