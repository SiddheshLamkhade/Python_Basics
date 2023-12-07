fo=open("TypingSpeed.txt","r+")         #To Open File  file_object=open("filenamewithextension","accessmode")
                                        # file and modules are different 
                                        # module means file but containing only python program
                                        # But file may contains text or image or video or audio
print("             File Attributes")
print("Name of File: ",fo.name)                           #These are not functions They are attributes
print("Access mode of file: ",fo.mode)
print("Is File closed or not:",fo.closed)

fo.close()                             #To Close File
print("Is File closed or not:",fo.closed)

print("             Content in File")            
with open("TypingSpeed.txt","r+") as fo:  #Opening file using with keyword bcause it gets automatically closed
    for line in fo:                       #after read write operations
        print(line)                       


print("             ")
print("Is File closed or not:",fo.closed)
