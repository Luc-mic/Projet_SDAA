from reddit.reddit_analysis import subreddit_degree
from reddit.reddit_analysis import subreddit_activity
from reddit.reddit_analysis import subbredit_shortest_path
from reddit import parser
from test.test_graph import test_graph
from test.test_graph_generation import test_graph_generation
from test.test_dijkstra import test_dijkstra
import time
from test.test_graph_generation import *
from test.test_temps_generation import time_generate_graph, time_court_chemin_graph
from test.test_dijkstra import *
from test.test_temps_gen_alpha import *


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
    subbredit_shortest_path(reddit_graph, "greenbaypackers", "missouripolitics")
    #print(time.time() - t)
    print("")


#tests()
#reddit()

time_generate_graph(10, 500, 10, 10)
time_generate_graph_alpha(70, 30, 30)
time_court_chemin_graph(10, 300, 10, 30)
time_court_chemin_graph_alpha(150, 30, 10)
