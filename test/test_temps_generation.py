from time import process_time
from src.graph_generation import generate_random_graph
from time import process_time, perf_counter
import numpy as np
import matplotlib.pyplot as plt


def time_generate_graph(start, end, step=1, nb_repetition=1, alpha=0.2):
    assert 0 < alpha, "alpha must be positive"
    assert alpha < start * ( start - 1 ) / ( 2 * start ** 2 ),"alpha too high, it induce too much edges for the graph"
    assert round(alpha * start ** 2) >= start, "Either the start value or alpha is too low"

    t = []
    for i in range(start, end, step):
        valeur_moyenne = 0
        for n in range(nb_repetition):
            t0 = process_time()
            generate_random_graph(i, round(alpha * i ** 2))
            t1 = process_time()
            valeur_moyenne += t1-t0
        t.append(valeur_moyenne/nb_repetition)
        print(i)

    n_range = np.arange(start, end, step)
    print(n_range, t)
    plt.plot(n_range, t)
    plt.xlabel('taille $n$')
    plt.ylabel('temps(s)')
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True)
    plt.savefig('exemple_process_time.png')
    plt.show()
    return
