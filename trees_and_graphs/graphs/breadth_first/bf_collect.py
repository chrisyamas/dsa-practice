from trees_and_graphs.graphs.vertex_undirected_unweighted import Vertex
from stacks_and_queues.queues.queue import Queue


def bf_collect(vertex, visited=set()):
    """
    A breadth-first search that collects the values of all vertices into
    a set, and returns that set of values.
    """
    visited.add(vertex.value)
    queue = Queue()
    queue.enqueue(vertex)
    while queue.read():
        current = queue.dequeue()
        for adjacent in current.adjacents:
            if adjacent.value not in visited:
                visited.add(adjacent.value)
                queue.enqueue(adjacent)
    return visited


