# run in terminal: exec(open("./initialize_tracks.py").read())
# to run this script

import algorithms as alg
import analysis as ana
import graph_class
import helpers as hlp
import csv
import numpy
import edges_class as tc2
import service_class as sc
import track_class as tc3

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
track0 = best_tracks[0]['tracks']['1']

trackc1 = tc3.track(g)
trackc1.add_whole_track(track1)

trackc0 = tc3.track(g)
trackc0.add_whole_track(track0)

service1 = sc.service(g)
service1.add_track(trackc0)
 

