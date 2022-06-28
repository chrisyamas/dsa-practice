
class Vertex:
    """
    Implements a DIRECTED graph
    """
    def __init__(self, value):
        self.value = value
        self.adjacents = set()
    
    def add_adjacent(self, vertex):
        self.adjacents.append(vertex)
