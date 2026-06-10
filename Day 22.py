'''
day 22 off my python course

Error Handling
--------------

Try block
------------> The try block, test a block of code for error
Except Block
-------------> The except block let the code handle if the code contain errors.....
Else Block
-------------> this will executed, if the try block has no error in the code....

Note: 
----
Final Block
-------------> This will be executed either try block contain error or not....
try:
    print(a)
except:
    print("NameError can be handled")

try:
    print(a)
except TypeError:
    print('This can handle NameError')
else:
    print("no error")

try:
    print(5+"Py")
    print(a)
except TypeError:
    print('This can handle TypeError')
except NameError:
    print('This can handle NameError')
else:
    print("no error")

try:
    print("Hai")
except TypeError:
    print('This can handle TypeError')
except NameError:
    print('This can handle NameError')
else:
    print("no error")
    
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    else:
        print("Division successful. Result =", result)
    finally:
        print("Execution finished.")


divide_numbers(10, 2)   
divide_numbers(5, 0)    

def sum_numbers(a,b):
    try :
        print(a * b)
    except :
        print("error: cannot multiply those num")
    else:
        print("multiplying two numbers successfully")
    finally:
        print("execution done")
sum_numbers(10,2)
sum_numbers(1,2)
'''
