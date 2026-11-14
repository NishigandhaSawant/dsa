from numpy import *

val = array([1, 2, 3, 4, 5, 6.7, 7, 8, 9, 'a', 'love'])
'''val = array([1, 2, 3, 4, 5, 6.7, 7, 8, 9], float)'''
for x in val:
    print(x, end=' ')

#numpy gives us abilty to do heterogeneous array, but it will convert all the values to the same data type. In this case, it will convert all the values to float.

 