class Parent:
    var="This is parent class"
class Child(Parent):      #Usually we don't write parenthesis next to class name But for inheritance purpose we did that
    var2="This is child class"
object=Child()


print(object.var)