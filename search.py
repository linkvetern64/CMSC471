#Author: Joshua Standiford
#Date:2/8/2017
#Desc: This program will simulate the Breadth-First-Search, Depth-First-Search, Uniform Cost Search
#Algorithms.

#--- Import Statements ---
import sys


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
        queue = list()
        stack = list()
        graph = {}
        visited = list()
        self.start = start
        self.end = end
        self.queue.append(int(self.start))

    # _ denotes private internal class.
    class _Node:

        children = list()
        weight = 0
        name = ""

        def __init__(self, name, weight):
            children = list()
            self.name = name
            self.weight = weight
            children.append("Child")

        def getChildren(self):
            for child in self.children:
                print(child)

    #Prints all items and their edges in the graph
    def printGraph(self):
        for node in self.graph.items():
            print(node)

    #Adds new node to graph
    #Preconditions: pos, dest, weight all integers
    #Postconditions: node is added to graph
    #@pos : position of self node
    #@dest : node to point to from current node
    #@weight : the cost to move from this node to the next
    def addNode(self, pos, dest, weight):
        self.graph.update({pos : [dest , weight]})

    #Breadth-First-search
    def BFS(self):

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

    graph = Graph(start, end)

    #splits lines then adds the nodes to a graph
    for line in file:
        items = line.split()
        graph.addNode(items[0], items[1], items[2])

    #Search method passed in via CMD line
    if(search == "BFS"):
        graph.BFS()
    elif(search == "DFS"):
        graph.DFS()
    elif(search == "UCS"):
        graph.UCS()
    else:
        print("Search not listed")
    #graph.printGraph()


main()