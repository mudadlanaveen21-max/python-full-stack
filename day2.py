day 2 of my python course
'''
Operators
--------
1)Arthimetic opertator
    {+,-,*,%,/,//,**}
    print(2*3)
    print(4%5 == 0)
    print(10**2)
    print(10/2)
    print(35.20//5)
2)Assignment operator
    =, +=,, -=, %=, *=
3)CompRISION OPERator
    ==, !=, >=, <=, >, <
4)Identity operator
    is, is not
NOte: is--->this operator looks for the objecct is same or not
        ==---> Looks for both values are equal or not
5)Logical operator
    and--> this operator used to check both should be true
    or--->this operator used to check at least one should be true
    not-->this operator is used to check both are false
6)Membership operator
    in----> this operator looks for the object is same or not
    not in--> this operator not looks the object is same or not
7)Bitwise operator
    &, |, <<,>>
a = 9 #immutable
b = 9.0
print(a+b)

STRINGS
    "",'','''''
String is sequence of char that are enclosed in '',"",''''' and string is a immutable
any = "" @&,."

METHIODS

1) replace()
        ----> used to replace with a new subsrtring
    Syntax
        -----> varible_name.replace("old string", "new string")
2) Split()
        ----> used to separate iintom parts,
                    and it will split based on the substring where before substring is
                        one index and after is another index in the list

    Syntax
        -----> varible_name.split("substring")
        eg: any = "python is a language"
        print(any.split("$"))
Functions

1) len()
        ----> get number of items, substring
    Syntax----> len(varible _name)
    eg: any = "python is a language"
        print(len(any))
2) slicing()
        ---->can give the access to get particular part from the string
    Syntax----> varible_name[starting index : ending index]
    eg : any = "python is a language"
         print(any[3:11])
3) indexing()
        ------> used to get substring present in that index position...
    Syntax-----> varible_name[index position]
    eg: any = "python is a language"
        print(any.index("ang"))


        count
join ---->substring.join
        syntax---> "substr".join(vari)


        
      '''
