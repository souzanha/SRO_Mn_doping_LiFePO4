import numpy as np
import sys

data=np.loadtxt(sys.argv[1])

avg=0
for i,j in zip(data[:,0],data[:,1]):
   avg += i*j

print(avg/sum(data[:,1]))
    
