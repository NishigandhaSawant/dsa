from array import *
val = array('i',[1,2,3,4,5,6,7,8,9,10])

for i in range(0,len(val)):
    print(val[i], end=' ')
print('\n')
for x in val:
    print(x, end=' , ')

"""print(val.buffer_info())
print(val.typecode)
val.reverse()
for i in range(0,len(val)):
    print(val[i], end=' ')"""
print('\n')

val.insert(2, 11)
val.append(100)
val[2] = 200
for i in range(0,len(val)):
    print(val[i], end=' ')  