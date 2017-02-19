#Author: Joshua Standiford
#Date:2/8/2017
#Desc: This program will simulate the Breadth-First-Search, Depth-First-Search, Uniform Cost Search
#Algorithms.

#--- Import Statements ---
import sys
import math

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
    weight = math.inf

    def __init__(self):
        self.nodes = list()
        self.path = list()

    def getWeight(self):
        return self.weight

    def setWeight(self, weight):
        self.weight = weight

    def updateName(self, name):
        self.name = name

    def insertPlain(self, name):
        self.nodes_plain.append(name)


    def hasChildren(self):
        return bool(self.nodes)

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
        for i in path:
            self.path.append(i)

    def updateParent(self, parent):
        self.path.append(parent)
        self.parent = parent

    def getParent(self):
        return self.parent

    #Gets next available child, if none available then return -1
    def getChildren(self):
        return self.nodes

    def getFatKids(self):
        for node in self.nodes:
            node.addWeight(self.weight)
        return self.nodes

    def getPath(self):
        return self.path

    def getNextChild(self):

        for child in self.nodes:
            if not child.isMarked():
                self.nodes.remove(child)
                return child.getName()
        return -1

    def getNextChildWeighted(self):
        for child in self.nodes:
            if not child.isMarked():
                self.nodes.remove(child)
                return child.getName()
        return -1

    def removeChild(self):
        self.nodes.pop(0)

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
    heavy = 100000

    def __init__(self, name, weight, parent):
        self.name = name
        self.weight = weight
        self.parent = parent
        self.marked = False
        self.short_path = list()

    def updateHeavy(self, heavy):
        self.heavy = heavy

    def getHeavy(self):
        return self.heavy

    def addWeight(self,weight):
        self.weight = self.weight + weight

    def addToPath(self, name):
        self.short_path.append(name)

    def getParentNode(self):
        return self.parent_node

    def getPath(self):
        return self.short_path

    def seen(self):
        self.marked = True

    def isMarked(self):
        return self.marked

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
    priority = list()

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

        patho.append(self.end)
        while self.visited:
            b_queue.append(self.visited.pop(-1))
        val = b_queue.pop(0)

        val = b_queue.pop(0)
        test = self.nodes[val].getPath()


        while test:

            val = test.pop(0)

            patho.append(int(val))
            if self.start in patho and self.end in patho:
                break
        p = list()
        while patho:
            p.append(patho.pop(-1))
        print(p)

    def playBack(self, queue):
        tmp = list()
        result = list()
        while queue:
            tmp.append(queue.pop(-1))

        while self.start not in result or self.end not in result:
            result.insert(0, tmp.pop(0))
        print(result)


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
        self.queue = list()
        #If start is the same as end, return
        if(self.start == self.end):
            print(list())
            return

        self.queue.append(int(self.start))

        while self.queue:
            tmp = self.queue.pop(0)

            if self.nodes[tmp] != None:
                #node is child of self.nodes[tmp]
                for node in self.nodes[tmp].getChildren():
                    if self.nodes[node.getName()] != None:
                        self.nodes[node.getName()].updatePath(self.nodes[tmp].getPath())
                    #if node wasn't seen go in
                    if tmp not in self.visited:
                        self.visited.append(tmp)

                    if node.wasSeen() and node.getName() not in self.visited:
                        self.queue.append(node.getName())
                        node.seen()

                    if node.getName() == int(self.end):
                        self.visited.append(node.getName())
                        self.backTrace()
                        return True

    #Depth-First-Search
    def DFS(self):
        self.queue = list()
        self.visited = list()
        removed = list()
        # If start is the same as end, return
        if (self.start == self.end):
            print(list())
            return

        self.queue.append(int(self.start))
        tmp = int(self.start)
        self.visited.append(tmp)
        #while the next queue has spots
        while self.queue:
            #getting stuck here
            if self.nodes[tmp] != None and self.nodes[tmp].hasChildren():
                nextChild = self.nodes[tmp].getNextChild()
                if nextChild > 0 and nextChild not in self.visited:
                    tmp = nextChild
                    self.queue.append(nextChild)
                    self.visited.append(nextChild)

                    if nextChild == self.end:
                        break

            else:
                self.queue.pop(-1)
                tmp = self.queue[-1]
                removed.append(tmp)

                #while parent has children, populate queue with children, then mark each node

        print(self.queue)

    #Uniform Cost Search
    def UCS(self):
        self.queue = list()
        self.visited = list()

        # If start is the same as end, return
        if (self.start == self.end):
            print(list())
            return

        tmp = self.start
        self.nodes[self.start].setWeight(0)
        self.queue.append(tmp)
        done = False
        while self.queue:
            if self.nodes[tmp] != None:
                #print(self.queue)

                for child in self.nodes[tmp].getChildren():
                    #print(child.toString())
                    #print("Nodes(" + str(tmp) + "): Weight = " + str(self.nodes[tmp].getWeight()))
                    new_weight = self.nodes[tmp].getWeight() + child.getWeight()
                    if self.nodes[child.getName()] != None:
                        if self.nodes[child.getName()].getWeight() > new_weight:
                            self.nodes[child.getName()].setWeight(new_weight)

                tmp_child = Node(-1, math.inf, -1)
                for child in self.nodes[tmp].getChildren():
                    if child.getName() == self.end:
                        done = True
                        break

                    if self.nodes[child.getName()] != None:
                        if self.nodes[child.getName()].getWeight() < tmp_child.getWeight() and child.wasSeen():
                            tmp_child = child

                if tmp_child.getName() > 0:
                    self.queue.append(tmp_child.getName())
                    tmp_child.seen()
                self.visited.append(self.queue.pop(0))
                if done:
                    self.visited.append(self.end)
                    break
                if self.queue:
                    tmp = self.queue[0]

        self.playBack(self.visited)

#Name: Main
#Preconditions: must have arguments - FILE_NAME START_NODE END_NODE SEARCH_TYPE
#Postconditions:
#Desc: Driver function for search.py
def main():

    #pulls command line arguments
    #sys.argv[1] = "med.txt"
    #sys.argv[1] = "easy.txt"
    file = open(sys.argv[1])
    start = sys.argv[2]
    end = sys.argv[3]
    search = sys.argv[4]

    #hard
    #start = 15
    #end = 5

    #med
    #start = 10
    #end = 1

    #easy
    #start = 1
    #end = 7

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