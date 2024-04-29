#seek() and tell functions sikhenge
with open("myfile3.txt", "r") as f:
    print(type(f))
    f.seek(12)
    data=f.read(5)
    print(data)


with open("myfile2.txt", "w") as f:
    f.write("hello world")
    f.truncate(5)
with open("myfile2.txt", "r") as f:
    print(f.read())