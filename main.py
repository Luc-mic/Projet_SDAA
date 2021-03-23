from reddit.reddit_analysis import subreddit_degree
from reddit.reddit_analysis import subreddit_activity
from reddit.reddit_analysis import subbredit_shortest_path
from reddit import parser
from test.test_graph import test_graph
from test.test_graph_generation import test_graph_generation
from test.test_dijkstra import test_dijkstra
import time

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
    subbredit_shortest_path(reddit_graph, "disney", "vegan")
    subbredit_shortest_path(reddit_graph, "greenbaypackers", "missouripolitics")
    print("")

reddit()