from combRegressorPlot import *
from scipy.spatial import cKDTree
import numpy as np
from pprint import pprint as pprint

n = 5

breaks = combRegress(n)
# pprint(breaks)
# showme()
xs, ys = [], []
def intersect_close(a,b,tol=20):
    dist = cKDTree(a).query(b, k=1)[0]
    if b[dist<=tol].tolist()!=[]:
        return b[dist<=tol].tolist()

tol = 15
for b in range(0, len(breaks)):
    for a in range(0, len(breaks)):
        if a!=b:
            dist = cKDTree(np.array(breaks[b][0::2])).query(np.array(breaks[a][0::2]), k=1)[0]
            ret = (np.array(breaks[a][0::2])[dist<=tol])
            if ret.tolist()!=[]:
                for d in range(int(ret.tolist()[0][0]), int(ret.tolist()[0][1])):
                    xs.append(ret.tolist()[0][0]+d-int(ret.tolist()[0][0]))
                    ys.append(ret.tolist()[0][2])

#pprint(xs)

colors = ["blue","green","red","cyan","magenta","brown","darkorange","grey", "pink", "purple"]
for i in range(0,len(xs)):
    plt.subplot(414)
    #print(xs[i][0], xs[i][2])
    plt.scatter(xs[i], ys[i], color="black", label="tree ", s=.5)
    plt.xlabel("data")
    plt.ylim(0, 100)
    plt.xlim(0, 100)

showme()
