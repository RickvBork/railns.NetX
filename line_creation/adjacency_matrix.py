'''
Make adjacency matrix for every station pair using Dijkstra shortest path algorithm.
'''

import algorithms as alg
import analysis as ana
import graph_class
import helpers as hlp
import csv
import networkx
import numpy as np

# initialize path files for Noord Holland graph
path_stations_file = '../data/StationsHolland.csv'
path_tracks_file = '../data/ConnectiesHolland.csv'

# initialise graph class
Graph = line_graph_class.Graph

# make graph instance (Noord Holland)
g = Graph("NH", path_stations_file, path_tracks_file)


# get all distances between stations
length = dict(networkx.all_pairs_dijkstra_path_length(g.G))

# put distances into matrix
station_list = list(g.G.nodes)
n = len(station_list) 
m = n
A = np.zeros(shape=(n,m))

for row in range(n):
	for column in range(m):
		station1 = station_list[row]
		station2 = station_list[column]	
		A[row][column] = length[station1][station2]
print(A)
# write matrix to file
np.savetxt('adjacencies.txt',A,fmt='%.0f')

with open('../data/adjacencies.csv', 'w', newline='') as myfile:
	writer1 = csv.writer(myfile,delimiter=',',quotechar=' ', quoting=csv.QUOTE_MINIMAL)
	writer1.writerow(station_list)
	for i in range(n):	
		writer1.writerow(A[i][0:i+1])

