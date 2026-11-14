from array import *
val = array('i',[1,2,3,4,5,6,7,8,9,10])

copyArray = array(val.typecode, [x*4 for x in val])
for i in range(0,len(copyArray)):
    print(copyArray[i], end=' ')
print('\n')
"""copyArray.pop()

for i in range(0,len(copyArray)):
    print(copyArray[i], end=' ')"""



copyArray.remove(20)    
for i in range(0,len(copyArray)):
    print(copyArray[i], end=' ')