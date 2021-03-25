from src.graph_generation import generate_random_graph, generate_random_community_graph
from src.graph import DirectedGraph
from time import process_time, perf_counter
import numpy as np
import matplotlib.pyplot as plt
import random as rd


def time_generate_graph_alpha(m, nb_valeur, nb_repetition=1):
    t_rand_graph = []
    for alpha in np.linspace(m - 1, m * (m - 1) / 2, nb_valeur):
        valeur_moyenne = 0
        for repetition in range(nb_repetition):
            t0 = process_time()
            generate_random_graph(m, int(round(alpha)))
            t1 = process_time()
            valeur_moyenne += t1 - t0
        t_rand_graph.append(valeur_moyenne / nb_repetition)
        print(alpha / (m * (m - 1) / 2))

    t_com_graph = []
    for alpha in np.linspace(m - 1, m * (m - 1) / 2, nb_valeur):
        valeur_moyenne = 0
        for n in range(nb_repetition):
            node_per_com = [0]
            cumul = 0
            while cumul != m:
                new = rd.randint(1, m - cumul)
                cumul += new
                node_per_com.append(new)
            t0 = process_time()
            generate_random_community_graph(node_per_com, alpha / (m * (m - 1) / 2), alpha / (m * (m - 1) / 2))
            t1 = process_time()
            valeur_moyenne += t1 - t0
        t_com_graph.append(valeur_moyenne / nb_repetition)
        print(alpha / (m * (m - 1) / 2))

    n_range = np.linspace(m - 1, m * (m - 1) / 2, nb_valeur)
    plt.plot(n_range, t_rand_graph, label="generate_random_graph")
    plt.plot(n_range, t_com_graph, label="generate_random_community_graph")
    plt.xlabel('alpha')
    plt.ylabel('temps(s)')
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True)
    plt.savefig('exemple_process_time.png')
    plt.show()
    return

def time_court_chemin_graph_alpha(m, nb_valeur, nb_repetition=1):
    t_dijkstra = []
    t_heap = []
    t_bellman_ford = []
    for alpha in np.linspace(m - 1, m * (m - 1) / 2, nb_valeur):
        valeur_moyenne_dijkstra = 0
        valeur_moyenne_heap = 0
        valeur_moyenne_bellman = 0
        for repetition in range(nb_repetition):
            my_graph = generate_random_graph(m, int(round(alpha)))
            t0 = process_time()
            my_graph.dijkstra_classique(0)
            t1 = process_time()
            my_graph.dijkstra_heap(0)
            t2 = process_time()
#            my_graph.bellman_ford(0)
            t3 = process_time()
            valeur_moyenne_dijkstra += t1 - t0
            valeur_moyenne_heap += t2 - t1
#            valeur_moyenne_bellman += t2 -t1
        t_dijkstra.append(valeur_moyenne_dijkstra / nb_repetition)
        t_heap.append(valeur_moyenne_heap / nb_repetition)
        #        t_bellman_ford.append(valeur_moyenne_bellman / nb_repetition)
        print(alpha / (m * (m - 1) / 2))

    n_range = np.linspace(m - 1, m * (m - 1) / 2, nb_valeur)
    plt.plot(n_range, t_dijkstra, label="dijkstra_classique")
    plt.plot(n_range, t_heap, label="dijkstra_heap")
    #   plt.plot(n_range, t_bellman_ford, label="bellman_ford")
    plt.xlabel('alpha')
    plt.ylabel('temps(s)')
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True)
    plt.savefig('exemple_process_time.png')
    plt.show()
    return