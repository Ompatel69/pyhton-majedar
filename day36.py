a = input("Enter the Number : ")
print(f"Multiplication table of {a} is: ")
try:
    for i in range(1, 11):
     print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print(e)
    print("must be an invalid input try again")
