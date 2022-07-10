from trees_and_graphs.graphs.vertex_undirected_unweighted import Vertex


def df_bool(vertex, search_value, visited=set()):
    print("function called")
    if vertex.value == search_value:
        return True
    
    visited.add(vertex.value)

    for adjacent in vertex.adjacents:
        if adjacent.value not in visited:
            # this line isn't necessary, but it prevents one last recursive function call
            if adjacent.value == search_value:
                return True
            vertex_found = df_bool(adjacent, search_value, visited)
            if vertex_found:
                return True
            return False


if __name__ == '__main__':
    apple = Vertex("apple")
    banana = Vertex("banana")
    carrot = Vertex("carrot")
    durian = Vertex("durian")

    apple.add_adjacent(banana)
    banana.add_adjacent(carrot)
    carrot.add_adjacent(durian)

    result = df_bool(apple, "durian")
    print(result)
