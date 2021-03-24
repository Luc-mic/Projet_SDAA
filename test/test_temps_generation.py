from time import process_time
from src.graph_generation import generate_random_graph, generate_random_community_graph
from time import process_time, perf_counter
import numpy as np
import matplotlib.pyplot as plt
import random as rd


def time_generate_graph(start, end, step=1, nb_repetition=1, alpha=0.2):
    assert 0 < alpha, "alpha must be positive"
    assert alpha < 1,"alpha too high, it induce too much edges for the graph"
    assert round(alpha * start * (start -1) / 2) >= start-1, "Either the start value or alpha is too low"

    t_rand_graph = []
    for i in range(start, end, step):
        valeur_moyenne = 0
        for n in range(nb_repetition):
            t0 = process_time()
            generate_random_graph(i, round(alpha * i * (i -1) / 2))
            t1 = process_time()
            valeur_moyenne += t1-t0
        t_rand_graph.append(valeur_moyenne/nb_repetition)
        print(i/end)

    t_com_graph = []
    for i in range(start, end, step):
        valeur_moyenne = 0
        for n in range(nb_repetition):
            node_per_com = [0]
            cumul = 0
            while cumul != i:
                new = rd.randint(1,i-cumul)
                cumul += new
                node_per_com.append(new)
            t0 = process_time()
            generate_random_community_graph(node_per_com, alpha, alpha)
            t1 = process_time()
            valeur_moyenne += t1-t0
        t_com_graph.append(valeur_moyenne/nb_repetition)
        print(i/end)

    n_range = np.arange(start, end, step)
    plt.plot(n_range, t_rand_graph)
    plt.plot(n_range, t_com_graph)
    plt.xlabel('taille $n$')
    plt.ylabel('temps(s)')
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True)
    plt.savefig('exemple_process_time.png')
    plt.show()
    return
