#numpy operations

import numpy as np

ld1 = [1,2,3]
ad1 = np.array(ld1)
#print(ad1)

md2 = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
ad2 = np.array(md2)
#print(ad2)

npa1 = np.arange(0, 120)
print(npa1)
xa1 = npa1.reshape((2,3,4,5))
print(xa1)

xa1 = np.random.randint(0,1000,7)
print(xa1)
print(xa1.dtype)

print(xa1.max())
print(xa1.min())

print(xa1.argmax())
print(xa1.argmin())
