import writeData as wd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import sklearn.tree
import matplotlib.pyplot as plt
import csv, pprint, random

#-------------------------------------------------------------------------------
# this file will save 20 png files of regressions on randomly generated datasets
#-------------------------------------------------------------------------------

for n in range(1, 21):

    training = wd.writeData()
    while type(training)==str:
        training = wd.writeData()

    Xtrain = [[p[0]] for p in training]
    ytrain = [p[1] for p in training]

    Xtest = [[p[0]+1+random.uniform(-1,1)] for p in training]
    ytest = [p[1]+1+random.uniform(-1,1) for p in training]


    X_test = np.arange(0.0, len(training), .99999)[:, np.newaxis]
    regr = RandomForestRegressor(max_depth=10,n_estimators=10)
    regr.fit(Xtrain, ytrain)

    y_1 = regr.predict(X_test)
    s = regr.score(Xtrain, ytrain)

    plt.figure()
    plt.scatter(Xtrain, ytrain, s=2, c="blue", label="training")
    plt.scatter(Xtest, ytest, s=2, c="red", label="testing")
    plt.plot(X_test, y_1, color="black", label="model", linewidth=2, alpha=0.9)
    x_l, y_l = 'data', 'target'
    plt.xlabel(x_l)
    plt.ylabel(y_l)
    plt.title("Random Forest Regression -> "+str(s)+" score")
    plt.legend()

    plt.savefig('RFRegressor_'+str(n)+'.png')
    #plt.show()
    print("saved "+str(n)+"th .png file!")
