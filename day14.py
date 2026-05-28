'''
day 14 of my python course
List comprehension
------------------
-----> this list comperhension shortest syntax when we want to create a new list from existing list
syntax---> vari_name = [expression loop condition]
eg:
old_ = [1,2,3,4,5]
new_ = [so for so in old_ if so % 2 == 0]
print(new_)
eg:
old = [1,28,3,42,5,66,7,83,9]
new = [so if so % 2 == 0 else "even" for so in old]
print(new)
               
generators
----------
-----> generators in python are special type of iterable allows users to iterate over data
       efficiently without storing everything the memory...
------> genrates the values lazily using yield keyword

why to use gen
--------------
-----> Genrators does not store the entire data set in a memory, they generate values
        on the fly or run fly
-----> avoiding the unneccessary storage of data speed up the execution.

How it works
-----------
---> it looks like nrml function but uses the yield keyword instead of return
---> when the fun is called, it does not execute immediately, Instead, it returns a
     generator object which can be iterated using loop or the next() function

eg:
def simple_gen():
    print("Start")
    yield 1
    yield 2
    yield 3
    yield 44
    print("end")
gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
eg:
def sqr(num):
    result = []
    for i in range(1,num+1):
        result.append(i&i)
    return result
print(sqr(5))

def any(num):
    for i in range(1,num+1):
        yield i*i
a = any(5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
'''
so = 'naveen is a bad boy, class "12"'
any = ''
for j in so:
    if j  not in "AEIOUaeiou" :
        any += j
print(any)
