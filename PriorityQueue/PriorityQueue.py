class PriorityQueue:
    def __init__(self):
        self.tree = [0]
        self.items = []

    # Swap [i] with [ii]
    def Swap(self, i, ii):
        temp = self.tree[i]
        self.tree[i] = self.tree[ii]
        self.tree[ii] = temp
    
    # Swim the item in the index up the tree
    def SwimUp(self, index: int):
        if(index == 1 or index == 0): return # Root item or invalid
        if(self.tree[index // 2].value < self.tree[index].value):
            self.Swap(index // 2, index)
            self.SwimUp(index // 2)
    
    # Swim the item in the index down the tree
    def SwimDown(self, index: int):
        if(index == 0 and index > (len(self.tree) - 1)): return # Leaf item or Invalid
        if(index * 2 <= len(self.tree) - 1):
            if(self.tree[index * 2].value > self.tree[index].value):
                self.Swap(index, index * 2)
                self.SwimDown(index * 2)
                self.SwimDown(index)
                return
        elif((index * 2) + 1 <= len(self.tree) - 1):
            if(self.tree[(index * 2) + 1].value > self.tree[index].value):
                self.Swap(index, (index * 2) + 1)
                self.SwimDown((index * 2) + 1)
                self.SwimDown(index)
                return

    # Add an item to the queue
    def Add(self, item):
        self.tree.append(item) 
        self.items.append(item)
        self.SwimUp(len(self.tree) - 1)
