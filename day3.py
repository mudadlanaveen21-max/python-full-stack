'''
day 3 of  my pythonclass
1) program to convert 24th clock into normal clock
 time_ = input("enter 24 hours time:")
 parts_ = time_.split(".")
 hour_ = int(parts_[0])
 min_ = int(parts_[1])
 print(f"{time_} is converted into {hour_ - 12} : {min_} pm")

 LIST
 ----> list is a collection of different data type
 ----->[] and separated by ,
 eg: any = [1, "python", [1,2]}
 print(any)
 METHODS:
 
 append()
 ------
 --->this method isnused to to add new item into list, and it will in the last index position
 SYNTAx---> varible_name.append(item)
eg :
any = [1,2,3]
any.append(6)
print(any)
any.append([20,90])
print(any)

 extend()
 ----> this method is used to add itterable into list, and it will in the last index
       position , each value or substring is each index in tye list
sSyntax---> varible_name.extend(itterable)
so = " python is a"
print(so.replace("python", "java"))
print(so)
any[1,2,3]
print(any.append(6))
print(any)

pop()
--->used to remove the item from the list, but will mention here index position in the
    pop method
SYNTAX---> varible_name.pop(any index value)
any = [1,2,3]
any.pop(0)
print(any)

remove()
--->used to remove the item from the list, but will mention here direct in the
    remove method
SYNTAX---> varible_name.remove()
eg:
    any = [1,3,4]
    any.remove(2)
    print(any)
IMMUTABLE
---> could not able to modify on that particular varible
eg:
    int, str
MUTTABLE
---> can able to modify on that particular varible
eg:
    list
so = "python is a"
print(so.replace("python", "java"))
print(so)
any = [1,2,3]
print(any.append(6))
print(any)
'''
any = [ "java"]
any.remove("java")
print(any)








