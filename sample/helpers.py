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
					G.add_edge(row[0], row[1], weight = int(row[2]), color = 'r')

				elif row[0] in list or row[1] in list:
					G.add_edge(row[0], row[1], weight = int(row[2]), color = 'r')

				else:
					G.add_edge(row[0], row[1], weight = int(row[2]), color = 'k')

	'''
	Draws this instance of the graph. If an init is also implemented, multiple Graphs
	can be stored and drawn.
	'''
	def draw():

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

		# interrupts flow of code, user needs to terminate draw to proceed
		plt.show()

		# plt.savefig("path.png")

	'''
	Spits data about the graph in prettyprint
	'''
	def spit_graph_data():

		print('\nThe stations are: ')
		
		nodes = [node for node in G.nodes()]
		for i in range(len(nodes)):
			if i < 9:
				print('\t' + str(i + 1) + '  ' + nodes[i])
			else:
				print('\t' + str(i + 1) + ' ' + nodes[i])

		print('\nThe critical stations are: ')
		count = 0
		for key, value in nx.get_node_attributes(G, 'color').items():
			if value == 'r':
				if count < 9:
					print('\t' + str(count + 1) + '  ' + key)
				else:
					print('\t' + str(count + 1) + ' ' + key)
				count += 1

	'''
	Spits data in lists to be used for algorithms.
	'''
	def spit_data_lists():
		
		# make nodelist
		nodelist = [node for node in G.nodes()]

		# seek minimum weight
		min_edge_weight = min([nx.get_edge_attributes(G,'weight')[edge] for edge in G.edges()])

		# make unique critical edge list
		critical_edge_list = []
		for key, value in nx.get_edge_attributes(G, 'color').items():
			if value == 'r':
					critical_edge_list.append(key)

		# return values
		return nodelist, critical_edge_list, min_edge_weight

	def random_walk(nodelist, minimum_weight, critical_connections):
		
		# start a list of unique critical tracks the random walk traverses
		critical_connections_traversed = []

		# rand number of tracks 1 up to including 7
		# random_tracks = random.randint(1,7)

		random_tracks = 7

		# keep track of critical connections that are not used yet
		delete_counter = 0
		total_time = 0

		# print('START track number is: ' + str(random_tracks))

		for track in range(random_tracks):

			# rand start station 0 up to nodelist length - 1 to pick a node in nodelist
			starting_station = nodelist[random.randint(0,len(nodelist) - 1)]
			# print('+++NEW Starting station is: ' + starting_station)
			# print('+++NEW Neighbors are: {}'.format(G[starting_station]))
			time = 0

			# rand time for a given track
			random_time = random.randint(minimum_weight,120)
			# print('+++NEW track length is going to be: ' + str(random_time))

			counter = 0
			while time < random_time:

				# chooses a random key from a dictionary (neighbors), is choosing a random neighbor

				#random_neighbor = random.choice(G[starting_station]).keys()
				random_neighbor = random.choice(list(G[starting_station]))
				# print('Random choise is: ' + random_neighbor)

				# keeps track of time of the track
				edge_time = G[starting_station][random_neighbor]['weight']
				time += edge_time
				total_time += edge_time

				# always pick one track, catch exception of second track being larger than random time
				if time > random_time and counter != 0:
					#print('        CAUGHT EXCEPTION')
					break
				counter += 1

				# print('The time from: ' + starting_station + ' to ' + random_neighbor + ' is: {}'.format(G[starting_station][random_neighbor]['weight']))
				# print('The total time is: ' + str(time))
		
				# make list of unique traversed critical connections
				if ((starting_station, random_neighbor) in critical_connections) or ((random_neighbor, starting_station) in critical_connections):
					if not ((starting_station, random_neighbor) in critical_connections_traversed) and not ((random_neighbor, starting_station) in critical_connections_traversed):
						critical_connections_traversed.append((starting_station, random_neighbor))

					# print('		DELETED: ' + str((starting_station, random_neighbor)))

				# updates the starting station
				starting_station = random_neighbor
				# print('        Updated neighbors are: {}'.format(G[random_neighbor]))

		# print(critical_connections)
		# print(delete_counter)

		# print("+++++++++++++++++++")
		# print(critical_connections_not_traversed)
		
		# percentage of critical tracs traversed
		score = float(len(critical_connections_traversed)) / float(len(critical_connections))
		
		# score function 1
		S = score * 10000 - (random_tracks * 20 + total_time / 100000)

		# rounds S to nearest 10, otherwhise the amount of columns in bar chart is insane...
		S_10 = round(S, 1)

		return S_10
