import writeData as wd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
import sklearn.tree
import matplotlib.pyplot as plt
import pprint

#-------------------------------------------------------------------------------
# set up function
#-------------------------------------------------------------------------------
def combRegress():
    lis, tes, combBreaks = [], [], []

    for n in range(1, 11):
        #create data
        points = wd.writeData()

        #prevent use of any poor data constructions (overlapping data from writeData.py)
        while type(points)==str:
            print("!Killed data set!")
            points = wd.writeData()

        #set Target and Data for regression
        X = [[p[0]] for p in points]
        y = [p[1] for p in points]

        #run regression
        X_test = np.arange(0.0, len(points), .99999)[:, np.newaxis]
        regr_1 = DecisionTreeRegressor(max_depth=5, min_impurity_split=3)
        regr_1.fit(X, y)
        y_1 = regr_1.predict(X_test)

    #---------------------------------------------------------------------------
    # determine breakpoints of regression for comparison
    #---------------------------------------------------------------------------

        bins, breaks = [], []
        for i in y_1:
            if i not in bins:
                bins.append(i)


        #****features will be found here****
        breaks = [] # [(start, stop, yval)]
        ys = y_1.tolist()
        start = 0
        for i in range(0,len(points)):
            if int(ys[i+1])!=int(ys[i]):
                breaks.append((int(start), int(X_test[i]), ys[i]))
                start = X_test[i]
        breaks.append((int(start), int(X_test[i]), ys[i]))

        # print(bins, breaks) #yvals, (start, stop, yval)

        lis.append((X, y))
        tes.append((X_test, y_1))

        #****this is the feature string****
        combBreaks.append(breaks)

    #---------------------------------------------------------------------------
    # plot unfit, fitted, and fit regressions
    #---------------------------------------------------------------------------

    colors = ["blue","green","red","cyan","magenta","brown","darkorange","grey", "pink", "purple"]
    for i in range(0,len(lis)):
        #unfit points in scatterplot
        plt.subplot(311)
        plt.scatter(lis[i][0], lis[i][1], s=10, color=colors[i-1], label="data "+str(i+1))
        plt.ylim(0, 100)
        plt.ylim(0, 100)
        plt.title("Prefit, Combined, and Fit Regression")
        plt.legend()

        #scatterplot and fit decision tree model
        plt.subplot(312)
        plt.scatter(lis[i][0], lis[i][1], s=10, color=colors[i-1], label="data "+str(i))
        plt.plot(tes[i][0], tes[i][1], color=colors[i-1], label="tree "+str(i), linewidth=2)
        plt.ylim(0, 100)
        plt.ylabel("target")
        plt.ylim(0, 100)

        #only fit decision tree model
        plt.subplot(313)
        plt.plot(tes[i][0], tes[i][1], color=colors[i-1], label="tree "+str(i), linewidth=2)
        plt.xlabel("data")
        plt.ylim(0, 100)
        plt.ylim(0, 100)

    print("\n---- complete ----\n")
    print("type 'showme()' to display triple plot\n")
    #pprint.pprint(combBreaks)
    return(combBreaks)


#will display plots
def showme():
    plt.show()
