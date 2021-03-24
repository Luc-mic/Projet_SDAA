from test.test_graph import *
from test.test_graph_generation import *
from test.test_temps_generation import *
from test.test_dijkstra import *
from test.test_temps_gen_alpha import *

test_graph()
test_graph_generation()
test_dijkstra()
time_generate_graph(10, 500, 10, 1)
time_generate_graph_alpha(100, 100, 50)

