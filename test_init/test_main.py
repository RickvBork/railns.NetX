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

scores, p_scores, best_tracks = alg.random_walk(g, 5)

print(p_scores)

count = 0
for i in range(len(p_scores)):
	if (p_scores[i] > 0.7) and (p_scores[i] < 0.8):
		count += 1
print(count)

hlp.print_score_information(scores)

# analysis.draw_graph(g)
analysis.draw_p_barchart(p_scores)

score_list = alg.hierholzer(g)
#print(score_list)

# print best tracks
# for track in best_tracks:
# 	for key in track:
# 		print("{}: {}".format(key, track[key]))