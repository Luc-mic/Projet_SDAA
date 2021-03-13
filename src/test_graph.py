from graph import DirectedGraph
from graph import UndirectedGraph


def test_directed_graph():
    print("Tests DirectedGraph")

    graph = DirectedGraph()
    graph.add_vertex(1)
    graph.add_edge(1, 2, 1)
    graph.add_edge(2, 1, 1)
    graph.add_edge(2, 3, 1)


    print("Test 1")
    print(graph.vertices) # affiche dict_keys([1, 2, 3])
    print("\nTest 2")
    print(len(graph)) # affiche 3
    print("\nTest 3")
    print(graph[2]) # affiche {1: 1, 3: 1}
    print("\nTest 4") # vertex : (voisin : distance), (voisin, distance)...
    print(graph)
    print("\nTest 5")
    for vertex in graph:
        print(vertex)
    print("\nTest 6")
    graph.remove_edge(1, 2)
    print(graph)
    print("\nTest 8")
    print(graph.induced_graph(graph.edges.keys(), False))# affiche le même graphe rendu non-orienté
    print("\nTest 9")
    print(graph.is_complete()) # Affiche False
    print("\nTest 10") 
    graph.add_edge(1, 2, 1)
    graph.add_edge(1, 3, 1)
    graph.add_edge(3, 2, 1)
    graph.add_edge(3, 1, 1)

    print(graph.is_complete()) # Affiche True



def test_undirected_graph():
    print("Tests UndirectedGraph")

    undir_graph = UndirectedGraph()
    print(undir_graph)
    undir_graph.add_vertex(1)
    undir_graph.add_edge(1, 2, 1)
    undir_graph.add_edge(2, 3, 1)

    print("Test 1")
    print(undir_graph.vertices) # affiche dict_keys([1, 2, 3])

    print("\nTest 2")
    print(len(undir_graph)) # affiche 3

    print("\nTest 3")
    print(undir_graph[2]) # affiche {1: 1, 3: 1}

    print("\nTest 4")
    print(undir_graph)

    print("\nTest 5")
    for vertex in undir_graph:
        print(vertex)

    print("\nTest 6")
    undir_graph.remove_edge(1, 2)
    print(undir_graph)

    print("\nTest 7")
    print(undir_graph.is_connected()) # affiche False
    undir_graph.add_edge(1, 2, 1)
    print(undir_graph.is_connected()) # affiche True

    print("\nTest 9")
    print(undir_graph.is_complete()) # Affiche False

    print("\nTest 10") 
    undir_graph.add_edge(1, 3, 1)
    print(undir_graph.is_complete()) # Affiche True

test_directed_graph()
test_undirected_graph()