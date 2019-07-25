import random, writeData as wd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

#---------------------------------------------------------------------------
# this file will evaulate 30 iterations of scores based on conditions of RFR
# - - - - change the condition to iterate:line 24 and x_l,y_l:line 32- - - -
#---------------------------------------------------------------------------

training = wd.writeData()
while type(training)==str:
    training = wd.writeData()

Xtrain = [[p[0]] for p in training]
ytrain = [p[1] for p in training]

Xtest = [[p[0]+1+random.uniform(-1,1)] for p in training]
ytest = [p[1]+1+random.uniform(-1,1) for p in training]

notested = 30
scores = [(RandomForestRegressor(max_depth=d).fit(Xtrain, ytrain).score(Xtest, ytest)) for d in range(2,notested+2)]
depths = [d for d in range(2,notested+2)]

[print(d,"\t",s) for s,d in zip(scores,depths)]

plt.figure()
plt.plot(depths, scores, linewidth=2, color="blue", label="scores")

x_l, y_l = 'max_depth', 'score'

plt.xlabel(x_l)
plt.ylabel(y_l)
plt.title("Random Forest Regression -> "+x_l+" vs "+y_l)
plt.legend()

plt.show()
