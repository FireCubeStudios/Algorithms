from Node import Node

class RedBlackTree:
    def __init__(self):
        self.root = None

    # Find an item in the search tree
    def find(self, key):
        node = self.root
        while(node is not None):
            if(key < node.key): node = node.left
            elif(key > node.key): node = node.right
            else: return node.value
        return None

    # Add an item to the search tree
    def add(self, key, value): self.root = self.addRecursive(key, value, self.root)
    def addRecursive(self, key, value, node: Node):
        if(node is None): return Node(key, value)
        else:
            if(key < node.key): node.left = self.addRecursive(key, value, node.left)
            elif(key > node.key): node.right = self.addRecursive(key, value, node.right)
            else: node.value = value
            return node

    # Find the nearest item above the specified key
    def ceiling(self, key): 
        node = self.find(key)
        return node if(node is not None) else self.ceilingRecursive(key, self.root) 
    def ceilingRecursive(self, key, node: Node):
        if(node.left is None and node.right is None): return node.value if(key < node.key) else None
        elif(node.left is not None):
            if(key < node.left.key): return self.ceilingRecursive(key, node.left)
        elif(node.right is not None):
            if(key > node.right.key and key > node.key): return self.ceilingRecursive(key, node.right)
            elif(key < node.right.key and key > node.key): return node.right.value
        else: return None

    def count(self, minKey, maxKey):
        # if left key higher than min then go to it 
        # if right key lower than max then go to it
        # increase count by 1
        return

