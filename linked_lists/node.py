
class Node:
    """
    Implements a Node object that may be used in a Stack, Queue, or singly LinkedList.
    """
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_
