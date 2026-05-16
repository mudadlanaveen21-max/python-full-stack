'''
day 4 of my python class

 concatination
 ------> the(+) for int and can add, but for the other data types it will act as concatination
         the data type
eg :
a = 90
b = 8
print(a+b)
any_ = "python"
so = "is a language"
print(any_ + so)
an = [1,2]
am = [3,4]
print(an + am)

TUPLE
-----> collection of different data types separated by commas, represenred in ()
        and immutable
METHODS
1) COUNT()
    -----> this method is used to count hte particular item in the tuple
    SYNTAx---> varible_name.count(item)
eg:
some = (6,"Naveen",[1,23,44,56],"Naveen", (2,33,45))
print(some.count("Naveen"))

2) INDEX()
    ----> used to find out the index position of the item, only gives the first oocurance
    SYNTAX----> varible_name.index()
eg:
    some = (6,[1,23,44,56],"Naveen", (2,33,45))
    print(some.index("Naveen"))
eg:
name = ("naveen", 78, "varshi", 1)
print(name.index("varshi"))

DICTONARY
---------> Dict is a key : value pair, key and value is  separated by : and pair is
            separated by comma
      ----> represented by {}
    
eg:
naveen_details = {"name" : "naveen",
                     1 : 2,
                     (1,2) : [4,2]}
print(naveen_details)

1) values()
------> used to get all values from the dict
syntax---> dict.values()
eg:
naveen_details = { "name" : "naveen",
                   "age" : 21 , 
                   "MobN" : "8019494314",
                   "pan" : "25874169"}
print(naveen_details.keys())


 items()
 -----< used to get key value together
 syntax--> dict.items()
 eg:
naveen_details = { "name" : "naveen",
                   "age" : 21 , 
                   "MobN" : "8019494314",
                   "pan" : "25874169"}
print(naveen_details.items())
print(naveen_details["MobN"])

update()
-----> used to add a new key : value pair into dict
syntax----> dict.update({key:value})
eg:
naveen_details = { "name" : "naveen",
                   "age" : 21 , 
                   "MobN" : "8019494314",
                   "pan" : "25874169"}
naveen_details.update({"Adhar":"1234455456566"})
print(naveen_details)
eg:
naveen_details = { "name" : "naveen",
                   "age" : 21 , 
                   "MobN" : "8019494314",
                   "pan" : "25874169"}
naveen_details['Adhar'] = ("1234455456566")
print(naveen_details)

clear()
----->used to remove all the items in the dict
syntax-----> dict.clear()
eg:
naveen_details = { "name" : "naveen",
                   "age" : 21 , 
                   "MobN" : "8019494314",
                   "pan" : "25874169"}
naveen_details.clear()
'''
print(naveen_details)
