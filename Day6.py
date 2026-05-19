'''
day 6 of my python class
type conversions
----------------
int---> int can be converted into string,float
eg:
an = 78
us = str(an)
om = float(an)
print(om)
print(type(om))
print(type(us))

str
---> string is  converted into integer

an = "40"
ear = int(an)
print(type(an))
in str we can convert str into int if we have input is integers
conversions
an = "90"
ear = list(an)
print(ear)
print(type(ear))
con = tuple(an)
print(con)

float--->float can be converted into integer and string

car = 90.7
print(int(car))
print(str(car))

list---->list is converted into tuple and string

an = [1,2,3]
print(str(an))
print(tuple(an))

Tuple--->tuple is converted into list and string

how = (9,0)
print(list(how))
print(str(how))

int as a user_input---->

num = int(input("Enter a number :"))
print(89 + num)

str as use_input---->

some = input("Write a text:")

any = list(map(int,input("enter a number:").split()))
print(any)

tuple as user_input
-------> 
any = tuple(map(int,input("enter a number:").split()))
print(any)

eval as user_input---->

num = eval(input("enter :"))
print(type(num))
'''

