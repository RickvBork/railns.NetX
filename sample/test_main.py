import test_helpers

# initialize path files
path_stations_file = '../data/StationsHolland.csv'
path_tracks_file = '../data/ConnectiesHolland.csv'

# initialise graph class
Graph = test_helpers.Graph

g = Graph("NH", path_stations_file, path_tracks_file)

print(g.min_edge_weight)