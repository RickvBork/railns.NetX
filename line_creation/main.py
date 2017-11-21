import line_algorithms as alg
import line_analysis as ana
import line_graph_class
import helpers as hlp

# initialize path files for Noord Holland graph
path_stations_file = '../data/StationsHolland.csv'
path_tracks_file = '../data/ConnectiesHolland.csv'

# initialise graph class
Graph = line_graph_class.Graph

# make graph instance (Noord Holland)
g = Graph("NH", path_stations_file, path_tracks_file)

scores, p_scores, best_tracks = alg.random_walk(g, 1)

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

