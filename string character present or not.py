str=input("Enter a String: ")
ch=input("Enter a character: ")
for i in str:
    if ch in str:
        print("Character is present in string")
        break
    else:
        print("It is not present")
        break
        
