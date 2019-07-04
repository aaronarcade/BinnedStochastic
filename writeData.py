# 04072019 - Aaron Brown
import csv, pprint, random

def writeData():
    numPoints = 100
    points = []   #(xval, yval)
    x = 0

    while x+1 < numPoints:
        randE = random.uniform(-3,3)
        if x in range(0,33):
            points.append((x+1, int(numPoints/3)+randE))
        elif x in range(34,63):
            points.append((x+1, int(2*numPoints/3)+randE))
        elif x in range(64,99):
            points.append((x+1,int(numPoints)+randE))
        x+=1

    return(points)
