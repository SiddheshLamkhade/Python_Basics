class Employee:
    def __init__(self,name,designation):
        self.n=name
        self.d=designation
        print("Employee name: ",self.n,"is at position",self.d)
E1=Employee("Shriram","CEO")
E2=Employee(input("Enter name: "),input("Enter designation: "))