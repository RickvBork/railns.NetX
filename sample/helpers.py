import csv
import networkx as nx
import matplotlib.pyplot as plt
import tkinter # by thom, because of some run errors
import random

G = nx.Graph()

'''
Graph class, mostly storage for functions. Can later be turned into a init Class,
storing multiple graphs from multiple csv files.
'''
class Graph:

	'''
	Adds nodes with node attributes to the graph from a formatted csv file.
	For optimization purposes, a critical node list is also created.
	'''
	def add_csv_nodes(file_name):

			with open(file_name) as csvfile:
			    rows = csv.reader(csvfile)

			    critical_station_list = []
			    for row in rows:

			    	if row[3] == "Kritiek":
			    		critical_station_list.append(row[0])
			    		G.add_node(row[0],
			    			pos = (float(row[2]), float(row[1])), 
			    			color = 'r',
			    			size = 40)

			    	else:
			    		G.add_node(row[0], 
			    			pos = (float(row[2]), float(row[1])),
			    			color = 'k',
			    			size = 10)

			return critical_station_list

	'''
	Adds the edges and attributes to the graph from a formatted csv file.
	'''
	def add_csv_edges(file_name, list):

		with open(file_name) as csvfile:
			rows = csv.reader(csvfile)

			for row in rows:
				if row[0] in list and row[1] in list:
					print('AAA' + row[0], row[1])
					G.add_edge(row[0], row[1], weight = int(row[2]), color = 'r')

				elif row[0] in list or row[1] in list:
					print('BBB' + row[0], row[1])
					G.add_edge(row[0], row[1], weight = int(row[2]), color = 'r')

				else:
					G.add_edge(row[0], row[1], weight = int(row[2]), color = 'k')

	'''
	Draws this instance of the graph. If an init is also implemented, multiple Graphs
	can be stored and drawn.
	'''
	def draw_graph():

		# get positions of nodes and edges
		pos = nx.get_node_attributes(G, 'pos')

		# make node color map and node size maps for draw function
		node_color_map = []
		node_size_map = []
		for node in G.nodes():
			node_color_map.append(nx.get_node_attributes(G, 'color')[node])
			node_size_map.append(nx.get_node_attributes(G, 'size')[node])

		# list comprehension to get edge color map
		edge_color_map = [nx.get_edge_attributes(G,'color')[edge] for edge in G.edges()]

		# draw everything except labels and show plot
		nx.draw_networkx(G, pos, node_color = node_color_map, node_size = node_size_map, edge_color = edge_color_map, with_labels = False)
		plt.show()


	def info_for_random_walk(critical_station_list):
		# determine critical connections and make list
		critical_lines = 0
		critical_connections = []
		for v in G:
			for w in G[v]:
				if v in critical_station_list and [v, w] not in critical_connections and [w, v] not in critical_connections:
					#print("i")
					# for every neighbour, add 1 critical line
					for n in G[w]:
						critical_lines += 1
						critical_connections.append([v,w])
		#print(critical_connections)
		
		# now start random walk:
		# Laat python tussen 0 en 21 berekenen en kies beginstation uit lijst.

		# make list of all nodes (G.nodes() returns an object that is not accessable with nodes[i])
		#nodelist = critical_node_list + non_critical_node_list
		nodelist = [node for node in G.nodes()]
		#weight_list = [weight for node in G.nodes()]
		# make dict keyed by tuple (from, to) : weight
		edge_labels = {}
		weight_list = []
		# iterate over tuples in edges (from, to) = (u,v) 
		# DEBUG: DOUBLE iterate edges earlier in code!
		edges = G.edges()
		for u,v in edges:
		    weight = G[u][v]['weight']
		    weight_list.append(weight)
		edge_labels[u,v] = weight
		#print("++++++++++++++++++++++++++++++++++++++++++++++")
		#print(weight_list)
		minimum_weight = min(weight for weight in weight_list)
		
		return nodelist, weight_list, minimum_weight, critical_connections


	
	def random_walk(nodelist, weight_list, minimum_weight, critical_connections):
				# rand number of tracks 1 up to including 7
		random_tracks = random.randint(1,7)

		# keep track of critical connections that are not used yet
		critical_connections_not_traversed = critical_connections
		length_critical_connections = len(critical_connections)
		#print('START track number is: ' + str(random_tracks))
		for track in range(random_tracks):

			# rand start station 0 up to nodelist length - 1 to pick a node in nodelist
			starting_station = nodelist[random.randint(0,len(nodelist) - 1)]
			#print('+++NEW Starting station is: ' + starting_station)
			#print('+++NEW Neighbors are: {}'.format(G[starting_station]))
			time = 0

			# rand time for a given track
			random_time = random.randint(minimum_weight,120)
			#print('+++NEW track length is going to be: ' + str(random_time))

			counter = 0
			delete_counter = 0
			while time < random_time:

				# chooses a random key from a dictionary (neighbors), is choosing a random neighbor
				#print("_+++++++++++++++++++++++++++")
				#print(G[starting_station])
				#random_neighbor = random.choice(G[starting_station]).keys()
				random_neighbor = random.choice(list(G[starting_station]))
				#print('Random choise is: ' + random_neighbor)

				# keeps track of time of the track
				time += G[starting_station][random_neighbor]['weight']

				# always pick one track, catch exception of second track being larger than random time
				if time > random_time and counter != 0:
					#print('        CAUGHT EXCEPTION')
					break
				counter += 1

				#print('The time from: ' + starting_station + ' to ' + random_neighbor + ' is: {}'.format(G[starting_station][random_neighbor]['weight']))
				#print('The total time is: ' + str(time))
		
				# delete connection from critical_connections_not_traversed
				if [starting_station, random_neighbor] in critical_connections_not_traversed:
					critical_connections_not_traversed.remove([starting_station, random_neighbor])
					delete_counter += 1
					#print([starting_station, random_neighbor])
		
				if [random_neighbor, starting_station] in critical_connections_not_traversed:
					critical_connections_not_traversed.remove([random_neighbor, starting_station])

				# updates the starting station
				starting_station = random_neighbor

				#print('        Updated starting station is: ' + starting_station)
				#print('        Updated neighbors are: {}'.format(G[random_neighbor]))

		#print(critical_connections)
		#print(delete_counter)

		score = float(1 - float(len(critical_connections_not_traversed)) / float(length_critical_connections))
		#print(score)
		#print(float(len(critical_connections_not_traversed)))
		#print(float(length_critical_connections))
		return score





