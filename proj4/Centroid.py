class Centroid:

    '''
    Points - Contains the [W,X,Y,Z] values of centroid
    Label - numeric value of the labels used
    '''
    def __init__(self, points, flag):
        self.points = points
        self.flag = flag
        self.label = ""

    #Set a specific point in the centroid
    def setPoint(self, index, value):
        self.points[index] = value

    #Set centroid to all new points
    def setPoints(self, points):
        self.points = points

    #Get the points of the centroid
    def getPoints(self):
        return self.points

    #Return the numeric value of the centroids assigned label
    def getFlag(self):
        return self.flag

    #Sets the label value for the centroid
    def setFlag(self, flag):
        self.flag = flag

    def setLabel(self, label):
        self.label = label

    def getLabel(self):
        return self.label