'''
day 21 of my python course

print(f"Name: {self.name}, Age: {self.age}, University: {Person.university_name}, Edu_BG: {self.Edu_BG}, gender: {self.gender}, department: {self.department}")

class Person:
    university_name = "codegnan university"

    def __init__(self, name, age, Edu_BG, gender, department):
        self.name = name
        self.age = age
        self.Edu_BG = Edu_BG
        self.gender = gender
        self.department = department

    def display_info(self):
        pass
        

class Student(Person):
    def __init__(self, name, age, Edu_BG, gender, department, course, days):
        self.course = course
        self.days = days
    def display_info(self):
        pass
class Faculty(Student):
    def __init__(self, name, age, Edu_BG, gender, department, course, days, subject):
        super().__init__(name, age, Edu_BG, gender, department, course, days)
        self.subject = subject
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, University: {Person.university_name}, Edu_BG: {self.Edu_BG}, gender: {self.gender}, department: {self.department}, subject: {python}")
        
s1 = Faculty("Naveen", 21, "BTECH" , "Male" , "CSE" , "Python Full Stack", 90, "python")
s1.display_info()

class Person:
    university_name = "codegnan university"

    def __init__(self, name, age, Edu_BG, gender, department):
        self.name = name
        self.age = age
        self.Edu_BG = Edu_BG
        self.gender = gender
        self.department = department

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, University: {Person.university_name}, "
              f"Edu_BG: {self.Edu_BG}, Gender: {self.gender}, Department: {self.department}")


class Student(Person):
    def __init__(self, name, age, Edu_BG, gender, department, course, days):
        super().__init__(name, age, Edu_BG, gender, department)
        self.course = course
        self.days = days

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Course: {self.course}, Duration: {self.days} days, "
              f"University: {Person.university_name}, Edu_BG: {self.Edu_BG}, Gender: {self.gender}, "
              f"Department: {self.department}")


class Faculty(Person): 
    def __init__(self, name, age, Edu_BG, gender, department, course, days, subject):
        super().__init__(name, age, Edu_BG, gender, department, course, days)
        self.subject = subject

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, University: {Person.university_name}, "
              f"Edu_BG: {self.Edu_BG}, Gender: {self.gender}, Department: {self.department}, "
              f"Course: {self.course}, Duration: {self.days} days, Subject: {self.subject}")



s1 = Student("Naveen", 21, "BTECH", "Male", "CSE", "Python Full Stack", 90)
s1.display_info()
s2 = Faculty("Teja", 25, "btech", "male", "ece", "python full stack", 90, "python")
s2.display_info()

2)

class Person:
    university_name = "codegnan university"

    def __init__(self, name, age, Edu_BG, gender, department):
        self.name = name
        self.age = age
        self.Edu_BG = Edu_BG
        self.gender = gender
        self.department = department

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, University: {Person.university_name}, "
              f"Edu_BG: {self.Edu_BG}, Gender: {self.gender}, Department: {self.department}")


class Student(Person):
    def __init__(self, name, age, Edu_BG, gender, department, course, days):
        super().__init__(name, age, Edu_BG, gender, department)
        self.course = course
        self.days = days

    def display_info(self):
        super().display_info()  
        print(f"Course: {self.course}, Duration: {self.days} days")


class Faculty(Person): 
    def __init__(self, name, age, Edu_BG, gender, department, course, days, subject):
        super().__init__(name, age, Edu_BG, gender, department)  
        self.course = course
        self.days = days
        self.subject = subject

    def display_info(self):
        super().display_info()  
        print(f"Course: {self.course}, Duration: {self.days} days, Subject: {self.subject}")




s1 = Student("Naveen", 21, "BTECH", "Male", "CSE", "Python Full Stack", 90)
s1.display_info()


s2 = Faculty("Teja", 25, "BTECH", "Male", "ECE", "Python Full Stack", 90, "Python")
s2.display_info()
'''
class University:
    university_name = "VISAKHA INSTITUTE OF ENGINEERING AND TECHNOLOGY"

    def display_university(self):
        print(f"University Name : {University.university_name}")


class Person(University):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_person(self):
        self.display_university()
        print(f"Name            : {self.name}")
        print(f"Age             : {self.age}")
        print(f"Gender          : {self.gender}")


class Student(Person):
    def __init__(self, name, age, gender, student_id, department):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.department = department

    def display_info(self):
        print("\n----- STUDENT DETAILS -----")
        self.display_person()
        print(f"Student ID      : {self.student_id}")
        print(f"Department      : {self.department}")


class Faculty(Person):
    def __init__(self, name, age, gender, faculty_id, subject):
        super().__init__(name, age, gender)
        self.faculty_id = faculty_id
        self.subject = subject

    def display_info(self):
        print("\n----- FACULTY DETAILS -----")
        self.display_person()
        print(f"Faculty ID      : {self.faculty_id}")
        print(f"Subject         : {self.subject}")


class LabAssistant(Person):
    def __init__(self, name, age, gender, employee_id, lab_name):
        super().__init__(name, age, gender)
        self.employee_id = employee_id
        self.lab_name = lab_name

    def display_info(self):
        print("\n----- LAB ASSISTANT DETAILS -----")
        self.display_person()
        print(f"Employee ID     : {self.employee_id}")
        print(f"Lab Name        : {self.lab_name}")


class Librarian(Person):
    def __init__(self, name, age, gender, employee_id):
        super().__init__(name, age, gender)
        self.employee_id = employee_id

    def display_info(self):
        print("\n----- LIBRARIAN DETAILS -----")
        self.display_person()
        print(f"Employee ID     : {self.employee_id}")


class Watchman(Person):
    def __init__(self, name, age, gender, employee_id, shift):
        super().__init__(name, age, gender)
        self.employee_id = employee_id
        self.shift = shift

    def display_info(self):
        print("\n----- WATCHMAN DETAILS -----")
        self.display_person()
        print(f"Employee ID     : {self.employee_id}")
        print(f"Shift           : {self.shift}")


class Cleaner(Person):
    def __init__(self, name, age, gender, employee_id, area):
        super().__init__(name, age, gender)
        self.employee_id = employee_id
        self.area = area

    def display_info(self):
        print("\n----- CLEANER DETAILS -----")
        self.display_person()
        print(f"Employee ID     : {self.employee_id}")
        print(f"Cleaning Area   : {self.area}")


class Canteen(University):
    def __init__(self, canteen_name, location, manager):
        self.canteen_name = canteen_name
        self.location = location
        self.manager = manager

    def display_info(self):
        print("\n----- CANTEEN DETAILS -----")
        print(f"University Name : {University.university_name}")
        print(f"Canteen Name    : {self.canteen_name}")
        print(f"Location        : {self.location}")
        print(f"Manager         : {self.manager}")


class Block(University):
    def __init__(self, block_name, purpose):
        self.block_name = block_name
        self.purpose = purpose

    def display_info(self):
        print("\n----- BLOCK DETAILS -----")
        print(f"University Name : {University.university_name}")
        print(f"Block Name      : {self.block_name}")
        print(f"Purpose         : {self.purpose}")




s1 = Student("Naveen", 21, "Male", "22L61A5444", "CSE")
s2 = Student("Nani", 21, "Male", "23L65A0421", "MECH")
f1 = Faculty("Rajesh", 45, "Male", "F101", "Python")
la1 = LabAssistant("Shiva", 30, "Male", "L101", "Python Lab")
lb1 = Librarian("Lakshmi", 35, "Female", "LB101")
w1 = Watchman("Puli", 58, "Male", "101", "Night")
cl1 = Cleaner("Ramu", 42, "Male", "103", "Block A")


c1 = Canteen("Main Canteen", "Block A", "rahul")
c2 = Canteen("Food Court", "Block B", "Fathima")
c3 = Canteen("Snack Point", "Near Library", "Kamala")

b1 = Block(
    "Visvesvaraya block",
    "MECH,CIVIL,M.TECH First Year Classrooms")

b2 = Block(
    "APJ Abdul Kalam Bhavan",
    "CSE, ECE, EEE,MBA Second Year Classrooms")

b3 = Block(
    "MWDL",
    "Python Lab, Java Lab, AI Lab")

b4 = Block(
    "Library Block",
    "Central Library")

b5 = Block(
    "Administration Block",
    "Principal Office, HOD Cabins, Accounts Section")



s1.display_info()
s2.display_info()
f1.display_info()
la1.display_info()
lb1.display_info()
w1.display_info()
cl1.display_info()

c1.display_info()
c2.display_info()
c3.display_info()

b1.display_info()
b2.display_info()
b3.display_info()
b4.display_info()
b5.display_info()
