'''
day 20 of my python course

Polymorphism
---------------> This means 'many forms'.. it allows the same function, method, or operator
                 to behave differently depending on the object..
1) Method Overloading
-----------------------> method overloading means defining multiple methods with the same
                         name but different parameters
eg:
class calculator:
    def add(self, a, b, c=0):
        return a+b+c
An = calculator()
print(An.add(23,6))
print(An.add(23,4,5))
eg:
class calculator:
    def add(self, a, b, c=0):
        return a+b+c
    def sum(self, a, b, c=0):
        return a - b - c
An = calculator()
print(An.add(23,6))
print(An.sum(23,4,5))
        

2) Method overriding
-----------------------> This occurs when a child provides its own implementation of a
                         method overriding defined in the parent class....
eg:
class animal:
    def sound(self):
        print("animal make sounds")
class dog(animal):
    def sound(self):
        print("Dog barks")
ntg = dog()
ntg.sound()

eg: using super()

class animal:
    def sound(self):
        print("animal make sounds")
class dog(animal):
    def sound(self):
        super().sound()
        print("Dog barks")
ntg = dog()
ntg.sound()

3) Operator Overloading
---------------------------> This allows operators such as +, -, * etc,, to perform
                           different actions for user-defined objects
Note: The operator inside the method will overload a special method or a operator
      given in the calling function
eg:
class stu_:
    def __init__(self,marks):
        self.marks = marks
    def __add__(self, b):
        return self.marks + b.marks
so_1= stu_(4)
so = stu_(78)
print(so_1 + so)

Data Abstraction
------------------> This is the process of hiding internal implementation details and
showing only the essential features to the user
----> it focuses on what an object does rather than how it does it....

from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def perimeters(self):
        pass
class Rec(shape):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    drf area(self):
        return self.a = afrom abc import ABC, abstractmethod
'''
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def perimeters(self):
        pass

class Rec(shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def area(self):
        return 2*(self.a * self.b)

an = Rec(10, 5)
print(an.area())
