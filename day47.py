#secret message program
st = input("enter your message")
words = st.split(" ")
coding = False
if(coding):
 nwords = []
 for word in words:
    if(len(word)>=3):
     r1 = "hfg"
     r2 = "pmy"
     stnew = r1 + word[1:] + word[0] + r2
     nwords.append(stnew)
    else:
     nwords.append(word[::-1])
 print(" ".join(nwords))

else:
    nwords = []
    for word in words:
     if(len(word)>=3):
      stnew = word[3:-3]
      stnew = stnew[-1] + stnew[:-1]
      nwords.append(stnew)
     else:
      nwords.append(word[::-1])
    print(" ".join(nwords))
