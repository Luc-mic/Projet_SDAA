from time import process_time
from src.graph_generation import generate_random_graph
from time import process_time, perf_counter
import numpy as np
import matplotlib.pyplot as plt


def time_generate_graph_alpha(m, step, nb_repetition=1):
    t = []
    for alpha in range(m - 1, m * (m - 1) // 2 + 1, step):
        valeur_moyenne = 0
        for repetition in range(nb_repetition):
            t0 = process_time()
            generate_random_graph(m, alpha)
            t1 = process_time()
            valeur_moyenne += t1-t0
        t.append(valeur_moyenne/nb_repetition)
        print(alpha)

    n_range = np.arange(m - 1, m * (m - 1) // 2 + 1, step)
    print(n_range, t)
    plt.plot(n_range, t)
    plt.xlabel('alpha')
    plt.ylabel('temps(s)')
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True)
    plt.savefig('exemple_process_time.png')
    plt.show()
    return
