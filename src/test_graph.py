from graph import DirectedGraph
from graph import UndirectedGraph

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
print("\nTest 4")
print(graph)
print("\nTest 5")
for vertex in graph:
    print(vertex)
print("\nTest 6")
graph.remove_edge(1, 2)
print(graph)


print("Tests UndirectedGraph")

graph.reset()
graph = UndirectedGraph()
print(graph)
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
print("\nTest 4")
print(graph)
print("\nTest 5")
for vertex in graph:
    print(vertex)
print("\nTest 6")
graph.remove_edge(1, 2)
print(graph)
