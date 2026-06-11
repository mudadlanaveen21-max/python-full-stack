'''
day 23 of my python course
File handling
-----------------> file handleer is an object of file to maintain several function of file like, creating, reading, updating
                   and deleting the file
open file
--------
1) open()
2) with open()
open('filename', 'mode') as name
----


modes
----
'r' ----> is used to reading the file, error if the file does not exist...
'a' ----> is used to add the file txt into file, if file does not exist...
not exist.....
'w' ----> is used to add the txt into file but it will override of all txt
          inside file. if the file does not exist it eill create with that name.....
'x' ----> used to create a file...
'r' ----> mode to create....

method
------
write()
-------
eg:
f = open('demo.txt', 'w')
f.write("MY class Strength is 45")
f.close()


read()
------
eg:
f = open('demo.txt', 'r')
print(f.read())
f.close()

readline()
-----------> Can read on;y one line at a time in a file.......
eg:
with open('demo.txt', 'r') as f:
    line1 = f.readline()
    line2 = f.readline()
    line3 = f.readline()
print("Line1:", line1)
print("Line2:", line2)
print("Line3:", line3)

readlines()
-----------> It will read entire file and gives in a list where esch line is each
             index in the list
eg:
with open("demo.txt", "r") as f:
    lines = f.readlines()
print(lines)
'''
