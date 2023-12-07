print("       Program for renaming and deleting file")
import os
os.rename("TypingSpeed.txt","typingspeed.txt")   #for delete replace rename by "remove" 



with open("typingspeed.txt","a") as fo:
    print("             After renaming file")
    print("Name of file is: ",fo.name)


print("       some direcory/folder 00functions00")
import os
print(os.getcwd())
#print(os.listdir())
#os.mkdir()
#os.chdir()