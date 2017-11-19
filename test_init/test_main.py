import test_class
import test_algos
import test_helpers

# initialize path files for Noord Holland graph
path_stations_file = '../data/StationsHolland.csv'
path_tracks_file = '../data/ConnectiesHolland.csv'

# initialise graph class
Graph = test_class.Graph
alg = test_algos

# make graph instance (Noord Holland)
g = Graph("NH", path_stations_file, path_tracks_file)

scores = alg.random_walk(g, 1000)[0]