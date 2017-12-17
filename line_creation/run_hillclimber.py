'''
used to test functions, file is ignored by git.
'''

import algorithms as alg
import analysis as ana
import graph_class
import helpers as hlp
import csv
import numpy
import service_class as sc
import track_class as tc
import hillclimber as hc
import hillclimber_helper as hh

# initialize path files for Noord Holland graph
#path_stations_file = '../data/StationsHolland.csv'
#path_tracks_file = '../data/ConnectiesHolland.csv'

# initialize path files for national graph
path_stations_file = '../data/StationsNationaal.csv'
path_tracks_file = '../data/ConnectiesNationaal.csv'

# initialise graph class
Graph = graph_class.Graph

# make graph instance (Noord Holland)
g = Graph("NH", path_stations_file, path_tracks_file)

#all_paths_dijkstra_path_length(g.G[])
# get services
max_number_of_tracks = 20
max_time = 180
services = hh.random_walk(g, 10, max_number_of_tracks, max_time)

for service in services:
	print(service.critical_edges_traversed)
	print(service.s_score)
	print()

service1 = services[-1]
# now use hillclimber to improve service
number_of_tracks = len(service1.tracks) 
number_of_tries = 10
print(service1.s_score)

#for i in range(number_of_tracks):
#	for j in range(number_of_tries):
#		hc.hillclimber(service1,i)
#		print(service1.s_score)
#		
hillclimber_scores = []
for j in range(number_of_tries):
	for i in range(number_of_tracks):
		for k in range(number_of_tries):
			hc.hillclimber_sim_an(service1,i,k*i*j)
			print(service1.s_score)
			hillclimber_scores.append(service1.s_score) 

# write score to csv
with open('../data/hillclimber.csv', 'w', newline='') as csvfile:
	wr = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	for score in hillclimber_scores:
		wr.writerow([score])
