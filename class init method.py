class rectagle:
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth
        print("You entered length is: ",self.l,"and breadth is:",self.b)
    def area(self):
        print("Area is: ",self.l)
    def peri(self):
        print("Perimeter is: ",self.b*2+self.l*2)

obj=rectagle(20,30)                      #init method has not need to call it is automatically called when obj is created.
obj.area()
obj.peri()


'''Motive of using init method is 
when we use simple method at that time we cannot pass values externally in class
we can pass in function at time of calling'''