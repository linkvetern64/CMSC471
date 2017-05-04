class Point:

    '''
    data - vector containing valued information about data
    label - String of the data points actual value
    flag - A numeric representation (0 - 2) in this example that will
           represent the value corresponding to it's assigned centroid
    '''
    def __init__(self, data, label):
        self.data = data
        self.label = label
        self.flag = -1

    def getData(self):
        return self.data

    def getLabel(self):
        return self.label

    def setFlag(self, flag):
        self.flag = flag

    def getFlag(self):
        return self.flag

    def toString(self):
        return "My data is - " + str(self.data) + " my label is - " + self.label + "\n"