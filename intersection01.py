from combRegressorPlot import *
from scipy.spatial import cKDTree
import numpy as np
from pprint import pprint as pprint

n = 10

# breaks = combRegress(n)
# pprint(breaks)
# showme()

def intersect_close(a,b,tol=1):
    dist = cKDTree(a).query(b, k=1)[0]
    print(b[dist<=tol])


breaks = [[[1,2],[2,3]],[[4,5],[5,6]],[[0,1],[5,6]]]
intersect_close(breaks[0][0], breaks[0][1])
for b in range(0, len(breaks)):
    for a in range(0, len(breaks)):
        if a!=b:
            print(breaks[b], breaks[a])








a = np.array([[1,2],[3,4],[5,6],[7,8],[8,10]])
b = np.array([[6,7],[8,9],[9,10]])
#intersect_close(a, b)
