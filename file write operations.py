with open("typingspeed.txt","w") as fo:                         #file is opened in w+ mode
    fo.write("This is written using write operations which got overwrite to avoid that use append mode")      
                                                                #it is overwritten
'''with open("typingspeed.txt","a") as fo:
    fo.write("Here We used append mode so file will not get overwrite.")
    fo.write("Content will be added at end of file but it is not convenient")'''



    print("read write pointer in file is at: ",fo.tell())             #tell and seek function
    fo.seek(10)
    print("After using seek function now pointer is at: ",fo.tell())

 
with open("typingspeed.txt","r") as fo:
    print(fo.read())  
                                              