from trees_and_graphs.graphs.vertex_undirected_unweighted import Vertex
from stacks_and_queues.queues.queue import Queue


# Algorithm could be modified to return boolean value instead of node.
# Simply return True if current_value == search_value in while loop,
# and otherwise return False after while loop completes
def bf_search(vertex, search_value, visited=set()):
    """
    Function traverses a graph breadth-first to find the vertex holding the
    given search_value. If such a vertex is not connected, directly or
    indirectly, to the given starting vertex, the function will return None.

    Params
    ------
    :vertex: Vertex-type object that will serve as starting point for search
    :search_value: value, potentially of any type, being sought in graph
    :visited: optional; default is empty set to be filled with vertex values

    Return
    ------
    either vertex in graph holding search_value, or None
    """
    visited.add(vertex.value)
    queue = Queue()
    queue.enqueue(vertex)

    while queue.read():
        current = queue.dequeue()
        if current.value == search_value:
            return current
        for adjacent in current.adjacents:
            if adjacent.value not in visited:
                visited.add(adjacent.value)
                queue.enqueue(adjacent)
    return None

