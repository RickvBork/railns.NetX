import test_class
import test_algos
import test_helpers
import analysis

# initialize path files for Noord Holland graph
path_stations_file = '../data/StationsHolland.csv'
path_tracks_file = '../data/ConnectiesHolland.csv'

# initialise graph class
Graph = test_class.Graph
alg = test_algos
hlp = test_helpers

# make graph instance (Noord Holland)
g = Graph("NH", path_stations_file, path_tracks_file)

scores, p_scores, best_tracks = alg.random_walk(g, 50)

hlp.print_score_information(scores)

analysis.draw_barchart(p_scores)