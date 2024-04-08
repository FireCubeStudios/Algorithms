class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.isRed = False
        self.left = None
        self.right = None
        self.root = None