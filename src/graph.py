from copy import copy
from heapq import heappush
from heapq import heappop

class DirectedGraph():

    def __init__(self, edges={}):
        self.edges = edges

    def __len__(self):
        return len(self.vertices)

    def __getitem__(self, vertex):
        assert vertex in self.vertices, "Vertex not in graph !"
        return self.edges[vertex]

    def __iter__(self):
        for vertex in self.vertices:
            yield vertex

    def __str__(self):

        text = ""

        for vertex in self.vertices:
            text += str(vertex) + " :"

            for neighboor in self.edges[vertex].keys():
                text += " (\"" + str(neighboor) + "\" : " + \
                    str(self.edges[vertex][neighboor]) + "),"

            text += "\n"
        return text

    @property
    def edges(self):
        return self.__edges

    @edges.setter
    def edges(self, edges):
        for vertex in edges.keys():
            for weight in edges[vertex].values():
                assert weight >= 0, "No negative weight !"
        self.__edges = edges
        self.vertices = edges.keys()

    @property
    def vertices(self):
        return self.__vertices

    @vertices.setter
    def vertices(self, vertices):
        self.__vertices = vertices

    def is_complete(self):
        for vertex in self.vertices:
            if len(self.edges[vertex].keys()) != len(self.vertices) - 1:
                return False
        return True

    def depth_search(self, initial):
        visited = []

        def depth_search_recursive(current):
            for neighboor in self.edges[current]:
                if neighboor not in visited:
                    visited.append(neighboor)
                    depth_search_recursive(neighboor)

        depth_search_recursive(initial)
        return visited

    def add_vertex(self, vertex):
        edges = self.edges
        edges[vertex] = {}
        self.edges = edges

    def remove_vertex(self, vertex):
        assert vertex in self.vertices, "Vertex not in vertices !"
        del self.edges[vertex]

        for other in self.vertices:
            self.remove_edge(other, vertex)
        
        self.vertices = self.edges.keys()

    def add_edge(self, vertex1, vertex2, weight):
        assert weight >= 0, "No negative weight !"
        if vertex1 not in self.vertices:
            self.add_vertex(vertex1)
        if vertex2 not in self.vertices:
            self.add_vertex(vertex2)

        assert vertex2 not in self.edges[vertex1].keys(
        ), "Edge already exists !"

        self.edges[vertex1][vertex2] = weight

    def remove_edge(self, vertex1, vertex2):
        if vertex2 in self.edges[vertex1].keys():
            del self.edges[vertex1][vertex2]

    def change_weight(self, vertex1, vertex2, weight):
        assert vertex1 in self.vertices, "Vertex not in graph !"
        assert vertex2 in self.vertices, "Vertex not in grpah !"
        assert vertex2 in self.edges[vertex1], "Edge do not exist !"

        self.edges[vertex1][vertex2] = weight

    def reset(self):
        vertices = list(self.vertices)
        for vertex in vertices:
            self.remove_vertex(vertex)

    def induced_graph(self, subset, directed=True):
        assert isinstance(directed, bool), "Directed argument must be bool"
        new_edges = {}

        for vertex in subset:
            assert vertex in self.vertices, "Incorrect subset, vertex not in graph"
            new_edges[vertex] = {}
        for vertex in subset:
            for other in subset:
                if other in self.edges[vertex].keys():
                    new_edges[vertex][other] = self.edges[vertex][other]
                    if directed == False and vertex not in new_edges[other].keys(
                    ):
                        new_edges[other][vertex] = self.edges[vertex][other]
        if directed:
            return DirectedGraph(new_edges)
        else:
            return UndirectedGraph(new_edges)

    def dijkstra_classique(self, initial):
        assert initial in self.vertices, "Initial not in graph"
        dist = {vertex : (float("inf"), None) for vertex in self}

        dist[initial] = (0, None)

        F = list(self.vertices)
        F.sort()
        while F:
            current = min(F, key=dist.get)
            F.remove(current)
            for neighboor in self[current]:
                if neighboor in F:
                    new_dist = dist[current][0] + self[current][neighboor]
                    if dist[neighboor][0] > new_dist:
                        dist[neighboor] = (new_dist, current)

        return(dist)

    def dijkstra_heap(self, initial):
        assert initial in self.vertices, "Initial not in graph"
        
        queue = [[0, initial]]
        dist = {vertex : (float("inf"), None) for vertex in self}

        dist[initial] = (0, None)

        F = list(self.vertices)
        F.sort()
        while F and queue:
            (current_dist, current) = heappop(queue)
            while current not in F:
                (current_dist, current) = heappop(queue)
            F.remove(current)
            for neighboor in self[current]:
                if neighboor in F and dist[neighboor][0] > current_dist + self[current][neighboor]:
                    dist[neighboor] = (dist[current][0] + self[current][neighboor], current)
                    heappush(queue, [dist[neighboor][0], neighboor])
                
        return(dist)

    def dijkstra_aimed(self, initial, end):

        assert initial in self.vertices, "Initial not in graph"
        assert end in self.vertices, "Initial not in graph"
        
        queue = [[0, initial]]
        dist = {vertex : (float("inf"), None) for vertex in self}

        dist[initial] = (0, None)

        F = list(self.vertices)
        while F and queue:
            (current_dist, current) = heappop(queue)
            while current not in F:
                (current_dist, current) = heappop(queue)
            F.remove(current)
            if current == end:
                break
            for neighboor in self[current]:
                if neighboor in F and dist[neighboor][0] > current_dist + self[current][neighboor]:
                    dist[neighboor] = (dist[current][0] + self[current][neighboor], current)
                    heappush(queue, [dist[neighboor][0], neighboor])
                
        return(dist)

    def bellman_ford(self, initial):
        assert type(self).__name__ == "DirectedGraph", "Bellman-Ford cannot be used on undirected graphs"



class UndirectedGraph(DirectedGraph):

    def __init__(self, edges={}):
        self.edges = edges

    @property
    def edges(self):
        return self.__edges

    @edges.setter
    def edges(self, edges):
        for vertex in edges.keys():
            for weight in edges[vertex].values():
                assert weight >= 0, "No negative weight !"
            for neighboor in edges[vertex].keys():
                assert vertex in edges[neighboor].keys(
                ) and edges[vertex][neighboor] == edges[neighboor][vertex], "Incorrect edges !"
        self.__edges = edges
        self.vertices = edges.keys()

    def is_connected(self):
        initial = list(self.vertices)[0]
        return len(self.vertices) == len(self.depth_search(initial))

    def remove_vertex(self, vertex):
        assert vertex in self.vertices, "Vertex not in vertices !"
        del self.edges[vertex]

        for other in self.vertices:
            self.remove_edge(other, vertex)

        self.vertices.remove(vertex)

    def add_edge(self, vertex1, vertex2, weight):
        assert weight >= 0, "No negative weight !"
        if vertex1 not in self.vertices:
            self.add_vertex(vertex1)
        if vertex2 not in self.vertices:
            self.add_vertex(vertex2)

        assert vertex2 not in self.edges[vertex1].keys(
        ), "Edge already exists !"

        self.edges[vertex1][vertex2] = weight
        self.edges[vertex2][vertex1] = weight

    def remove_edge(self, vertex1, vertex2):
        if vertex2 in self.edges[vertex1].keys():
            del self.edges[vertex1][vertex2]
            del self.edges[vertex2][vertex1]

    def change_weight(self, vertex1, vertex2, weight):
        assert vertex1 in self.vertices, "Vertex not in graph !"
        assert vertex2 in self.vertices, "Vertex not in grpah !"
        assert vertex2 in self.edges[vertex1], "Edge do not exist !"

        self.edges[vertex1][vertex2] = weight
        self.edges[vertex2][vertex1] = weight

    def induced_graph(self, subset):
        new_edges = {}

        for vertex in subset:
            assert vertex in self.vertices, "Incorrect subset, vertex not in graph"
            new_edges[vertex] = {}
            for other in subset:
                if other in self.edges[vertex].keys():
                    new_edges[vertex][other] = self.edges[vertex][other]
                    new_edges[other][vertex] = self.edges[other][vertex]
        return UndirectedGraph(new_edges)
