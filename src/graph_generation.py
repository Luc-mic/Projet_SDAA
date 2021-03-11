from graph import UndirectedGraph
from random import choice
from random import randint
from random import seed

seed()

# an undirected connected graph of n vertices must have between n-1 (to be connected)
# and n(n-1)/2 (number of edges in a complete unoriented graph)

def generate_random_weight(n_vertices, n_edges):
    return randint(0, n_edges)

def generate_connected_graph(n_vertices, n_edges):

    edges = {i:{} for i in range(n_vertices)}
    
    unconnected_vertices = [i for i in range(1, n_vertices)]
    connected_vertices = [0]

    while unconnected_vertices:
        connected_vertex = choice(connected_vertices)
        unconnected_vertex = choice(unconnected_vertices)

        connected_vertices.append(unconnected_vertex)
        unconnected_vertices.remove(unconnected_vertex)

        wheight = generate_random_weight(n_vertices, n_edges)

        edges[connected_vertex][unconnected_vertex] = wheight
        edges[unconnected_vertex][connected_vertex] = wheight

    return UndirectedGraph(edges)

def generate_random_graph(n_vertices, n_edges):
    assert n_edges >= n_vertices - 1, "Not enough edges to be connected !"
    assert n_edges <= n_vertices * (n_vertices - 1) / 2, "Too many edges !"

    random_graph = generate_connected_graph(n_vertices, n_edges)

    for i in range(n_edges - (n_vertices - 1)):

        other_vertices = []

        while other_vertices == []:

            vertex1 = choice(list(random_graph.vertices))

            other_vertices = list(random_graph.vertices)
            other_vertices.remove(vertex1)
            for neighboor in random_graph.edges[vertex1].keys():
                other_vertices.remove(neighboor)
                
        vertex2 = choice(other_vertices)

        random_graph.add_edge(vertex1, vertex2, generate_random_weight(n_vertices, n_edges))

    return random_graph
    
    
