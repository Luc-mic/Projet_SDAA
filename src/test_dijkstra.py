from src.graph import DirectedGraph
from src.graph import UndirectedGraph
from src.graph_generation import generate_connected_graph
from src.graph_generation import generate_random_graph
from time import time

def test_dijkstra_classique():
    print("   Tests Dijkstra classique")

    graph = DirectedGraph()
    graph.reset()
    graph.add_vertex(1)
    graph.add_edge(1, 2, 10)
    graph.add_edge(2, 1, 20)
    graph.add_edge(2, 3, 30)

    print(graph.dijkstra_classique(1)) # affiche {1: (0, None), 2: (10, 1), 3: (40, 2)}
    print(graph.dijkstra_classique(3)) # affiche {1: (inf, None), 2: (inf, None), 3: (0, None)}


def test_dijkstra_heap():
    print("   Tests Dijkstra heap")

    graph = DirectedGraph()
    graph.reset()
    graph.add_vertex(1)
    graph.add_edge(1, 2, 10)
    graph.add_edge(2, 1, 20)
    graph.add_edge(2, 3, 30)

    print(graph.dijkstra_heap(1)) # affiche {1: (0, None), 2: (10, 1), 3: (40, 2)}
    print(graph.dijkstra_heap(3)) # affiche {1: (inf, None), 2: (inf, None), 3: (0, None)}


def test_dijkstra_comparatif():

    print("   Tests Dijkstra comparatif")

    """graph = generate_connected_graph(10000, 80000)
    print("graph genere")

    initial_time = time()

    res_dijkstra_classique = graph.dijkstra_classique(0)

    print("Dijkstra classique : " + str(time() - initial_time) + "s.")
    initial_time = time()

    res_dijkstra_heap = graph.dijkstra_heap(0)

    print("Dijkstra heap : " + str(time() - initial_time) + "s.")"""

    for i in range(50):
        graph1 = generate_random_graph(50, 1000, True)

        res_dijkstra_classique = graph1.dijkstra_classique(0)
        res_dijkstra_heap = graph1.dijkstra_heap(0)

        assert [res_dijkstra_classique[i][0] for i in range(len(res_dijkstra_classique))] == [res_dijkstra_heap[i][0] for i in range(len(res_dijkstra_heap))], "Djikstra classique != Dijkstra heap directed graph \n" + str(res_dijkstra_classique) + "\n" + str(res_dijkstra_heap) + "\n" + str(graph1)

    print("Test 1 : Ok : Djikstra classique == Dijkstra heap for directed graph")

    for i in range(100):
        graph2 = generate_random_graph(5, 10, False)

        res_dijkstra_classique = graph2.dijkstra_classique(0)
        res_dijkstra_heap = graph2.dijkstra_heap(0)

        assert res_dijkstra_classique == res_dijkstra_heap, "Djikstra classique != Dijkstra heap undirected graph \n" + str(res_dijkstra_classique) + "\n" + str(res_dijkstra_heap)

    print("Test 2 : Ok : Djikstra classique == Dijkstra heap undirected graph")


def test_dijkstra_aimed():
    print("   Tests Dijkstra aimed")

    graph = DirectedGraph()
    graph.reset()
    graph.add_vertex(1)
    graph.add_edge(1, 2, 10)
    graph.add_edge(2, 1, 20)
    graph.add_edge(2, 3, 30)

    print(graph.dijkstra_aimed(1, 2))
    print(graph.dijkstra_aimed(1, 3))


def test_bellman_ford():
    graph = DirectedGraph()
    graph.bellman_ford(0)

def test_dijkstra():
    print("\nTests Dijkstra")
    test_dijkstra_classique()
    test_dijkstra_heap()
    test_dijkstra_comparatif()
    test_dijkstra_aimed()
    test_bellman_ford()
