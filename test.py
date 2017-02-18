class Nodes:
    nodes = list()

    def __init__(self):
        self.nodes = list()

    def addNode(self, node):
        self.nodes.append(node)

    def printChildren(self):
        return self.nodes

class Node:

    name = ""
    weight = 0
    children = list()
    parent = None
    marked = 0

    def __init__(self, name, weight, parent):
        self.name = name
        self.weight = weight
        self.parent = parent

    #def __init__(self, name, weight, parent):
    #    self.name = name
    #    self.weight = weight
    #    self.parent = parent
    #    self.marked = 0

    def seen(self):
        self.marked = 1

    def getName(self):
        return self.name

    def getWeight(self):
        return self.weight

    def getParent(self):
        return self.parent

    def hasNext(self):
        return len(self.children) > 0

    def addChild(self, node):
        self.children.append(node)

    def getChild(self, key):
        return self.children.index(key)

    def getChildren(self):
        return self.children

    def toString(self):
        return "Name:" + str(self.name) + " , Weight:" + str(self.weight) + " , Parent:" + str(self.parent)

def main():
    nodes = [Nodes()] * 50
    counter = 0

    file = open("example.txt")
    start = 15
    end = 5

    for line in file:
        items = line.split()
        print(line)
        nodes[int(items[0])].addNode(Node(int(items[1]), int(items[2]), int(items[0])))
        # name, weight, parent
#        graph.addNode(int(items[1]), int(items[2]), int(items[0]))

    for node in nodes:
        for t in node.printChildren():
            print(t.toString())


main()