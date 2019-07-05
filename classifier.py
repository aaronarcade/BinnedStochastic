#not sure what classifier to use to compare overlapping intervals.
import numpy as np
from combRegressorPlot import *

vals = combRegress()


colors = ["blue","green","red","cyan","magenta","brown","darkorange","grey", "pink", "purple"]
for i in range(0, len(vals)):
    start, stop, yval = np.array([[x[0]] for x in vals[i]]), [x[1] for x in vals[i]], [x[2] for x in vals[i]]
    plt.scatter(start, yval, s=10, color=colors[i-1], label="data "+str(i+1))

    print(start, "----------------")
    X = start
    y = yval

    X_test = np.arange(0.0, max(X), .99999)[:, np.newaxis]
    regr_1 = DecisionTreeRegressor(max_depth=5, min_impurity_split=3)
    regr_1.fit(X, y)
    y_1 = regr_1.predict(X_test)
    plt.plot(X_test, y_1, color=colors[i-1], label="fit "+str(i-1), linewidth=2)


    plt.xlabel("start")
    plt.ylabel("yval")
    plt.legend()
plt.show()


