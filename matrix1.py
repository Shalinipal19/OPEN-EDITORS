#program to multiply two matrix(vectorized implementation)

import numpy as np

A=[[1,7,3],
   [4,5,6],
   [7,8,9]]

B=[[3,5,1,2],
   [6,7,3,0],
   [4,5,59,1]]

#result will be 3*4

result=[[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]

result = np.dot(A,B)

for r in result:
    print(r)
A=[[3,5,1,2],
   [6,7,3,0],
   [4,5,59,1]]

