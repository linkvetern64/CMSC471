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
    # Add start to queue and set weight = to 0
    self.queue.append(int(self.start))
    self.nodes[self.start].setWeight(0)

    tmp = int(self.start)
    self.visited.append(tmp)
    self.priority.append((tmp, self.nodes[tmp].getWeight()))
    tmp = self.priority[0]

    # while the next queue has spots
    while self.priority:
        if self.nodes[tmp[0]] != None and self.nodes[tmp[0]].hasChildren():
            parent_weight = self.nodes[tmp[0]].getWeight()
            children = self.nodes[tmp[0]].getFatKids()

            # get the children of the parent for evaluation
            for child in children:
                # children to put into priority queue
                # gets weight from parent to child traversal
                child_weight = child.getWeight() + parent_weight

                # if the weight from parent to child is less than current weight
                # set that new weight
                if self.nodes[child.getName()] != None:
                    if child_weight < self.nodes[child.getName()].getWeight():
                        self.nodes[child.getName()].setWeight(child_weight)

                    # add children to priority queue
                    if child.getName() not in self.visited:
                        self.priority.append((child.getName(), child.getWeight()))
                        self.visited.append(child.getName())
                    self.priority.sort(key=lambda tup: tup[1])

        print(self.priority)
        # Get lowest weight first
        tmp = self.priority.pop(0)


main()