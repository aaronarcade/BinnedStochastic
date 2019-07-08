#not sure what classifier to use to compare overlapping intervals.
import numpy as np
import pprint
from combRegressorPlot import *

vals = combRegress()

start, stop, yval = [], [], []
colors = ["blue","green","red","cyan","magenta","brown","darkorange","grey", "pink", "purple"]
for i in range(0, len(vals)):
    for x in vals[i]:
        start.append([x[0]])
        stop.append([x[1]])
        yval.append([x[2]])



#plt.scatter(start, yval, s=10, color=colors[i-1], label="data "+str(i+1))

X = np.array(start)
y = yval

X_test = np.arange(0.0, max(X), .99999)[:, np.newaxis]
regr_1 = DecisionTreeRegressor(max_depth=5, min_impurity_split=3)
regr_1.fit(X, y)
y_1 = regr_1.predict(X_test)
plt.scatter(X, yval, s=10, color=colors[i-1], label="data "+str(i))
plt.plot(X_test, y_1, color=colors[i-1], label="fit "+str(i-1), linewidth=2)


plt.xlabel("start")
plt.ylabel("yval")
plt.legend()
plt.show()


