class Nodes:
    nodes = list()

    def __init__(self):
        self.nodes = list()

    def addNode(self, node):
        self.nodes.append(node)

    def printChildren(self):
        print(len(self.nodes))

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
        self.marked = 0

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
    start = 1
    end = 4
    nodes = [None] * end

    if(nodes[2] == None):
        nodes[2] = list()
    nodes[2].append(Node(3,34,2))
    nodes[2].append(Node(3,34,2))
    nodes[2].append(Node(3,34,2))
    nodes[2].append(Node(3,34,2))
    nodes[2].append(Node(3,34,2))

    print(len(nodes[2]))

main()