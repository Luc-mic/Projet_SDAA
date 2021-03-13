from src.graph_generation import generate_connected_graph
from src.graph_generation import generate_random_graph
from src.graph_generation import generate_random_community_graph
from math import sqrt
from random import randint
from random import random


def test_connected_undirected_graph():
    print("   Test generate_connected_graph")

    for i in range(10):
        graph = generate_connected_graph(100, 100, False)
        assert len(
            graph) == 100, "One of the graphs doesn't have the right number of vertices : \n" + str(graph)

    print("Test 1 : Ok : All graphs have the right number of vertices")

    for i in range(10):
        graph = generate_connected_graph(100, 100, False)
        assert graph.is_connected(), "One of the graphs isn't connected : \n" + str(graph)

    print("Test 2 : Ok : All graphs are connected")


def test_random_undirected_graph():
    print("   Test generate_random_graph")

    # Vérifie le nombre sommets

    for i in range(10):
        graph = generate_random_graph(100, 100, False)
        assert len(
            graph) == 100, "One of the graphs doesn't have the right number of vertices : \n" + str(graph)

    print("Test 1 : Ok : All graphs have the right number of vertices")

    # Vérifie le nombre d'edges pour des graphes quelconques

    for i in range(10):
        graph = generate_random_graph(100, 100, False)
        edges = 0
        for vertex in graph:
            edges += len(graph.edges[vertex].keys())
        edges = edges / 2

        assert edges == 100, "One of the graphs doesn't have the right number of edges : " + \
            str(edges) + "for : \n" + str(graph)

    # Vérifie que que l'erreur surgit lorsque edges < vertices - 1
    #graph = generate_random_graph(100, 98)

    # Vérifie le cas limite edges = verices - 1
    graph = generate_random_graph(100, 99, False)
    edges = 0
    for vertex in graph:
        edges += len(graph.edges[vertex].keys())
    edges = edges / 2

    assert edges == 99, "One of the graphs doesn't have the right number of edges : " + \
        str(edges) + "for : \n" + str(graph)

    # Vérifie que que l'erreur surgit lorsque edges > vertices * (vertices - 1) / 2
    #graph = generate_random_graph(100, 4951)

    # Vérifie le cas limite edges = vertices * (vertices - 1) / 2

    graph = generate_random_graph(100, 4950, False)
    edges = 0
    for vertex in graph:
        edges += len(graph.edges[vertex].keys())
    edges = edges / 2

    assert edges == 4950, "One of the graphs doesn't have the right number of edges : " + \
        str(edges) + "for : \n" + str(graph)

    print("Test 2 : Ok : All graphs have the right number of edges")


def test_connected_directed_graph():
    print("   Test generate_connected_graph")

    for i in range(10):
        graph = generate_connected_graph(100, 100, True)
        assert len(
            graph) == 100, "One of the graphs doesn't have the right number of vertices : \n" + str(graph)

    print("Test 1 : Ok : All graphs have the right number of vertices")

    for i in range(10):
        graph = generate_connected_graph(100, 100, True)
        # erreur too many positional arguments du linter, mais le code passe
        # quand même
        unconnected_induced_graph = graph.induced_graph(graph.vertices, False)
        assert unconnected_induced_graph.is_connected(
        ), "One of the graphs isn't connected : \n" + str(graph)

    print("Test 2 : Ok : All graphs are connected")


def test_random_directed_graph():
    print("   Test generate_random_graph")

    # Vérifie le nombre sommets

    for i in range(10):
        graph = generate_random_graph(100, 100, True)
        assert len(
            graph) == 100, "One of the graphs doesn't have the right number of vertices : \n" + str(graph)

    print("Test 1 : Ok : All graphs have the right number of vertices")

    # Vérifie le nombre d'edges pour des graphes quelconques

    for i in range(10):
        graph = generate_random_graph(100, 100, True)
        edges = 0
        for vertex in graph:
            edges += len(graph.edges[vertex].keys())

        assert edges == 100, "One of the graphs doesn't have the right number of edges : " + \
            str(edges) + "for : \n" + str(graph)

    # Vérifie que que l'erreur surgit lorsque edges < vertices - 1
    #graph = generate_random_graph(100, 98)

    # Vérifie le cas limite edges = verices - 1
    graph = generate_random_graph(100, 99, True)
    edges = 0
    for vertex in graph:
        edges += len(graph.edges[vertex].keys())

    assert edges == 99, "One of the graphs doesn't have the right number of edges : " + \
        str(edges) + "for : \n" + str(graph)

    # Vérifie que que l'erreur surgit lorsque edges > vertices * (vertices - 1) / 2
    #graph = generate_random_graph(100, 9901)

    # Vérifie le cas limite edges = vertices * (vertices - 1) / 2

    graph = generate_random_graph(100, 9900, True)
    edges = 0
    for vertex in graph:
        edges += len(graph.edges[vertex].keys())

    assert edges == 9900, "One of the graphs doesn't have the right number of edges : " + \
        str(edges) + "for : \n" + str(graph)

    print("Test 2 : Ok : All graphs have the right number of edges")


def test_random_community_graph():
    for i in range(10):
        graph1 = generate_random_community_graph([5 * i, 3 * i, 4 * i], 1, 1)
        assert graph1.is_complete(), "Graph proba 1, 1 not complete"
        assert len(graph1.vertices) == sum(
            [5 * i, 3 * i, 4 * i]), "Graph doesn't have the right number of edges\n" + str(graph1)
    print("Test1 : Ok : All graphs with prob (1, 1) are complete and have the right number of edges")

    graph2 = generate_random_community_graph([5, 3, 4], 0, 0)
    for vertex in graph2:
        assert not graph2[vertex].keys()

    print("Test2 : Ok : Graphs with prob (0, 0) has no edges")

    nodes_per_community = [randint(25, 50) for i in range(100)]
    p_intra = random()
    p_inter = random()

    graph = generate_random_community_graph(
        nodes_per_community, p_intra, p_inter)

    communities = []
    increment = 0
    for community in nodes_per_community:
        communities.append([])
        for i in range(community):
            communities[-1].append(increment)
            increment += 1

    # number of community whose number of edges is within intra_trust interval
    solid_community = 0
    # number of community whose number of edges is within inter_trust interval
    successful_community = 0

    for community in communities:

        intra_trust_min = len(community) * (len(community) - 1) / 2 * p_intra - 1.96 * sqrt(
            len(community) * (len(community) - 1) / 2 * p_intra * (1 - p_intra))
        intra_trust_sup = len(community) * (len(community) - 1) / 2 * p_intra + 1.96 * sqrt(
            len(community) * (len(community) - 1) / 2 * p_intra * (1 - p_intra))

        inter_trust_min = len(community) * (len(graph.vertices) - len(community)) * p_inter - 1.96 * sqrt(
            len(community) * (len(graph.vertices) - len(community)) * p_inter * (1 - p_inter))
        inter_trust_sup = len(community) * (len(graph.vertices) - len(community)) * p_inter + 1.96 * sqrt(
            len(community) * (len(graph.vertices) - len(community)) * p_inter * (1 - p_inter))

        intra_community_edge = 0
        inter_community_edge = 0

        for vertex in community:
            for other in graph[vertex].keys():
                if other in community:
                    intra_community_edge += 1
                else:
                    inter_community_edge += 1

        intra_community_edge = intra_community_edge // 2
        if intra_community_edge >= intra_trust_min and intra_community_edge <= intra_trust_sup:
            solid_community += 1
        if inter_community_edge >= inter_trust_min and inter_community_edge <= inter_trust_sup:
            successful_community += 1
    print(
        "Test 3.1 : " +
        str(solid_community) +
        " of 100 communities are solid")
    print(
        "Test 3.2 : " +
        str(successful_community) +
        " of 100 communities are successful")


def test_graph_generation():

    print("Tests undirected graphs : ")
    test_connected_undirected_graph()
    test_random_undirected_graph()

    print("\nTests directed graphs : ")
    test_connected_directed_graph()
    test_random_directed_graph()

    print("\nTests community graphs : ")
    test_random_community_graph()
