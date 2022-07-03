
def df_search(vertex, search_value, visited_vertices=set()):
    # Return the original vertex if it happens to
    # be the one we're searching for:
    if vertex.value == search_value:
        return vertex

    visited_vertices.add(vertex.value)

    for adjacent_vertex in vertex.adjacent_vertices:
        if adjacent_vertex.value not in visited_vertices:
            # If the adjacent vertex is the vertex we're searching for,
            # just return that vertex:
            if adjacent_vertex.value == search_value:
                return adjacent_vertex
            # Attempt to find the vertex we're searching for by recursively
            # calling this method on the adjacent vertex:
            sought_vertex = df_search(adjacent_vertex, search_value, visited_vertices)
            # If we were able to find the correct vertex using the above dynamic_programming,
            # return the correct vertex:
            if sought_vertex:
                return sought_vertex
            # If we haven't found the vertex we're searching for:
            return None
        