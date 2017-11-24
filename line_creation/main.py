import line_algorithms as alg
import line_analysis as ana
import line_graph_class
import helpers as hlp
import csv

# initialize path files for Noord Holland graph
path_stations_file = '../data/StationsHolland.csv'
path_tracks_file = '../data/ConnectiesHolland.csv'

# initialise graph class
Graph = line_graph_class.Graph

# make graph instance (Noord Holland)
g = Graph("NH", path_stations_file, path_tracks_file)

scores, p_scores, best_tracks = alg.random_walk(g, 1000)

ana.draw_barchart(p_scores)


# write scores to csv
# ref: https://stackoverflow.com/questions/39282516/python-list-to-csv-throws-error-iterable-expected-not-numpy-int64
# ref: https://docs.python.org/3/library/csv.html
with open('../data/results.csv', 'w', newline='') as myfile:
	wr = csv.writer(myfile,delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	wr.writerows(map(lambda x: [x], scores))


