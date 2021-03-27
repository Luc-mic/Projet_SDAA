from src.graph_generation import generate_random_graph
from src.graph_generation import generate_random_community_graph
from src.graph import DirectedGraph

from time import process_time, perf_counter
import numpy as np
import matplotlib.pyplot as plt
import random as rd


def time_generate_graph_alpha(m, nb_valeur, nb_repetition=1):

    print("Génération de graphes en fonction du nombre d'arrêtes...")
    time_random_graph = []
    for alpha in np.linspace(m - 1, m * (m - 1) / 2, nb_valeur):
        valeur_moyenne = 0
        for repetition in range(nb_repetition):
            initial_time = process_time()
            generate_random_graph(m, int(round(alpha)))
            final_time = process_time()
            valeur_moyenne += final_time - initial_time
        time_random_graph.append(valeur_moyenne / nb_repetition)

    time_community_graph = []
    for alpha in np.linspace(m - 1, m * (m - 1) / 2, nb_valeur):
        valeur_moyenne = 0
        for n in range(nb_repetition):
            node_per_community = [0]
            cumul = 0
            while cumul != m:
                new = rd.randint(1, m - cumul)
                cumul += new
                node_per_community.append(new)
            initial_time = process_time()
            generate_random_community_graph(
                node_per_community, alpha / (m * (m - 1) / 2), alpha / (m * (m - 1) / 2))
            final_time = process_time()
            valeur_moyenne += final_time - initial_time
        time_community_graph.append(valeur_moyenne / nb_repetition)

    n_range = np.linspace(m - 1, m * (m - 1) / 2, nb_valeur)
    plt.plot(n_range, time_random_graph, label="generate_random_graph")
    plt.plot(
        n_range,
        time_community_graph,
        label="generate_random_community_graph")
    plt.xlabel('Nombre d\'arêtes dans le graphe')
    plt.ylabel('Temps de génération (s)')
    plt.xscale('log')
    plt.yscale('log')
    plt.legend()
    plt.grid(True)
    plt.show()
    return


def time_court_chemin_graph_alpha(m, nb_valeur, nb_repetition=1):
    t_dijkstra = []
    t_heap = []

    print("Calcul dijkstra en fonction du nombre d'arrêtes...")

    for alpha in np.linspace(m - 1, m * (m - 1) / 2, nb_valeur):
        valeur_moyenne_dijkstra = 0
        valeur_moyenne_heap = 0
        for repetition in range(nb_repetition):
            my_graph = generate_random_graph(m, int(round(alpha)))
            initial_time = process_time()
            my_graph.dijkstra_classique(0)
            final_time = process_time()
            valeur_moyenne_dijkstra += final_time - initial_time
            initial_time = process_time()
            my_graph.dijkstra_heap(0)
            final_time = process_time()
            valeur_moyenne_heap += final_time - initial_time
        t_dijkstra.append(valeur_moyenne_dijkstra / nb_repetition)
        t_heap.append(valeur_moyenne_heap / nb_repetition)

    n_range = np.linspace(m - 1, m * (m - 1) / 2, nb_valeur)
    plt.plot(n_range, t_dijkstra, label="dijkstra_classique")
    plt.plot(n_range, t_heap, label="dijkstra_heap")
    plt.xlabel('Nombre d\'arêtes dans le graphe')
    plt.ylabel('Temps de calcul (s)')
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True)
    plt.legend()
    plt.show()
    return
