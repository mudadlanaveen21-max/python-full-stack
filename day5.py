'''
day 5 of my python class
sets
-----> a set is a collection of unique items and unordered elements
-----> Duplicate values are not allowed
-----> Items are not not stored in index order 
-----> represented in curly braces {}
eg :
any = (1,2,2,3,4)
print(any)

union()
-----> it will combine 2 sets together at once
-----> it will represented by|
syntax
-----> varible_name.union(another varible)
eg:
any = { 1,2,3,4,}
an = {50,30,80}
print(any | an)
print(any.union(an))

intersection ()
-----> to get common elements from both sets
syntax
-----> varible_name.intersection(another var)
eg:
any = {2,3,3,4,5}
an = {2,5,3}
print(any and an)
print(any.intersection(an))

difference()
------> it removes both sets same values and give other values
syntax
------> varible_name.difference()
eg:
any = { 1,2,2,3,4,}
an = {3,26,89,4}
print(any - an)
print(an.difference(any))

symmetric_difference()
-------> it removes same values
eg:
any = { 1,2,2,3,4,}
an = {3,26,89,4}
print(any - an)
print(an.symmetric_difference(any))

add()
-----> to add a new element to a set
syntax
-----> varible_name.add(element)
eg:
any = { 1,2,2,3,4,}
any.add(41)
print(any)

update()
------> to add multiple elements to the set
syntax
------> varible_name.update([elements])
eg:
any = {1,2,3,4}
any.update([32,41])
print(any)

remove()
-----> it removes the element from the set
-----> if the given element is not in the set then it shows an error keyerror
syntax
-----> varible_name.remove(element)
eg:
any = {1,2,3}
any.remove(4)
print(any)

discard()
-----> it also removes an element from the set
-----> it does not show any error if we give the element which is not in the set
eg:
any = {1,2,3}
any.discard(4)
print(any)
    



