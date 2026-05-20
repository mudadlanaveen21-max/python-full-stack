'''
day 7 of my python course

F-string
-----> fstring means it can be used with out commas
eg:
num = 8
if  num % 2 == 0:
    print(f"{num} is a even number")
    
condition statements
---------> if,elif,nested if
if---> to check wheather the statement 
eg:
num = 8
if num % 2 == 0:
    print("even")

if-else----> else in the if statement , incase the condition becomes false
                then it will enter into fall-back(else)
eg:
num = int(input("enter a number :"))
if num % 2 != 0:
    print(f"{num} is a odd number")
else :
    print(f"{num} is a even number")

practice eg : voting
age_ = 11
if age_ >= 18:
    print("you are eligible to vote")
else :
    print(f" you are not eligible to vote {18-age_}")
    
eg: greater or smaller number

num = 11
num_2 = 15
if num >= 2:
    print(f"{num} is a greatest number than {num_2}")
else :
    print(f"{num_2} is a greater number than {num}")
    
eg: leap year

year_ = 2025
if (year_ % 4 == 0 and year_ % 100 != 0) or year_ % 400 == 0:
    print(f"{year_} is a leap year")
else :
    print(f"{year_} is not a leap year")

eg : vowels or consonants

vowel_ = "b"
if vowel_ in "AEIOUaeiou":
    print(f"{vowel_} is a vowel")
else :
    print(f"{vowel_} is a consonant")

eg: positive or negative number

num = 1
if num >=0:
    print(f"{num} is a positive number")
else :
    print(f"{num} is a negative number")
eg: fail or pass

marks_ = int(input("Enter your marks : "))
stu_name = input("enter your name :")
if marks_ >= 45:
    print(f"{stu_name} your passed")
else :
    print(f"{stu_name} your failed")
    
    
eg : divisiblity rule

num = 33
if num % 3 == 0 and num % 5 == 0 :
    print(f"{num} is divisible by 3 and 5 ")
else:
    print(f"{num} is not divisible by 3 and 5")
'''
