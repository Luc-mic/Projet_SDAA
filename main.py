from test.test_graph import *
from test.test_graph_generation import *
from test.test_temps_generation import time_generate_graph, time_court_chemin_graph
from test.test_dijkstra import *
from test.test_temps_gen_alpha import *

test_graph()
test_graph_generation()
test_dijkstra()
time_generate_graph(10, 500, 10, 10)
time_generate_graph_alpha(70, 30, 30)
time_court_chemin_graph(10, 300, 10, 30)
time_court_chemin_graph_alpha(150,30,10)

