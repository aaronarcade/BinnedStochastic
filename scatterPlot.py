# 04072019 - Aaron Brown
#imports
import writeData as wd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
import sklearn.tree
import matplotlib.pyplot as plt

for i in range(0,50):
    points = wd.writeData()

def scatter():
    # #create data
    points = wd.writeData()
    X = [[p[0]] for p in points]
    y = [p[1] for p in points]

    #plot figure
    plt.figure()
    plt.scatter(X, y, s=20, edgecolor="black", c="darkorange", label="data")
    plt.xlabel("data")
    plt.ylabel("target")
    plt.ylim(0, 100)
    plt.title("Scatter Plot")
    plt.legend()
    #plt.show()

