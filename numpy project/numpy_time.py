import time
import numpy as np
import sys

pl1 = []
size = 1000000

for i in range(size):
    pl1.append(i)

pl2 = []
size = 1000000

for i in range(size):
    pl2.append(i)

start = time.time()
result = [(x+y) for x, y in zip(pl1, pl2)]
print("python list takes: ", (time.time() - start)*1000) 

npa1 = np.array(pl1)
npa2 = np.array(pl2)

start = time.time()
result = npa1 + npa2
print("numpy list takes: ", (time.time() - start)*1000)