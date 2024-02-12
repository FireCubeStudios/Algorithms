class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None

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
        return

    # move val1 from it's set into the set of val2
    def move(self, val1: int, val2: int): # TRY TO MAKE A VERSION WHERE ONLY UPDATE PARENTS
        if val1 == val2: return
        if self.query(val1, val2) == 1: return
        node1 = self.nodes.get(val1)
        node2 = self.nodes.get(val2)
        parent = self.traverse(node2)
        node1.parent = parent

        # code to enumerate any nodes which connect to val1 and update them to point to val1 old parent
        # if val1 had no parent then update them to point to a random new root
        return
    
setsCount, linesCount = map(int, input().split())

Set = DisjointSet(setsCount)

# Read following lines
for _ in range(linesCount):
    operation, set1, set2 = map(int, input().split())
    if operation == 0:
        print(Set.query(set1, set2))
    elif operation == 1:
        Set.union(set1, set2)
    elif operation == 2:
        Set.move(set1, set2)
