# FILE: Graph.py
# Python v27
# 
# This file loads in stations and tracks from two csv files.
# It then seperates them in critical and non critical stations and edges, and stored in lists.
# These are used by NetworkX to plot the graph with the important data.
# By seperating stations and tracks into categories, different colors can be used to distinguish
# between them.

import networkx as nx
import pylab as py
import csv

critical_stations = []

# define G
G = nx.Graph()

# read in stations from csv and put each station as node in graph
with open('StationsHolland.csv') as csvfile:
    stations = csv.reader(csvfile, delimiter=',', quotechar='|')

    for row in stations:

		if row[3] == "Kritiek":
			critical_stations.append(row[0])
			G.add_node(row[0],
				pos = (float(row[2]), float(row[1])),
				label = str(row[0]))
		else:
			G.add_node(row[0], 
				pos = (float(row[2]), float(row[1])),
				label = str(row[0]))

critical_neighbours = []

# add connections between nodes (=stations) into graph
with open('ConnectiesHolland.csv') as csvfile:
    stations = csv.reader(csvfile, delimiter=',', quotechar='|')

    for row in stations:
    	if row[0] and row[1] in critical_stations:
    		# both are critical, color edge red
    		G.add_edge(row[0], row[1], weight=int(row[2]))

    	elif row[0] or row[1] in critical_stations:
    		# one is a critical station, color edge blue
    		G.add_edge(row[0], row[1], weight=int(row[2]))

    	else:
    		# neither is critical, color edge black
    		G.add_edge(row[0], row[1], weight=int(row[2]))

# link position attibute to node and call this 'pos'
pos = nx.get_node_attributes(G,'pos')

# make node lists
critical_node_list = []
non_critical_node_list = []

# define nodes
nodes = G.nodes()

# iterate over nodes
for node in nodes:
	if node in critical_stations:
		critical_node_list.append((node))
	else:
		non_critical_node_list.append((node))

# draw different kinds of nodes for critical stations
nx.draw_networkx_nodes(G, pos, node_size=20, nodelist=critical_node_list, node_color='r')
nx.draw_networkx_nodes(G, pos, node_size=5, nodelist=non_critical_node_list, node_color='k')

# make edge lists
critical_edge_list = []
non_critical_edge_list = []
super_critical_edge_list = []

# define edges
edges = G.edges()

# iterate over tuples in edges (from, to) = (u,v)
for u,v in edges:
	if u in critical_stations and v in critical_stations:
		super_critical_edge_list.append((u,v))
	elif u in critical_stations or v in critical_stations:
		critical_edge_list.append((u,v))
	else:
		non_critical_edge_list.append((u,v))

# draw different kinds of edges
nx.draw_networkx_edges(G, pos, edgelist = super_critical_edge_list, edge_color = 'r')
nx.draw_networkx_edges(G, pos, edgelist = critical_edge_list, edge_color = 'b')
nx.draw_networkx_edges(G, pos, edgelist = non_critical_edge_list, edge_color = 'k')

# print data about the stations
print("Critical stations: {}".format(len(critical_node_list)))
print("Non-critical stations: {}".format(len(non_critical_node_list)))
print("All stations: {}".format(len(non_critical_node_list + critical_node_list)))

# print data about the tracks
print("Useless tracks: {}".format(len(non_critical_edge_list)))
print("Critical tracks: {}".format(len(critical_edge_list)))
print("Supercritical tracks: {}".format(len(super_critical_edge_list)))
print("Total important tracks: {}".format(len(super_critical_edge_list + critical_edge_list)))

# make dict keyed by tuple (from, to) : weight
edge_labels = {}

# iterate over tuples in edges (from, to) = (u,v) 
# DEBUG: DOUBLE iterate edges earlier in code!
for u,v in edges:
	edge_labels[u,v] = G[u][v]['weight']
nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, font_size = 5)

label_positions = {}
# accessing node data by generating a list of tuples, j is station name, k is dict with attributes
for j,k in G.nodes(data=True):

	# alter coordinates and append to correct station name
	label_positions[j] = (k['pos'][0],k['pos'][1] + 0.05)

	# individual alterations to coordinates
	if j == 'Rotterdam Centraal':
		label_positions[j] = (k['pos'][0],k['pos'][1] - 0.05)

	if j == 'Amsterdam Sloterdijk':
		label_positions[j] = (k['pos'][0]+0.08,k['pos'][1]+0.03)

	if j == 'Amsterdam Zuid':
		label_positions[j] = (k['pos'][0],k['pos'][1]-0.04)

	if j == 'Amsterdam Amstel':
		label_positions[j] = (k['pos'][0]+0.07,k['pos'][1]-0.01)

	if j == 'Amsterdam Centraal':
		label_positions[j] = (k['pos'][0]+0.08,k['pos'][1])

	if j == 'Beverwijk':
		label_positions[j] = (k['pos'][0]+0.04,k['pos'][1]+0.02)

	if j == 'Heemstede-Aerdenhout':
		label_positions[j] = (k['pos'][0],k['pos'][1]-0.05)

	if j == 'Den Haag Centraal':
		label_positions[j] = (k['pos'][0]+0.02,k['pos'][1]+0.05)

# draw all labels to corrected position
labels = nx.get_node_attributes(G, 'label')
nx.draw_networkx_labels(G, label_positions, labels, font_size=5)

critical_total = 0
not_critical_total = 0

# DEBUG: DOUBLE iterate edges earlier in code!
for u,v in edges:
	if u in critical_stations or v in critical_stations:
		critical_total += edge_labels[u,v]
	else:
		not_critical_total += edge_labels[u,v]

print((critical_total % 60))
print(critical_total // 60)
print((not_critical_total % 60))
print(not_critical_total // 60)



min = (7*94)
t = 7
p = 0
print(min/100000)
S = 10000*p - (t*20 + min/100000)
print(S)

py.show()