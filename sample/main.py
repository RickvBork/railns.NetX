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

nodelist, critical_edge_list, min_edge_weight = Graph.spit_data_lists()

print(nodelist)
print(min_edge_weight)
print(critical_edge_list)

scores = []
for i in range(10):
	scores.append(Graph.random_walk(nodelist, weight_list, minimum_weight, critical_connections))
print(scores)

#make bar chart of scores
barchart.draw(scores)
