from Node import Node

# Implementing my own disjoint set for learning purposes
class DisjointSet:
    def __init__(self, setsCount):
        self.nodes = {} # Maintain dictionary to map int to node
        for x in range(setsCount):
            self.nodes[x] = Node(x)

    # Recursively traverse up a node to get it's top level parent
    def traverse(self, node: Node):
        if(node.parent is None): return node
        else: return self.traverse(node.parent)

    # return 0 if val1 and val2 are in the same set otherwise 1
    def query(self, val1: int, val2: int):
        if val1 == val2: return 1
        node1 = self.nodes.get(val1)
        node2 = self.nodes.get(val2)
        return 1 if self.traverse(node1).value == self.traverse(node2).value else 0

    # Merge 2 sets
    def union(self, val1: int, val2: int): 
        if val1 == val2: return
        if self.query(val1, val2) == 1: return
        node1 = self.nodes.get(val1)
        node2 = self.nodes.get(val2)
        parent1 = self.traverse(node1)
        parent2 = self.traverse(node2)
        parent2.parent = parent1
        parent1.children.append(parent2)
        return

    # move val1 from it's set into the set of val2
    def union(self, val1: int, val2: int): 
        if val1 == val2: return
        if self.query(val1, val2) == 1: return
        node1 = self.nodes.get(val1)
        node2 = self.nodes.get(val2)
        parent1 = self.traverse(node1)
        parent2 = self.traverse(node2)
        parent2.parent = parent1
        parent1.children.append(parent2)
        return

    # move val1 from it's set into the set of val2
    def move(self, val1: int, val2: int):
        if val1 == val2: return
        if self.query(val1, val2) == 1: return
        node1 = self.nodes.get(val1)
        node2 = self.nodes.get(val2)

        if(node1.parent is not None): # not root node
            for child in node1.children:
                child.parent = node1.parent
                node1.parent.children.append(child)
        elif(len(node1.children) > 1): # root node with more than one child
            root = node1.children[0] # set the new root of the set
            root.parent = None
            for i in range(1, len(node1.children)):
                child = node1.children[i]
                child.parent = root
                root.children.append(child)
        else: 
            for child in node1.children: child.parent = None

        parent = self.traverse(node2)
        node1.children.clear()
        node1.parent = parent
        parent.children.append(node1)
        return