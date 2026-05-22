'''
day  9 of pythn coding challange

Nested loop
-----> loop in a loop
eg: print 1 to 10
for i in range(1,10):
    for j in range(1,2):
        print(j)
        print(i)
eg : print tables 
num = 9
for i in range(1,21):
    print(f"{num} x {i} = {i*num}")
eg : checking palindrome

so = input("enter a name : ")
empty_str = ""
for j in so:
    empty_str = j + empty_str
    print(empty_str)
if empty_str == so:
    print(f"{so} is palindrome")
else:
    print(f"{so} is not a palindrome")
    
eg: checking an amstrong number or not

num = int(input("enter a number :"))
amstro_ = 0
length_= len(str(num))
for i in str(num):
          amstro_+= int(i) ** length_
if amstro_ == num:
          print(f"{num} is a amstrong number")
else:
    print(f"{num} is not a amstrong number")
    
eg: checking the number is a perfect number or not

num = int(input("enter a number:"))
per_nu = 0
for i in range(1,num):
    if num % i == 0:
        per_nu += i
if per_nu == num:
        print(f"{num} is a perfect num")
else:
        print(f"{num} is not a perfect num")
        
eg: chcecking prime number or not

num = 5
count = 0
for k in range(1,num+1):
    if num % k == 0:
        count += 1
if count == 2:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

eg: print the stars 
star_ = 5
for g in range(1,star_+1):
    for d in range(1,g+1):
        print("*", end="")
    print()
eg:
star_ = 5
for g in range(1,star_+1):
    for d in range(1,g+1):
        print(chr(64+d), end=" ")
    print()
eg:
star_ = 5
count = 0
for g in range(star_,0,-1):
    for d in range(1,g+1):
        count += 1
        print(d, end=" ")
    print()
    
eg: printing the pyramid
'''
num = 10
for j in range(1,num+1):
    print(" "*(num-j), end="")
    for i in range(1,j+1):
        print("*", end=" ")
    print()
