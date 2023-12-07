class Simplemethod:
    roll=123
    def fun(self):
        name="Shriram"
        print("This is simple function",self.roll,name)

obj=Simplemethod()

obj.fun()           #function inside class
print(obj.roll)     #variable inside class
#print(obj.name)    #we can't access variable inside function. bcause it is local variable


class Initmethod:
    mark=100
    def __init__(self):
        mrk=345
        print("This is init method marks are: ",self.mark,mrk)    #Pay attention on self pointer
obj1=Initmethod()

class Student:
    def __init__(self,roll,name):
        self.roll=roll
        self.name=name
        print("Roll no. is ",self.roll,"Name is ",self.name)
objj=Student(45,"ramesh")