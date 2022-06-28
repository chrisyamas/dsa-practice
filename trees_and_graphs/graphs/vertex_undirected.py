

class Vertex:
    """
    Implements an UNDIRECTED graph
    """

    def __init__(self, value):
        self.value = value
        self.adjacents = set()
    
    def add_adjacent(self, vertex):
        if vertex in self.adjacents:
            return
        self.adjacents.add(vertex)
        vertex.add_adjacent(self)