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

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def getName(self):
        return self.name

    def getWeight(self):
        return self.weight

    def toString(self):
        return "Name:" + str(self.name) + " , Weight:" + str(self.weight)

def main():

    graph = {}

    print(graph.get(1) == None)

    graph.update({1 : Nodes()})
    graph.update({2 : Nodes()})

    graph.get(1).addNode(Node(1,2))
    graph.get(1).addNode(Node(2,3))

    graph.get(2)

    graph.get(2).addNode(Node(5,6))

    print(graph.get(1).printChildren())
    print(graph.get(2).printChildren())

main()