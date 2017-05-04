from Centroid import Centroid
from Point import Point
import random
import math

'''
Project 4: K-means Classificiation
Author:
Date: 

Implements a K-means classifier on the Iris dataset
'''
#Assuming vectors with N dimensions gets distance from p2 to p1
def distance(p1, p2):
    if len(p1) != len(p2): return -1
    sums = 0
    for N in range(0, len(p1), 1):
        sums += ((p2[N] - p1[N])**2)
    return math.sqrt(sums)


#Train a k-means classifier with the given data and labels.
def train(data, labels, k=3):
    #k = 9 #gives 96.67%
    if len(data) != len(labels): raise Exception('Data size inconsistent with labels')
    #Will contain random centroid points for clustering
    points = []
    centroids = []
    labelsUnique = set(labels)
    #random.seed(1)

    #Split data into points
    for i in range(0, len(data), 1):
        points.append(Point(data[i], labels[i]))

    #Generate random points and append

    for i in range(0, k, 1):
        loc = points[random.randrange(0,len(points),1)].getData()
        centroids.append(Centroid(loc, i))


    #Gets K-means starting centroids by random grouping selection
    '''
    index = 0
    for label in labelsUnique:
        sub = []
        for i in range(0, len(data), 1):
            if labels[i] == label:
                sub.append(data[i])

        loc = sub[random.randrange(0, len(sub), 1)]
        centroids.append(Centroid(loc, index))
        index += 1
    '''

    # Gets K-means starting centroids by means of initial labels grouping
    '''
    index = 0
    for label in labelsUnique:
        sub = [0, 0, 0, 0]
        total = 0
        for i in range(0, len(data), 1):
            if labels[i] == label:
                sub[0] += data[i][0]
                sub[1] += data[i][1]
                sub[2] += data[i][2]
                sub[3] += data[i][3]
                total += 1

        if total != 0:
            sub[0] = sub[0] / total
            sub[1] = sub[1] / total
            sub[2] = sub[2] / total
            sub[3] = sub[3] / total

        centroids.append(Centroid(sub, index))
        index += 1
    '''
    #Start the clustering algorithm
    for n in range(0, 30, 1):
        for point in points:
            #Check against each centroid
            closest = 10000000000
            for centroid in centroids:
                dist = distance(point.getData(), centroid.getPoints())
                if dist < closest:
                    #print(dist)
                    closest = dist
                    point.flag = centroid.getFlag()
                    #print("Flag = " + str(point.flag))

        #Calculate new centroid centers
        for i in range(0, k, 1):
            total = 0
            avg = [0,0,0,0]
            for point in points:
                if point.getFlag() == i:
                    avg[0] += point.getData()[0]
                    avg[1] += point.getData()[1]
                    avg[2] += point.getData()[2]
                    avg[3] += point.getData()[3]
                    total += 1
            if total != 0:
                avg[0] = avg[0] / total
                avg[1] = avg[1] / total
                avg[2] = avg[2] / total
                avg[3] = avg[3] / total
                centroids[i].setPoints(avg)
            #print("( " + str(n) + "," + str(i) + " ) = " + str(avg))

    #assign centroids the label by the avg label found in each centroid
    for centroid in centroids:
        occur = []
        for point in points:
            if point.getFlag() == centroid.getFlag():
                occur.append(point.getLabel())

        largest = 0
        for label in labelsUnique:
            count = occur.count(label)
            if count > largest:
                largest = count
                centroid.setLabel(label)

    return centroids

def classify(x, model):
    """Classify a sample using the given model."""
    closest = 10000000
    label = ""
    for centroid in model:
        dist = distance(centroid.getPoints(), x)
        if dist < closest:
            label = centroid.getLabel()
            closest = dist
    return label