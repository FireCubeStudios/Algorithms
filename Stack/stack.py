from Node import Node

# Implementing my own stack for learning purposes
class StackEmptyError(Exception): pass

class Stack:
    def __init__(self):
        self.pointer = None

    # Push an item into the stack
    def push(self, item):
        node = Node(item, self.pointer)
        self.pointer = node
        return 
    
    # Pop an item from the stack
    def pop(self):
        if(self.pointer is None):
            raise StackEmptyError("Stack is empty")
        node = self.pointer
        self.pointer = node.pointer
        return node.value
    
    def isEmpty(self) -> bool:
        return self.pointer is None