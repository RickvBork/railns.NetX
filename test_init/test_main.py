import test_class
import test_algos
import test_helpers

# initialize path files for Noord Holland graph
path_stations_file = '../data/StationsHolland.csv'
path_tracks_file = '../data/ConnectiesHolland.csv'

# initialise graph class
Graph = test_class.Graph
alg = test_algos
hlp = test_helpers

# make graph instance (Noord Holland)
g = Graph("NH", path_stations_file, path_tracks_file)

scores, p_scores, best_tracks = alg.random_walk(g, 1)

hlp.print_score_information(scores)

score_list = alg.hierholzer(g)

# print best tracks
# for track in best_tracks:
# 	for key in track:
# 		print("{}: {}".format(key, track[key]))