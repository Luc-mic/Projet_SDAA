from src.graph import UndirectedGraph
from src.graph import DirectedGraph
from copy import copy
from random import choice
from random import randint
from random import random
from random import seed
from random import shuffle


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
    shuffle(unconnected_vertices)
    connected_vertices = [0]

    while unconnected_vertices:
        connected_vertex = choice(connected_vertices)
        unconnected_vertex = unconnected_vertices.pop()

        connected_vertices.append(unconnected_vertex)

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

    free_others = {}  # dict that keep tracks of vertices having no edge with the key vertex
    available = []
    for vertex in random_graph:

        free_others[vertex] = list(
            set(random_graph.vertices) - set([vertex]) - set(random_graph[vertex].keys()))
        if free_others[vertex]:
            available.append(vertex)
        # allows a legit use of pop(), which is faster that remove()
        shuffle(free_others[vertex])

    vertex1 = choice(list(random_graph.vertices))

    for i in range(n_edges - (n_vertices - 1)):

        vertex1 = choice(available)
        vertex2 = free_others[vertex1].pop()

        if not directed:
            # less efficient for undirected graphs
            free_others[vertex2].remove(vertex1)
            if not free_others[vertex2]:
                available.remove(vertex2)
        random_graph.add_edge(
            vertex1,
            vertex2,
            generate_random_weight(n_vertices))

        if not free_others[vertex1]:
            available.remove(vertex1)

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
                        graph.add_edge(
                            vertex1, vertex2, generate_random_weight(n_vertices))

    return graph
