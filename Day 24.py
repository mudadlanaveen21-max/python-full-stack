'''
day 24 of my python course


Regular Expression (RegEx)
-------------------------
----> RegEx is a sequence of char that from a searching pattern....
----> This can be used to check if a string contain  the specified search pattern...
----> Python has a built-in package clled're' which can be used to work with RegEx....

Functions in re
---------------
1. Findall
eg:import re
any_ = " C is a 1programming 3language9"
print(re.findall('[al]',any_))
                    
2. Search
eg: import re
any_ = " C is a 1programming 3language9"
print(re.search('[al]',any_))
                    
3. Fullmatch
eg: import re
any_ = " C is a 1programming 3language9"
print(re.fullmatch('[a]',any_))
                    

metachar
--------
[]---> a-z,A-z,0-9, and my specified squence...
------
eg:
import re
any_ = " C is a 1programming language"
print(re.search('[l.....ge]',any_))
                    

dot . ---> Here each dot is one char
---
eg:
import re
any_ = " C is a 1programming language"
print(re.search('l.....ge',any_))


 ^ (cap symbol)---> This look for the string is starting with specified sequence or not...      
--------------

$ dollar ----> This look for the, string is ending with specified sequence or not...
--------
eg:import re
any_ = "python is a foundational"
print(re.findall('foundational$',any_))

* star symbol ----> Zero or more
-------------
eg:
import re
any_ = "python is a foundational"
print(re.findall('p.*thon',any_))

? question mark-----> zero or one
---------------
eg:
import re
any_ = "python is a foundational"
print(re.findall('p.?thon',any_))

+ plus symbol ---> one or more occurences
-------------
eg:
import re
any_ = "python is a foundational"
print(re.findall('p.+ython',any_))

{} flower brackets -->
------------------
eg:
import re
any_ = "python is a foundational"
print(re.findall('p.{7}',any_))

Special Sequence
----------------
\S ---> No space
\s ---> only space
\D ---> digits will gone
\d ---> only digits will come
\W ---> only special characters will be printed
\w ---> matchs any words char (letters, digits, underscore)
eg:
import re
any_ = "python is a  323foundational@."
print(re.findall('\W',any_))


finding a  indian mobile number
-------------------------------
import re
mobile_ = input(" Enter 10 digit mobile number: ")
how = re.fullmatch('[6-9][0-9]{9}', mobile_)
if how:
    print(f"{mobile_} this is india number")
else:
    print(f"{mobile_} this not a india number")
    
finding a telephone number or not
--------------------------------
import re
telephone = input("enter a telephone number:")
how = re.fullmatch('[0-9][0-9][0-9]', telephone)
if how:
    print(f"{telephone} it is a telephone number")
else:
    print(f"{telephone} it is not a telephone number")
