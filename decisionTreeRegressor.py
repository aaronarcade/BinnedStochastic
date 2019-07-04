import writeData as wd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
import sklearn.tree
import matplotlib.pyplot as plt

# #create data
points = wd.writeData()
print(len(points))
X = [[p[0]] for p in points]
y = [p[1] for p in points]

X_test = np.arange(0.0, len(points), .99999)[:, np.newaxis]
regr_1 = DecisionTreeRegressor(max_depth=2, min_impurity_split=2)
regr_1.fit(X, y)
y_1 = regr_1.predict(X_test)

bins, breaks = [], []
for i in y_1:
    if i not in bins:
        bins.append(i)

breaks = [] # [(start, stop, yval)]
ys = y_1.tolist()
start = 0
for i in range(0,len(points)):
    if int(ys[i+1])!=int(ys[i]):
        breaks.append((int(start), int(X_test[i]), ys[i]))
        start = X_test[i]
breaks.append((int(start), int(X_test[i]), ys[i]))

print(bins)
print(breaks)

plt.figure()
plt.scatter(X, y, s=20, edgecolor="black", c="darkorange", label="data")
plt.plot(X_test, y_1, color="cornflowerblue", label="max_depth=2", linewidth=2)
plt.xlabel("data")
plt.ylabel("target")
plt.title("Decision Tree Regression")
plt.legend()
plt.show()
