# run in terminal: exec(open("./initialize_tracks.test.py").read())
# to run this script

import line_algorithms as alg
import line_analysis as ana
import line_graph_class
import helpers as hlp
import csv
import numpy
import track_class as tc
import line_edges_class as tc2
import service_class as sc

# initialize path files for Noord Holland graph
path_stations_file = '../data/StationsHolland.csv'
path_tracks_file = '../data/ConnectiesHolland.csv'

# initialise graph class
Graph = line_graph_class.Graph

# make graph instance (Noord Holland)
g = Graph("NH", path_stations_file, path_tracks_file)

#all_paths_dijkstra_path_length(g.G[])
# get scores
scores, p_scores, best_tracks = alg.random_walk(g, 10)

track1 = best_tracks[1]['tracks']['1']
trackc = tc.track(track1, g)

service1 = sc.service(g)
service1.add_track(trackc)

