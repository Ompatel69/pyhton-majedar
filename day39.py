#kbc
questions = [
  [
    "capital of india?", "mumbai", "banglore", "kolkata", "delhi", 4
  ],
  [
    "Cricket meh kitne players hote hai?", "9", "10", "12", "15", 3
  ],
  [
    "Which language was used to create fb?", "Python", "French", "php",
    "JS", 3 
  ],
  [ 
    "national anthm kisne likha hai?", "mohamad rafi", "rabindra nath tagore", "dada Harish bhai"
    "chacha bose", 2
  ],
  [ 
    "Virat ki biwi ka naam kya hai?", "neha ", "alia bhatt", "anushka sharma", "jackline fernandes", 3
  ],
  [ 
    "Which company owns multiple car brands?", "volkswagen", "Toyota", "BMW", "mercedes-benz", 1
  ],
]
levels = [1000, 2000, 3000, 4000, 5000, 10000,]
money = 0
for i in range(0, len(questions)):

    question = questions[i]
    print(f"\nQuestion for Rs. {levels[i]}")
    print(f"{question[0]}")
    print(f"a. {question[1]}               b. {question[2]} ")
    print(f"c. {question[3]}               d. {question[4]} ")
    reply = int(input("ENter your ans: \n"  ))
    if (reply == question[-1]):
        print(f"Correct Answer, you have won Rs. {levels[i]}")
        if (i == 1):
            money = 2000
        elif (i == 3):
            money = 4000
        elif (i == 5):
            money = 10000
    else:
        print("wrong Answer")
        break

print(f"your take home money is {money}")