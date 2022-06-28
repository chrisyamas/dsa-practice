
def depth_first_collect(vertex, visited_vertices=set()):
    # Mark vertex as visited by adding it to the set:
    visited_vertices.add(vertex.value)
    # Optional: print vertex's value to confirm algorithm working
    print(vertex.value)
    # Iterate through the current vertex's adjacent vertices:
    for adjacent_vertex in vertex.adjacent_vertices:
        # If adjacent vertex hasn't been visited,
        # recursively call this method on it
        if adjacent_vertex.value not in visited_vertices:
            depth_first_collect(adjacent_vertex, visited_vertices)
    # After loop and recursive calls have completed, return collection
    return visited_vertices