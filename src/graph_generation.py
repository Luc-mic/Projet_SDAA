from src.graph import UndirectedGraph
from src.graph import DirectedGraph
from random import choice
from random import randint
from random import random
from random import seed


seed()

# an undirected connected graph of n vertices must have between n-1 (to be connected)
# and n(n-1)/2 (number of edges in a complete unoriented graph)


# a directed connected graph of n vertices must have between n-1 (to be connected)
# and n(n-1) (number of edges in a complete unoriented graph)


def generate_random_weight(n_vertices):
    return randint(0, n_vertices * 2)


def generate_connected_graph(n_vertices, directed=False):

    edges = {i: {} for i in range(n_vertices)}

    unconnected_vertices = [i for i in range(1, n_vertices)]
    connected_vertices = [0]

    while unconnected_vertices:
        connected_vertex = choice(connected_vertices)
        unconnected_vertex = choice(unconnected_vertices)

        connected_vertices.append(unconnected_vertex)
        unconnected_vertices.remove(unconnected_vertex)

        wheight = generate_random_weight(n_vertices)

        edges[connected_vertex][unconnected_vertex] = wheight

        if not directed:
            edges[unconnected_vertex][connected_vertex] = wheight

    if not directed:
        return UndirectedGraph(edges)
    
    if directed:
        return DirectedGraph(edges)


def generate_random_graph(n_vertices, n_edges, directed=False):
    assert n_edges >= n_vertices - 1, "Not enough edges to be connected !"
    if not directed:
        assert n_edges <= n_vertices * (n_vertices - 1) / 2, "Too many edges !"
    if directed:
        assert n_edges <= n_vertices * (n_vertices - 1), "Too many edges !"

    random_graph = generate_connected_graph(n_vertices, directed)

    for i in range(n_edges - (n_vertices - 1)):

        # The available list helps when the graph start to be filled with edges
        available = []

        for vertex in random_graph:
            if len(random_graph.edges[vertex]) != n_vertices - 1:
                available.append(vertex)

        other_vertices = []

        while other_vertices == []:

            vertex1 = choice(available)

            other_vertices = list(set(random_graph.vertices) -
                                  set(random_graph.edges[vertex1].keys()) -
                                  set([vertex1]))

        vertex2 = choice(other_vertices)

        random_graph.add_edge(vertex1, vertex2, generate_random_weight(n_vertices))

    return random_graph


def generate_random_community_graph(nodes_per_community, p_intra, p_inter):

    assert p_intra >= 0 and p_intra <= 1, "Invalid p_intra !"
    assert p_inter >= 0 and p_inter <= 1, "Invalid p_inter !"

    n_vertices = sum(nodes_per_community)
    graph = UndirectedGraph({i: {} for i in range(n_vertices)})

    communities = []
    increment = 0
    for community in nodes_per_community:
        communities.append([])
        for i in range(community):
            communities[-1].append(increment)
            increment += 1

    for community1 in communities:
        for vertex1 in community1:
            for vertex2 in community1[community1.index(vertex1) + 1:]:
                if random() < p_intra:
                    graph.add_edge(
                        vertex1, vertex2, generate_random_weight(n_vertices))

            for community2 in communities[communities.index(community1) + 1:]:
                for vertex2 in community2:
                    if random() < p_inter:
                        graph.add_edge(vertex1, vertex2, generate_random_weight(n_vertices))

    return graph
