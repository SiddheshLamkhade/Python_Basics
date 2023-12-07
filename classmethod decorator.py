class Student:
    @classmethod
    def greet(cls):
        print("Welcome")

Student.greet()          # @classmethod is used to access any method or function in class without creating object
                         # By using classname.methodname()
