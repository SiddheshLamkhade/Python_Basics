#b=float(input("Enter breadth of rectangle "))          #We have to declare this variables outside function 
                                                        #before calling
                                                        #or else at time of calling
#l=float(input("Enter length of rectangle "))
                                                    #and first of the function
def arearect(l,b):
    area=l*b
    print(area,"unit is Area of Rectangle")
arearect(l=float(input("Enter length ")),b=float(input("Enter breadth ")))
 


print("function for Area of Circle")
r=float(input("Enter radius of Circle "))
def areacir(r):
    pi=3.14
    areac=pi*r*r
    print("Area of Circle is ",areac)
areacir(r)

'''This 
is 
multiline 
comment
'''
