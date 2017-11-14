'''
main.py
@author Team Stellar Heuristiek
'''

# import the helpers file
import helpers
import barchart

# initialise graph class
Graph = helpers.Graph


# initialize path files
path_stations_file = '../data/StationsHolland.csv'
path_tracks_file = '../data/ConnectiesHolland.csv'

# OTHER WAY TO GET CRITICAL LIST?
critical_stations = Graph.add_csv_nodes(path_stations_file)

Graph.add_csv_edges(path_tracks_file, critical_stations)

nodelist, critical_edge_list, minimum_edge_weight = Graph.spit_data_lists()

scores = []
for i in range(1):
	scores.append(Graph.random_walk(nodelist, minimum_edge_weight, critical_edge_list))

#make bar chart of scores
barchart.draw(scores)

#testing
# nodelist, critical_edge_list, min_edge_weight = spit_data_list(nodelist, critical_edge_list, min_edge_weight)
# print(critical_edge_list)
# print('hoi')
