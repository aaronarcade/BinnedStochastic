# 04072019 - Aaron Brown
import csv, pprint, random

def writeData():
    numPoints = 100
    numBins = int(random.uniform(1,10))
    points = []   #(xval, yval)
    bins = []    #(start, stop)
    x = 0

    #set yvals for bins
    randY = [random.uniform(0,100) for i in range(0,numBins)]

    #set partitions of sample space
    rem, opart = numPoints, 0
    for b in range(0,numBins):

        #if the last element, fill to 100 points
        if b == numBins-1:
            bins.append((opart+1, numPoints))
            break

        #random partition size
        part = int(random.uniform(opart+1,10))
        bins.append((opart+1, opart+1+part))

        #prevent overlapping points
        if opart+1>=100 or opart+1+part>=100:
            print("poor data construction")
            return("error")

        #set floor of next partition
        opart = opart+1+part
        rem = 100-part-opart-1
    #print(bins)***************************

    #append x,y to list to return
    for i in range(0,len(bins)):
        for x in range(bins[i][0],bins[i][1]):
            points.append((x, randY[i]+random.uniform(-2,2)))

    #return x,y for scatterplots
    return(points)

