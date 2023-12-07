"""a=int(input("Enter a roll no ")) 
b=input("Enter name ")
c=input("Enter cource name ")    
"""

roll=23
name="Sita"
course="u"

def funct(roll="(not given)",name="(not submitted)",course="engineering"):    #function is defined using def keyword and variables\parameters are written in parenthesis
    
    print("         Name of student having Roll no:",roll,"is",name,"& has course",course   )


funct(roll,name,course)         #no of parameters in fun definition should be equal to no of parameters in fun called
#funct(a,b,c)                    #function calling 
funct(44,"setupati","aids")     #value for parameters are given when function is called.
funct(45)       

funct(name="shyam",course="civil")  #⏭️imp
funct(roll=int(input("Enter a roll no ")),name=input("Enter name "), course=input("Enter course ")) #⏭️imp