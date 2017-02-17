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
    path = list()
    parent = -1
    nodes_plain = list()
    name = 0

    def __init__(self):
        self.nodes = list()
        self.path = list()

    def updateName(self, name):
        self.name = name

    def insertPlain(self, name):
        self.nodes_plain.append(name)

    def isChild(self, child):
        for i in self.nodes:
            if self.nodes[i].getName() == child:
                return True
        return False

    def retPlain(self):
        kids = list()
        for i in self.nodes:
            kids.append(int(i.getName()))
        return kids

    def addNode(self, node):
        self.nodes.append(node)

    def getNodes(self):
        return self.nodes

    def updatePath(self, path):
        self.path.append(path)

    def updateParent(self, parent):
        self.parent = parent
    def getParent(self):
        return self.parent

    def getChildren(self):
        return self.nodes

    def getPath(self):
        return self.path

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
    children = list()
    parent = None
    marked = False
    short_path = list()

    def __init__(self, name, weight, parent):
        self.name = name
        self.weight = weight
        self.parent = parent
        self.marked = False
        self.short_path = list()

    def addToPath(self, name):
        self.short_path.append(name)

    def getParentNode(self):
        return self.parent_node

    def getPath(self):
        return self.short_path

    def seen(self):
        self.marked = True

    def wasSeen(self):
        return not self.marked

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
    nodes = []
    lastParent = None

    #Constructor
    def __init__(self, start, end):
        self.queue = list()
        self.stack = list()
        self.graph = {}
        self.visited = list()
        self.start = start
        self.end = end
        self.nodes = [None] * (50)

    def backTrace(self):
        b_queue = list()
        patho = list()

        for i in self.nodes:
            if i != None:
                print(i.getPath())

        while self.visited:
            b_queue.append(self.visited.pop(-1))
        #print(b_queue)
        val = b_queue.pop(0)

        while b_queue:

            val = b_queue.pop(0)


        print(patho)




    #Adds new node to graph
    #Preconditions: pos, dest, weight all integers
    #Postconditions: node is added to graph
    #@pos : position of self node
    #@dest : node to point to from current node
    #@weight : the cost to move from this node to the next
    def addNode(self, name, weight, parent):
        #Creates nodes in dictionary if it doesn't exist
        if(self.nodes[parent] == None):
            self.nodes[parent] = Nodes()
            self.nodes[parent].updateParent(parent)
        self.nodes[parent].addNode(Node(name, weight, parent))
        self.nodes[parent].insertPlain(name)


    #Breadth-First-search
    def BFS(self):
        stack = list()
        self.queue = list()
        paths = [[]] * 50
        #If start is the same as end, return
        if(self.start == self.end):
            print(list())
            return

        self.queue.append(int(self.start))
        prior = 0
        while self.queue:
            tmp = self.queue.pop(0)
            self.nodes[tmp].updatePath(tmp)
            if self.nodes[tmp] != None:
                for node in self.nodes[tmp].getChildren():
                    #if node wasn't seen go in
                    
                    if tmp not in self.visited:
                        self.visited.append(tmp)

                    if node.wasSeen():
                        self.queue.append(node.getName())
                        node.seen()

                    if node.getName() == int(self.end):
                        self.visited.append(node.getName())
                        self.backTrace()
                        return True
            prior = tmp

        #print(path)
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

    start = 15
    end = 5
    #For Hard BFS

    graph = Graph(int(start), int(end))
    #splits lines then adds the nodes to a graph
    for line in file:
        items = line.split()
        #name, weight, parent
        graph.addNode(int(items[1]), int(items[2]), int(items[0]))

    #For BFS and DFS dont need to include weights
    #put path to get to that current node, in the node themselves.
    #Search method passed in via CMD line
    if(search == "BFS"):
        if not graph.BFS():
            print([])
    elif(search == "DFS"):
        graph.DFS()
    elif(search == "UCS"):
        graph.UCS()
    else:
        print("Search not listed")

main()