# compare numpy arrays and python lists

import numpy as np
import sys
import time

l1 = []
size = 10000
step = 3
start = 1
for i in range(start, size, step):
    l1.append(i)
    
print(l1)

na1 = np.array(l1)
print(na1)

print(sys.getsizeof(5)*len(l1))
print(na1.size*na1.itemsize)