import csv
import networkx as nx
import matplotlib.pyplot as plt
import tkinter # by thom, because of some run errors
import random

G = nx.Graph()

def return_p(critical_tracks_covered, total_critical_tracks):
	return float(len(critical_connections_traversed)) / float(len(critical_connections))

def return_score(p, t, min):
	return p * 10000 - (random_tracks * 20 + total_time / 100000)

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

	def random_walk(nodelist, minimum_weight, critical_connections, simulations = 100):
		
		score = []
		critical_track_coverage = []
		for i in range(simulations):

			# start a list of unique critical tracks the random walk traverses
			critical_connections_traversed = []

			# rand number of tracks 1 up to including 7
			random_tracks = random.randint(1,7)

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
			p = return_p(critical_connections_traversed, critical_connections)

			score = return_score(p, random_tracks, total_time)

			# append to lists
			score.append(return_score(p, random_tracks, total_time))
			critical_track_coverage.append(p)

		return score, critical_track_coverage

		
		# voor commit even checken of dat hierboven nog klopt!!
	def hierholzer(self, critical_station_list):
		#a directed graph has an Eulerian cycle if following conditions are true 
		#(1) All vertices with nonzero degree belong to a single strongly connected component. 
		#(2) In degree and out degree of every vertex is same. The algorithm assumes that the given graph has Eulerian Circuit.

		# list of tuples: to add used edges, that is two nodes that share that edge
		used_edge_list = []
		# in Hierholzer's they use a complete list of edges, and delete edges from this. Is that faster? Don't know how to do this... 

		current_node;

		# ensure that starting node is critical station
		while current_node not in critical_station_list:
			current_node = random.choice(G.nodes())
			# BUT: in critical_edge_list there are tuples: does this work? see also below with used_edge_list
			# BUT: there might be repetitions in random choice... something with range()? Because of repetitions, this might be slower
			# de random choice etc. ook bij randomwalk
			# print(current_node)

		# BUT: needs to stop when all edges are used: misschien met time? 
		while True:

			boolean_edges_unused = False

			# to check if current_node has any unused edges
			while boolean_edges_unused == False:

				for current_node in G.edges():
				# BUT: saved in G.edges as tuple, does this search work?
					counter1 += 1

				for current_node in used_edge_list:
				# BUT: saved as tuple..
				# zorgen dat het beneden bij append aan deze lijst wel zo opgeslagen wordt als de G.edges, anders werkt dat met de counter niet.
					counter2 += 1

				# if current_node has no unused edges
				if counter1 == counter2:
					current_node = random.choice(G.nodes())
					# BUT: the node now chosen might not be critical: is this bad? no, because after first current_node, it doesn't really matter I think.
					# BUT: the node can have been critical already.
					# misschien: hier een break doen. Op dit punt misschien een heel nieuw startpunt nemen (wel met een nieuwe current, dus op zich oet je zo verder.
					# maar het is gewoon niet erg duidelijk aangegeven.)
					# misschien2: backtracken om zo een langer traject te maken? Maar dat is wel lastig denk ik, en dan duurt het langer..
				# if current_node has some unused edges
				else:
					boolean_edges_unused = True

			random_neighbor_node;

			# choose random new neighbor node until you find one with unused edge.
			while (current_node, random_neighbor_node) in used_edge_list or (random_neighbor_node, current_node) in used_edge_list:
				random_neighbor_node = random.choice(all_neighbors(G, current_node))
				# in random_walk: random_neighbor = random.choice(list(G[current_node])); welke list? nog even checken.

			# add now used edge to used_edge_list
			used_edge_list.append(current_node, random_neighbor_node)
			# BUT: hoe wordt het precies opgeslagen in G.edges? wordt de tuple daar ook andersom opgeslagen? voor de boolean_unused_edges

			# change current_node to random_neighbor_node
			current_node = random_neighbor_node
								
		# returns list of tuples so you can, "by hand" follow the path
		return used_edge_list


	# after while loop: check if all edges are in used_edge_list
	# if so, yee!
	# if not, new current node that is not in list?

		


#It is not possible to get stuck at any vertex other than v, because indegree and outdegree of every vertex must be same, 
#when the trail enters another vertex w there must be an unused edge leaving w. ---- lijkt mij: it is not possible to get stuck, because it is a 
# Eulerian cycle.

#The tour formed in this way is a closed tour, but may not cover all the vertices and edges of the initial graph.
#As long as there exists a vertex u that belongs to the current tour but that has adjacent edges not part of the tour, 
#start another trail from u, following unused edges until returning to u, and join the tour formed in this way to the previous tour.

#Thus the idea is to keep following unused edges and removing them until we get stuck. Once we get stuck, we back-track to 
#the nearest vertex in our current path that has unused edges, and we repeat the process until all the edges have been used. We can use another container to maintain the final path.
