str="Hello"
print(str)
print(str[0])
print(str[0:2])
print(str[-1])
newstr="G"+str[1:]
print(newstr)

print("          in Operator        ")
print("G" in newstr)
print(str in newstr)

print("          iterating strings      ")
for i in newstr:
    print(i)


print("          iterating strings using while loop      ")

i=0
while i<len(str):
    print(str[i])
    i=i+1