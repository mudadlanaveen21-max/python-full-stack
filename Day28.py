'''
day 28 if my python course

MATPLOTLIB:
-----------
-->THIS IS A LIBRARY IN PYTHON FOR DATA VISUALIZATION, ALLOWING USERS TO CREATE
A VARIETY OF PLOTS,..

BAIC STRUCTURE OF MATPLOTLIB:
-----------------------------
-->FIGURE
-->AXES
-->AXIS
-->GRID
-->TITLE
-->LEGEND
------------------------------------

import matplotlib.pyplot as plt
sales = ['A','B','C']
values = [25,30,45]
plt.bar(sales,values,color = 'red',edgecolor = 'black')
plt.xlabel('CAR models')
plt.ylabel('values')
plt.title('BMW sales')
plt.show()


import matplotlib.pyplot as plt
overs = [1,2,3,4]
score = [10,20,30,50]
plt.plot(overs,score)
plt.title('score card')
plt.xlable('overs')
plt.ylable('scores')
plt.show()

import matplotlib.pyplot as plt
subjects = ['python', 'java', 'c']
students = [35,7,15]
plt.pie(students,labels=subjects)
plt.title('students in courses')
plt.show()

import matplotlib.pyplot as plt
subjects = ['python', 'java', 'c']
students = [35,7,15]
plt.pie(students,labels=subjects,autopct='%1.1f%%')
plt.legend(subjects)
plt.title('students in courses')
plt.show()


import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [10,15,18,20,23]

plt.scatter(x,y,color = "red")
plt.title('Scatter plot')
plt.xlabel('X values')
plt.ylabel('Y label')
plt.show()

import matplotlib.pyplot as plt
y = [10,15,18,20,23]

plt.hist(y,color = "red")
plt.title('Histogram plot')
plt.xlabel('X values')
plt.ylabel('Y label')
plt.show()

import matplotlib.pyplot as plt
sales = ['A','B','C']
values = [25,30,45]
plt.bar(sales,values,color = 'red',edgecolor = 'black')
plt.xlabel('CAR models')
plt.ylabel('values')
plt.title('BMW sales')
plt.show()

import matplotlib.pyplot as plt
subjects = ['python', 'java', 'c']
students = [35,7,15]
plt.pie(students,labels=subjects)
plt.title('students in courses')
plt.show()

import matplotlib.pyplot as plt
cars = ['BMW', 'AUDI', 'BENZ']
sales = [23,44,46]
plt.pie(sales,labels=cars,autopct='%1.1f%%')
plt.legend(cars)
plt.title('Cars sales in a year')
plt.show()

import matplotlib.pyplot as plt
sales = ['A','B','C']
values = [25,30,45]
plt.bar(sales,values,color = 'red',edgecolor = 'black')
plt.xlabel('CAR models')
plt.ylabel('values')
plt.title('BMW sales')
plt.show()

'''
import matplotlib.pyplot as plt
company = ["tcs", "wipro", "tech mahindra"]
jobs = [25,10,20]
plt.bar(company,jobs,color = "blue",edgecolor = 'red')
plt.legend(company)
plt.xlabel('Years')
plt.ylabel('companys')
plt.title('jobs in a year')
plt.show()
plt.show()
