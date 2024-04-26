
#while loop with else use karke dikhaege
i = 0
while i < 7:
    print(i)
    i = i + 1
    #if i == 4:
     #break

else:
   print("i khtam")
'''loop ko break kiya unexpected toh else execute nae hua woh tabhi hi execute hoga jab successful loop end hoga'''
#for loop with else
for x in range(7):
    print("iteration {} loop ke andar".format(x + 1))
else:
    print("else loop meh aaya")

    print("loop khtam")
#done