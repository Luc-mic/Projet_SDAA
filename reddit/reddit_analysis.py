from heapq import heappushpop
from heapq import heappop
from reddit import parser
from time import time
data_path = "../data/reddit.tsv"


def n_most_active_subreddits(graph, n):
    n_most_popular = [(0, "") for i in range(n)]
    for vertex in graph:
        heappushpop(n_most_popular, (len(graph[vertex]), vertex))
    return n_most_popular


def subreddit_degree(graph):

    ten_most_active_subreddits = n_most_active_subreddits(graph, 10)

    nb_impopular = 0
    for vertex in graph:
        if len(graph[vertex]) == 0:
            nb_impopular += 1

    print(str(nb_impopular) + " subreddits have 0 links towards other subreddits.")
    print("The ten subreddits having the highest number of links are :")
    while ten_most_active_subreddits:
        (links, vertex) = heappop(ten_most_active_subreddits)
        print(str(vertex) + " with " + str(links) + " links.")


def subreddit_activity(graph):
    most_active_subbredits = n_most_active_subreddits(
        graph, len(graph) * 2 // 100)

    links_in_graph = 0
    for vertex in graph:
        links_in_graph += len(graph[vertex])

    links_in_most_active_subreddits = 0

    while most_active_subbredits:
        (links, vertex) = heappop(most_active_subbredits)
        links_in_most_active_subreddits += links

    print("2% most active subreddits represent " +
          str(links_in_most_active_subreddits /
              links_in_graph *
              100) +
          r"% of subreddits activity.")


def subbredit_shortest_path(graph, initial, final):
    print("Distance from " + str(initial) + " to " + str(final) +
          " is " + str(graph.dijkstra_aimed(initial, final)[final][0]) + ".")
