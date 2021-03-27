from reddit.reddit_analysis import subreddit_degree
from reddit.reddit_analysis import subreddit_activity
from reddit.reddit_analysis import subbredit_shortest_path
from reddit import parser

from test.test_dijkstra import test_dijkstra
from test.test_graph import test_graph
from test.test_temps_generation import time_court_chemin_graph
from test.test_temps_generation import time_generate_graph
from test.test_graph_generation import test_graph_generation
from test.test_temps_gen_alpha import time_court_chemin_graph_alpha
from test.test_temps_gen_alpha import time_generate_graph_alpha

from src.graph_generation import generate_random_graph

from networkx import draw
import matplotlib.pyplot as plt


def tests():

    test_graph()
    test_graph_generation()
    test_dijkstra()


def reddit():

    data_path = "data/reddit.tsv"

    reddit_graph = parser.create_graph(data_path)

    subreddit_degree(reddit_graph)
    print("")
    subreddit_activity(reddit_graph)
    print("")
    # t = time.time()
    subbredit_shortest_path(reddit_graph, "disney", "vegan")
    # print(time.time() - t)
    # t = time.time()
    subbredit_shortest_path(
        reddit_graph,
        "greenbaypackers",
        "missouripolitics")
    #print(time.time() - t)
    print("")


def networkx_test():

    # On cherche simplement à afficher un petit graphe dans un fichier png. La
    # vitesse de networkx a été comparé dans la "course" des algorithmes, et
    # est visible dans le rapport.

    graph = generate_random_graph(5, 10, True)
    networkx_reddit_graph = graph.to_networkx()

    draw(networkx_reddit_graph, with_labels=True)

    plt.savefig("graph.png")


# tests()
# reddit()
# networkx_test()

#time_generate_graph(500, 1510, 100, 5, 0.7)
#time_court_chemin_graph(500, 1510, 100, 5, 0.7)
#time_generate_graph_alpha(1000, 5, 5)
#time_court_chemin_graph_alpha(1500, 5, 5)
