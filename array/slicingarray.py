from array import *

val = array('i',[1,2,3,4,5,6,7,8,9])

"""a = val[2:5]"""
"""a = val[::-1]     #reversing an array"""
a = val[2:5:1]
for i in range(0,len(a)):
    print(a[i], end=' ')