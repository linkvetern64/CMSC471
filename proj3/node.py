class Node:

    def __init__(self):
        self.branches = dict()
        self.data = ()
        self.labels = ()

    def addBranch(self, key, data):
        d = {"key" : "val"}
        self.branches.update(d)

    def printBranches(self):
        print(self.branches)

    def updateData(self, data):
        self.data[:-1] = data