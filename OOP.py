# OOP = object-oriented programming
class MyClass:
    x = 5
m1 = MyClass()
print(m1.x)

class Person:
    name = "Joe"
    age = 35
    def __init__(self):
        print("My name is",self.name)
        print("My age is",self.age)
p = Person()