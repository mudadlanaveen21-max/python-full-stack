'''
day 27 of my python course
DATA ANALYSIS:
--------------
-->THIS IS PROCESS OF INSPECTING, CLEANING,TRANSFROMING, AND MODELING DATA TO DISCOVER USEFUL INSIGHTS...
TYPES OF DA:
------------
1.DESCRIPTIVE ANALYSIS
----------------------
-->SUMMARIZING CAUSES

2.DIAGNOSTIC ANALYSIS:
----------------------
-->UNDERSTANDING CAUSES

3.PREDICTIVE ANALYSIS:
----------------------
-->FORECASTING FUTURE OUTCOMES
4.PRESCRIPTIVE ANALYSIS:
------------------------
-->SUGGESTING ACTINS BASED ON DATA

WHY DA:
-------
-->TO IMPROVE DECISION MAKING
-->DETECTS TRENDS & PATTERNS

NUMPY (NUMERICAL PYTHON):
-------------------------
-->THIS PYTHON LIBERARY FOR NUMERICAL COMPUTING .IT PROVIDES SUPPORt FOR MULTIDIMENSINOL ARRAYS, AND LINEAR ALGEBRA
OPEARTIONS MAKING IT ESSENTIAL FOR DATA NALYSIS

USING NUMPY IN DA
-----------------
---> IMPROVED PERFORMANCE
---> SIMPLIFIES COMPLEX QUESTIONS
---> EASY DATA MANIPULATION

import numpy as np
arr_1 = np.array([[1,2,3,4], [5,6,7,8], [2,4,6,8]])
print(arr_1)

import numpy as np
arr_1 = np.array([[1,2,3], [5,6,7]])
print(arr_1)
print(arr_1.shape)
reshaped = arr_1.reshape(3,2)
print(reshaped)

import numpy as np
arr_1 = np.array([1,2,3,4,5])
print(arr_1)
print(arr_1 + 5)

import numpy as np
arr_1 = np.array([1,2,3,4,5])
print(arr_1)
print(arr_1 * 5)

import numpy as np
arr_1 = np.array([[1,2], [1,2]])
arr_2 = np.array([[1,2], [4,5]])
print(np.dot(arr_1, arr_2))

import numpy as np
arr_1 = np.array([10,20,30])
nrm_copy = arr_1.view()
arr_1[0] = 100
print(nrm_copy)
print(arr_1)


Pandas
------
---> pandas is a powerful data manipulation and analysis library...
---> Where it provides data structure like series and dataframe for efficient data handling....
eg:
import pandas as pd
any_ = pd.Series([2999, 15999, 52999,4999,1999],
                 index = ['Ear Buds', 'SmartPhone', 'Lap', 'Watch', 'Footware'])
print(any_)
Method Series
-------------
mean()
sum()
max()
min()
apply()
map()

Dataframe
---------
'''
import pandas as pd
data = {
    'product' : ['Earbuds', 'smartpjone', 'lap', 'watch', 'footware'],
    'brand' : ['Noise', 'oneplus', 'hp', 'bolt', 'nike'],
    'price': [1599,1599,23400,56800,3400],
    'stock' : [50,15,25,40,70]
    }
dip = pd.DataFrame(data)
print(dip)
