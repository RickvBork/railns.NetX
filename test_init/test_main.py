import test_class
import test_algos as alg
import test_helpers as hlp
import analysis as ana

# initialize path files for Noord Holland graph
path_stations_file = '../data/StationsHolland.csv'
path_tracks_file = '../data/ConnectiesHolland.csv'

# initialise graph class
Graph = test_class.Graph

# make graph instance (Noord Holland)
g = Graph("NH", path_stations_file, path_tracks_file)

scores, p_scores, best_tracks = alg.random_walk(g, 100000)

print(p_scores)

# get score of smart random walk
# scores, p_scores, best_tracks = alg.smart_random_walk(g, 1)

# hlp.print_score_information(scores)

#analysis.draw_barchart(p_scores)

#score_list = alg.hierholzer(g)

# analysis.draw_graph(g)
#analysis.draw_p_barchart(p_scores)

score_list = alg.hierholzer(g)

#print(score_list)

# print best tracks
# for track in best_tracks:
# 	for key in track:
# 		print("{}: {}".format(key, track[key]))

ana.draw_barchart(p_scores)


