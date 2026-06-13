'''
day 25 of my python course

PROJECT BASED ON REGULAR EXPRESSION
-----------------------------------
 VALIDATION
-------------
1)MOBILE NUMBER
---------------
---> 10 DIGITS INIT

2)PASSWORD
----------
---> CAPITAL,SMALL LETTERS,DIGITS,SPECIAL CHAR, ATLEAST 8 CHARCTERS IN THE PASSWORD

3)MAIL
------
---> @gmail.com

mobile number verification
--------------------------
import re
class Validation:
    def __init__(self):
        self.mobile_pattern = r"^[6-9][0-9]{9}"
    def mobile(self,data):
        if re.match(self.mobile_pattern, data):
            return "Valid number"
        return "Invalid number"
validate = Validation()
print(validate.mobile("8019494314 "))

email verification
------------------
import re
class Validation:
    def __init__(self):
        self.password_pattern = r"^[A-Z][a-z][@#$%^&*][0-9]"
    def password(self,data):
        if re.fullmatch(self.password_pattern, data):
            return "Valid Password"
        return "Invalid Password"
validate = Validation()
print(validate.password("Nanivardhan@123"))
'''
import re
name = input("Enter name:")
email = input("Enter email:")
mobile = input("Enter mobile num:")
password = input("Enter the password:")

if re.fullmatch(r'^[A-Za-z ]{3,}$',name):
    print("VAlid Name")
else:
    print("Invalid Name")

if re.fullmatch(r'^[a-zA-z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}$', email):
    print("Valid email")
else:
    print("Invalid email")
if re.fullmatch(r'^[6-9][0-9]{9}$',mobile):
    print("VAlid mobile num")
else:
    print("Invalid number")
if re.fullmatch(r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-za-z\d@$!%*?&]{8,}$',password):
    print("Strong Password")
else:
    print("Weak password")
