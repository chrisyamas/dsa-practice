from stacks_and_queues.queues.queue import Queue
from tree_node import TreeNode


def bfs(root, search_value):
    queue = Queue()
    queue.enqueue(root)
    while queue.read():
        current = queue.dequeue()
        if current.value == search_value:
            return current
        for child in current.left, current.right:
            if child:
                queue.enqueue(child)
    return None
