def graph_challenge(str_arr):
    """
    Determines if the given set of vertices forms a Hamiltonian path on a graph.

    Args:
        strarr (list): A list of three strings representing vertices, edges, and a path.

    Returns:
        str: Returns 'yes' if a Hamiltonian path exists, otherwise returns the vertex where the path terminates.

    Example:
        graph_challenge(["(A, B, C)", "(B-A, C-B)", "(C, B, A)"])
        Output: 'yes'
    """
    vertices = str_arr[0][1:-1].split(',')
    edges = [edge.split('-') for edge in str_arr[1][1:-1].split(',')]
    path = str_arr[2][1:-1].split(',')

    def is_hamiltonian(path):
        """
        Checks if the given path forms a Hamiltonian path on the graph.

        Args:
            path (list): A list of vertices representing the path.

        Returns:
            str: Returns 'yes' if a Hamiltonian path exists, otherwise returns the vertex where the path terminates.
        """
        visited = set()
        current_vertx = path[0]
        visited.add(current_vertx)

        for next_vertx in path[1:]:
            valid_edge = False
            for edge in edges:
                v1, v2 = edge
                if (v1 == current_vertx and v2 == next_vertx) or (v2 == current_vertx and v1 == next_vertx):
                    valid_edge = True
                    break
            if not valid_edge or next_vertx in visited:
                return current_vertx
            visited.add(next_vertx)
            current_vertx = next_vertx

        return 'yes' if len(visited) == len(vertices) else current_vertx
    #print(path)
    #print(is_hamiltonian(path))
    return is_hamiltonian(path)


# Test cases
# Output: yes
#print(graph_challenge(["(A,B,C)", "(B-A,C-B)", "(C,B,A)"]))
# Output: Q
#print(graph_challenge(["(X,Y,Z,Q)", "(X-Y,Y-Q,Y-Z)", "(Z,Y,Q,X)"]))
