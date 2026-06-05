'''
day 19 of my python course
INHERITANCE
-----------
--> this inheritance allows one class to aquire the properties and methods of another class...
Types
-----
1) single inheritance
-------------------------> A class inherts from a single parent class...
                            (Single inheritance have one parent class and one child class)
eg:
class father:
    def Land(self):
        print(" I am father i have 5acres")
class Naveen(father):
    def my_own(self):
        print('I have 2 acres')
fam = Naveen()
fam.Land()
eg:
class Codegnan:
    def student(self):
        print('total pfs students are 45 members')
class Naveen(Codegnan):
    def Pfs(self):
        print('i am one of the student in PFs')
all_ = Naveen()
all_.student()
all_.Pfs()

2) mulitiple inheritance
---------------------------> A child class inherts from more
                            (a single child class can borrow features from two or more
                            parent classes)
eg:
class father:
    def Land(self):
        print(" I am father i have 5acres")
class mother:
    def gold(self):
        print("my mother have 1kg gold")
        
class Son(father,mother):
    def mine(self):
        print('I have ntg')
all_ = Son()
all_.Land()
all_.gold()
eg:
class Codegnan:
    def student(self):
        print('how many students are there in batch 003')
class Jfs:
    def members(self):
        print('Jfs students are 11 members')
class Naveen(Codegnan,Jfs):
    def Pfs(self):
        print('i am one of the student in PFs')
all_ = Naveen()
all_.student()
all_.members()
all_.Pfs()

3) Multi level inheritance
---------------------------> A class inherts a parent class and another class inherts from
                             that child class
eg:
class grandfather:
    def Land(self):
        print(" I am grandfather i have 5acres")
class father(grandfather):
    def flat(self):
        print("my father have 1 flat")
        
class Son(father):
    def Ntg(self):
        print('I own both of their p')
all_ = Son()
all_.Land()
all_.flat()
all_.Ntg()
eg:
class Codegnan:
    def so(self):
        print('how many students are there in batch 003')
class Branch(Codegnan):
    def any(self):
        print('Jfs students are 11 members')
class Naveen(Branch):
    def Pfs(self):
        print('i am one of the student in PFs')
all_ = Naveen()
all_.so()
all_.any()
all_.Pfs()

4) Hierarichical inheritance
-----------------------------> Multiple child classes inherts from a single parent
eg:
class father:
    def Land(self):
        print(' I have 10 acres')
class Naveen(father):
    def mine(self):
        print("job")
class Vardhan(father):
    def bro(self):
        print("jobless")
all_ = Naveen()
all_.Land()
all_ = Vardhan()
all_.Land()


5)Hybride inheritance
-----------------------> This is the combination of two or more types of inheritance
eg:
class A:
    def Some(self):
        print('Class A')
class B:
    def any(self):
        print('Class B')
class C:
    def so(self):
        print('Class C')
class D(B,C):
    def All_(self):
        print('Class D')
how = D()
how.so()

#super() method
----------------> super() is used to access the methods and constructor of the parent
                  class from the child class
eg:
class parent:
    def display(self):
        print('Method parent')
class child(parent):
    def display(self):
        super().display()
        print('Method child')
any_ = child()
any_.display()
eg:
class Person:
    def __init__(self, name):
        self.name = name

class stu_(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

    def show(self):
        print(f"Name: {self.name}")
        print(f"Roll: {self.roll}")

all_ = stu_('nani', 578)
all_.show()
        




class Codegnan:
    def so(self):
        print('how many students are there in batch 003')
class Branch(Codegnan):
    def any(self):
        print('Jfs students are 11 members')
class Naveen(Branch):
    def Pfs(self):
        print('i am one of the student in PFs')
all_ = Naveen()
all_.so()
all_.any()
all_.Pfs()

class Person:
    def __init__(self, name):
        self.name = name

class stu_(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

    def show(self):
        print(f"Name: {self.name}")
        print(f"Roll: {self.roll}")

all_ = stu_('nani', 578)
all_.show()
eg: for multi level     
class grandparent:
    def Ace(self):
        print("Grandparent:", 'i have earned 50 acres')
class parent(grandparent):
    def So(self):
        print("parent:", 'i have earned a bmw car')
class child(parent):
    def any(self):
        print("child:", 'i have ntg')
so = child()
so.Ace()
so.So()
so.any()
'''
class A:
    def featureA(self):
        print("Feature A")

class B(A):
    def featureB(self):
        print("Feature B")

class C(A):
    def featureC(self):
        print("Feature C")

class D(B, C):
    def featureD(self):
        print("Feature D")

d = D()
d.featureA()
d.featureB()
d.featureC()
d.featureD()

