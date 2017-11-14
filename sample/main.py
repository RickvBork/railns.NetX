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
critical_list = Graph.add_csv_nodes(path_stations_file)
Graph.add_csv_edges(path_tracks_file, critical_list)