from graph_generation import generate_connected_graph
from graph_generation import generate_random_graph


def test_connected_graph():
    print("Test generate_connected_graph")

    for i in range(10):
        graph = generate_connected_graph(100, 100)
        assert len(graph) == 100, "One of the graphs doesn't have the right number of vertices : \n" + str(graph)

    print("Test 1 : Ok : All graphs have the right number of vertices")

    for i in range(10):
        graph = generate_connected_graph(100, 100)
        assert graph.is_connected() == True, "One of the graphs isn't connected : \n" + str(graph)

    print("Test 2 : Ok : All graphs are connected")

def test_random_graph():
    print("Test generate_random_graph")

    #Vérifie le nombre sommets

    for i in range(10):
        graph = generate_random_graph(100, 100)
        assert len(graph) == 100, "One of the graphs doesn't have the right number of vertices : \n" + str(graph)

    print("Test 1 : Ok : All graphs have the right number of vertices")

    #Vérifie le nombre d'edges pour des graphes quelconques

    for i in range(10):
        graph = generate_random_graph(100, 100)
        edges = 0
        for vertex in graph:
            edges += len(graph.edges[vertex].keys())
        edges = edges / 2

        assert edges == 100, "One of the graphs doesn't have the right number of edges : " + str(edges) +  "for : \n" + str(graph)

    #Vérifie que que l'erreur surgit lorsque edges < vertices - 1
    #graph = generate_random_graph(100, 98)
    
    # Vérifie le cas limite edges = verices - 1
    graph = generate_random_graph(100, 99)
    edges = 0
    for vertex in graph:
        edges += len(graph.edges[vertex].keys())
    edges = edges / 2

    assert edges == 99, "One of the graphs doesn't have the right number of edges : " + str(edges) +  "for : \n" + str(graph)
    
    #Vérifie que que l'erreur surgit lorsque edges > vertices * (vertices - 1) / 2
    #graph = generate_random_graph(100, 4951)

    # Vérifie le cas limite edges = vertices * (vertices - 1) / 2

    graph = generate_random_graph(100, 4950)
    edges = 0
    for vertex in graph:
        edges += len(graph.edges[vertex].keys())
    edges = edges / 2

    assert edges == 4950, "One of the graphs doesn't have the right number of edges : " + str(edges) +  "for : \n" + str(graph)

    print("Test 2 : Ok : All graphs have the right number of edges")


test_connected_graph()
test_random_graph()
