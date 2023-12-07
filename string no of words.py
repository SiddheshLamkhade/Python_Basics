str=input("Enter string: ")
print("No of characters are: ",len(str))

list=str.split()
print("splitted string into list is: ",list)
w=0
for i in list:
    w+=1
print("No. of words present in string are: ",w)