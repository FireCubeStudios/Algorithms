class Node:
    def __init__(self, key, value, isRed = False):
        self.key = key
        self.value = value
        self.Red = isRed
        self.left = None
        self.right = None
        self.root = None

    def isRed(self) -> bool:
        if(self.right is None or self.left is None): return False
        else: return self.Red