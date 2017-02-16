#Author: Joshua Standiford
#Date:2/8/2017
#Desc: This program will simulate the Breadth-First-Search, Depth-First-Search, Uniform Cost Search
#Algorithms.

#--- Import Statements ---
import sys

#Class: Nodes
#Class Invariants: None
#Preconditions: None
#Postconditions: None
#Desc:
#This class will contain class Node children of current index in graph
class Nodes:
    nodes = list()

    def __init__(self):
        self.nodes = list()

    def addNode(self, node):
        self.nodes.append(node)

    def getNodes(self):
        return self.nodes

    def printChildren(self):
        for node in self.nodes:
            print(node.toString())

#Class: Node
#Class Invariants: None
#Preconditions: None
#Postconditions: None
#Desc:
#Container class that holds edge weight and child information
class Node:

    name = ""
    weight = 0
    parent = 0

    def __init__(self, name, weight, parent):
        self.name = name
        self.weight = weight
        self.parent = parent

    def getName(self):
        return self.name

    def getParent(self):
        return self.parent

    def getWeight(self):
        return self.weight

    def toString(self):
        return "Name:" + str(self.name) + " , Weight:" + str(self.weight)

#Class: Graph
#Class Invariants: None
#Preconditions: None
#Postconditions: None
class Graph:
    queue = list()
    stack = list()
    graph = {}
    visited = list()
    start = 0
    end = 0

    #Constructor
    def __init__(self, start, end):
        self.queue = list()
        self.stack = list()
        self.graph = {}
        self.visited = list()
        self.start = start
        self.end = end
        self.queue.append(int(self.start))

    #Prints all items and their edges in the graph
    def printGraph(self):
        for i in range(1, len(self.graph), 1):
            self.graph.get(i).printChildren()


    #Adds new node to graph
    #Preconditions: pos, dest, weight all integers
    #Postconditions: node is added to graph
    #@pos : position of self node
    #@dest : node to point to from current node
    #@weight : the cost to move from this node to the next
    def addNode(self, index, name, weight):
        #Creates nodes in dictionary if it doesn't exist
        if(self.graph.get(index) == None):
            self.graph.update({index : Nodes()})
        self.graph.get(index).addNode(Node(name, weight, index))

    #Returns
    def getIndex(self, index):
        return self.graph.get(index)

    #Breadth-First-search
    def BFS(self):
        self.queue = list()
        path = list()
        #If start is the same as end, return
        if(self.start == self.end):
            print(list())
            return

        self.queue.append(self.start)
        while self.queue:
            tmp = int(self.queue.pop())
            if tmp == self.end:
                break
            for item in self.graph.get(tmp).getNodes():
                if item.getName() not in self.visited:
                    self.visited.append(item.getName())
                    self.queue.append(item.getName())

    #Depth-First-Search
    def DFS(self):

        #If start is the same as end, return
        if(self.start == self.end):
            print(list())
            return
        elif(str(self.start) not in self.graph):
            print(list())
            return


        while len(self.queue) >  0:
            item = self.queue.pop()

            self.visited.append(int(item))

            if(item == self.end):
                print(self.visited)
                return

            self.queue.append(self.graph.get(str(item))[0])

        print(self.visited)

    #Uniform Cost Search
    def UCS(self):
        print("UCS")


#Name: Main
#Preconditions: must have arguments - FILE_NAME START_NODE END_NODE SEARCH_TYPE
#Postconditions:
#Desc: Driver function for search.py
def main():

    #pulls command line arguments
    file = open(sys.argv[1])
    start = sys.argv[2]
    end = sys.argv[3]
    search = sys.argv[4]

    graph = Graph(int(start), int(end))

    #splits lines then adds the nodes to a graph
    for line in file:
        items = line.split()
        graph.addNode(int(items[0]), int(items[1]), int(items[2]))


    #Search method passed in via CMD line
    if(search == "BFS"):
        graph.BFS()
    elif(search == "DFS"):
        graph.DFS()
    elif(search == "UCS"):
        graph.UCS()
    else:
        print("Search not listed")

main()