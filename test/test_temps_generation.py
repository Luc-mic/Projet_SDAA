from src.graph_generation import generate_random_graph
from src.graph_generation import generate_random_community_graph
from src.graph import DirectedGraph

from time import process_time
import numpy as np
import matplotlib.pyplot as plt
import random as rd


def time_generate_graph(start, end, step=1, nb_repetition=1, alpha=0.2):
    assert 0 < alpha, "alpha must be positive"
    assert alpha < 1, "alpha too high, it induce too much edges for the graph"
    assert round(alpha * start * (start - 1) / 2) >= start - \
        1, "Either the start value or alpha is too low"

    t_rand_graph = []

    print("Generating random undirected graphs...")

    for i in range(start, end, step):
        valeur_moyenne = 0.
        for n in range(nb_repetition):
            initial_time = process_time()
            generate_random_graph(i, round(alpha * i * (i - 1) / 2))
            final_time = process_time()
            valeur_moyenne += final_time - initial_time
        t_rand_graph.append(valeur_moyenne / nb_repetition)

    t_com_graph = []

    print("Generating random community graphs...")

    for i in range(start, end, step):
        valeur_moyenne = 0.
        for n in range(nb_repetition):
            node_per_com = [0]
            cumul = 0.
            while cumul != i:
                new = rd.randint(1, i - cumul)
                cumul += new
                node_per_com.append(new)
            initial_time = process_time()
            generate_random_community_graph(node_per_com, alpha, alpha)
            final_time = process_time()
            valeur_moyenne += final_time - initial_time
        t_com_graph.append(valeur_moyenne / nb_repetition)

    n_range = np.arange(start, end, step)
    plt.plot(n_range, t_rand_graph, label="Génération graphes aléatoires")
    plt.plot(n_range, t_com_graph, label="Génération graphes de communauté")
    plt.legend()
    plt.xlabel('Taille en noeuds $n$')
    plt.ylabel('Temps de génération (s)')
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True)
    plt.show()
    return


def time_court_chemin_graph(start, end, step=1, nb_repetition=1, alpha=0.2):
    assert 0 < alpha, "alpha must be positive"
    assert alpha < 1, "alpha too high, it induce too much edges for the graph"
    assert round(alpha * start * (start - 1) / 2) >= start - \
        1, "Either the start value or alpha is too low"

    t_dijkstra = []
    t_heap = []
    for i in range(start, end, step):
        valeur_moyenne_dijkstra = 0
        valeur_moyenne_heap = 0

        my_graph = generate_random_graph(i, round(alpha * i * (i - 1)), True)

        vertices_list = list(my_graph.vertices)
        for n in range(nb_repetition):

            initial_vertex = rd.choice(vertices_list)

            initial_time = process_time()
            my_graph.dijkstra_classique(initial_vertex)
            final_time = process_time()
            valeur_moyenne_dijkstra += final_time - initial_time

            initial_time = process_time()
            my_graph.dijkstra_heap(initial_vertex)
            final_time = process_time()
            valeur_moyenne_heap += final_time - initial_time

        t_dijkstra.append(valeur_moyenne_dijkstra / nb_repetition)
        t_heap.append(valeur_moyenne_heap / nb_repetition)

    n_range = np.arange(start, end, step)
    plt.plot(n_range, t_dijkstra, label="Dijkstra classique")
    plt.plot(n_range, t_heap, label="Dijkstra heap")
    plt.xlabel('Taille en noeuds $n$')
    plt.ylabel('Temps de calcul (en s)')
    plt.xscale('log')
    plt.yscale('log')
    plt.legend()
    plt.grid(True)
    plt.show()
    return
