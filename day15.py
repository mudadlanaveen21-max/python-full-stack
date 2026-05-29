'''
day 15 of my python course
Modulus
-------
---> A modulus in python is a file that contains python code such as
    #varibles
    #functions
    #classes
    #statements
two types of modulus
--------------------
1)user-define
2) built in
------------
eg:
def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)

eg:
import math
print(math.sqrt(25))
print(math.factorial(10))
print(math.pow(2,5))

eg:
import os
os.remove("deo.txt")

eg:
import sys
print(sys.version)
print(sys.path)
print(sys.exit)

eg:

import  random
print(random.randint(1000,9999))

eg:

from collections import Counter
data = ['a','b','c','d']
counter = Counter (data)
print(counter)

dd = defaultdict(int)
dd['missing'] += 1
print(dd['missing'])
print(dd)
task:
is,==
mutable,immutable
extend,append
memory allocation in python
