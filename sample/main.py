'''
main.py
@author Team Stellar Heuristiek
'''

# import the helpers file
import helpers

# initialise graph class
Graph = helpers.Graph


# initialize path files
path_stations_file = '../data/StationsHolland.csv'
path_tracks_file = '../data/ConnectiesHolland.csv'

# OTHER WAY TO GET CRITICAL LIST?
critical_stations = Graph.add_csv_nodes(path_stations_file)
Graph.add_csv_edges(path_tracks_file, critical_stations)

print(critical_stations)

#Graph.draw_graph()

# random walk:
print("randomwalks:")
nodelist, weight_list, minimum_weight, critical_connections = Graph.info_for_random_walk(critical_stations)

scores = []
for i in range(10):
	scores.append(Graph.random_walk(nodelist, weight_list, minimum_weight, critical_connections))
	
print(scores)