from linked_lists.node import Node


class Stack:
    """
    Implements a node-based stack.
    """
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        self.size += 1
        new_node = Node(value, self.top)
        self.top = new_node

    def pop(self):
        if not self.top:
            raise Exception("Cannot perform operation on empty stack.")
        else:
            self.size -= 1
            top_node = self.top
            self.top = self.top.next
            return top_node.value

    def peek(self):
        return self.top.value

    def is_empty(self):
        return self.size == 0


