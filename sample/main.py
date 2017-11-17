'''
main.py
@author Team Stellar Heuristiek
'''

# import the helpers file
import helpers
import barchart
import csv
# import walks TODO IGNORE FOR NOW!

# initialise graph class
Graph = helpers.Graph


# initialize path files
path_stations_file = '../data/StationsHolland.csv'
path_tracks_file = '../data/ConnectiesHolland.csv'

# OTHER WAY TO GET CRITICAL LIST?
critical_stations = Graph.add_csv_nodes(path_stations_file)

Graph.add_csv_edges(path_tracks_file, critical_stations)

nodelist, critical_edge_list, minimum_edge_weight = Graph.spit_data_lists()

# print(walks.walk1(nodelist, minimum_edge_weight, critical_edge_list)) TODO IGNORE FOR NOW!

scores = []
p = []
for i in range(10000):
	p, score = Graph.random_walk(nodelist, minimum_edge_weight, critical_edge_list)
	scores.append(score)
	print(p)

helpers.print_score_information(scores)

# make bar chart of scores
# barchart.draw(scores)