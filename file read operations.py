with open("typingspeed.txt","r") as fo:
    print("           for whole file")
    print(fo.read())

print("           for specific lines")
with open("typingspeed.txt","r") as fo:print(fo.read(10))

print("           for one line")
with open("typingspeed.txt","r") as fo:
    print(fo.readline())

print("            list() function")
with open("typingspeed.txt","r") as fo:
    print(list(fo))                              

print("            for loop over file")
with open("typingspeed.txt","r") as fo:
    for line in fo:
        print(line)

print("             split one line in file into words")
with open("typingspeed.txt","r") as fo:
    line=fo.readline()
    print(line)
    list=line.split()
    print(list)