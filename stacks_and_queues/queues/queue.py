from linked_lists.node import Node


class Queue:

    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    def enqueue(self, value):
        new_node = Node(value)
        self.size += 1
        if not self.front:
            self.front = new_node
            self.back = new_node
        else:
            self.back.next = new_node

    def dequeue(self):
        if not self.front:
            raise Exception("Cannot perform operation on empty queue.")
        else:
            self.size -= 1
            front_node = self.front
            self.front = self.front.next
            if self.size == 0:
                self.back = None
            return front_node.value

    def read(self):
        return self.front

    def is_empty(self):
        return self.size == 0


