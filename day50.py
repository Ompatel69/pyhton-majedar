#yeh hai readline methods 
f = open("myfile.txt", "r")
i = 0
while True:
    i = i + 1
    line = f.readline()
    if not line:
        break
    m1 = line.split(",")[0]
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]
    print(f"marks of student {i} in Maths is {m1}")
    print(f"marks of student {i} in English {m2}")
    print(f"marks of student {i} is SST is {m3}")
    print(line,"\n")
    

#yeh hai write line methods
f = open("myfile2.txt", "w")
print(f"line1\nline2\nline3\n")
f.writelines(line)
f.close()