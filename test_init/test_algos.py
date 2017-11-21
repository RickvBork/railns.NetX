import test_helpers
import random

'''
Pure, random walk. No heuristics.
Takes a graph object and an iterator.
'''
def random_walk(graph, iterator):

	# get information from graph to perform algorithm
	nodelist = graph.nodes
	minimum_weight = graph.minimal_edge_weight
	critical_connections = graph.critical_edge_list
	total_critical_connections = graph.total_critical_edges
	G = graph.G
	hlp = test_helpers

	# set lists
	p_list = []
	s_list = []
	best_tracks = []
	best_score = - 141

	# do the walk iterator amount of times
	for i in range(iterator):

		# start a list of unique critical tracks the random walk traverses
		critical_connections_traversed = []

		# begin new track dict
		all_connections = {"tracks": {}, "score": None}

		# rand number of tracks 1 up to including 7
		random_tracks = random.randint(1, 7)

		print("Track number: {}".format(random_tracks))

		# keep track of critical connections that are not used yet
		total_time = 0

		# builds the service of multiple tracks
		for track in range(random_tracks):

			# begin new dict with lists
			all_connections["tracks"][str(track)] = []

			# rand start station 0 up to nodelist length - 1 to pick a node in nodelist
			starting_station = random.choice(nodelist)

			print("Begin walk: {}".format(starting_station))

			# keeps track of the time of one track of a service
			track_time = 0

			# random time for a given track
			random_time = random.randint(minimum_weight, 120)

			print("Track maximum time: {}".format(random_time))

			counter = 0
			while track_time < random_time:

				#random_neighbor = random.choice(G[starting_station]).keys()
				random_neighbor = random.choice(list(G[starting_station]))

				# keeps track of time of the track
				edge_time = G[starting_station][random_neighbor]['weight']
				track_time += edge_time

				# append each new edge to track
				all_connections["tracks"][str(track)].append((starting_station, random_neighbor))
				
				# always pick one track
				if ((edge_time > random_time) and counter != 0) or (edge_time > random_time - track_time):
					print("		Exception!")
					break
				counter += 1

				# update traversed critical connections as long as not all have been covered
				if len(critical_connections_traversed) != total_critical_connections:
					critical_connections_traversed = hlp.update_critical_connections_travesed((starting_station, random_neighbor), critical_connections, critical_connections_traversed)
				else:
					print("`GOT EM!") # yeah right...

				# updates the starting station
				starting_station = random_neighbor
				print("		Next station: {}".format(random_neighbor))
				print("			Edge time is: {}".format(edge_time))
				print("			Total time is: {}".format(track_time))
				print("-------------------------------------------------")

			# total time of the service
			total_time = track_time

			print("This service will take {}min\n".format(track_time))
		
		# percentage of critical tracs traversed
		p = hlp.get_p(critical_connections_traversed, critical_connections)
		p_list.append(p)

		# append score
		s = hlp.get_score(p, random_tracks, total_time)
		s_list.append(s)

		# update best track if its score is better than previous best
		if s > best_score:
			best_tracks.append(all_connections)
			best_score = s

		all_connections["score"] = s

		print("Connections made:")
		for i in range(random_tracks):
			print("Track {}:	".format(i + 1))
			edgeList = all_connections["tracks"][str(i)]
			score = all_connections["score"]
			for edge in edgeList:
				print("		{}".format(edge))
		print("Score: {}".format(score))

	return s_list, p_list, best_tracks



'''
Smart 'random' walk
'''

def smart_random_walk(graph, iterator):

	# get information from graph to perform algorithm
	nodelist = graph.nodes
	minimum_weight = graph.minimal_edge_weight
	critical_connections = graph.critical_edge_list
	total_critical_connections = graph.total_critical_edges
	G = graph.G
	hlp = test_helpers

	# set lists
	p_list = []
	s_list = []
	best_tracks = []
	best_score = - 141

	# do the walk iterator amount of times
	for i in range(iterator):

		# start a list of unique critical tracks the random walk traverses
		critical_connections_traversed = []

		# begin new track dict
		all_connections = {"tracks": {}, "score": None}

		# rand number of tracks 1 up to including 7
		random_tracks = 7

		print("Track number: {}".format(random_tracks))

		# keep track of critical connections that are not used yet
		total_time = 0

		# builds the service of multiple tracks
		for track in range(random_tracks):

			# begin new dict with lists
			all_connections["tracks"][str(track)] = []

			# rand start station 0 up to nodelist length - 1 to pick a node in nodelist
			# take a random critical station as starting station instead of a total random station
			starting_station = random.choice(graph.critical_station_list)

			print("Begin walk: {}".format(starting_station))

			# keeps track of the time of one track of a service
			track_time = 0

			# Use maximum time for each train (as opposed to random time)
			random_time = 120

			print("Track maximum time: {}".format(random_time))

			counter = 0
			while track_time < random_time:
				
				# get list of critical neighbours of starting_station
				critical_neighbors = [station for station in list(graph.G[starting_station]) if station in graph.critical_station_list]
				

				if critical_neighbors == []:
					random_neighbor = random.choice(list(G[starting_station]))
				else: 
					random_neighbor = random.choice(critical_neighbors)

				# keeps track of time of the track
				edge_time = G[starting_station][random_neighbor]['weight']
				track_time += edge_time

				# append each new edge to track
				all_connections["tracks"][str(track)].append((starting_station, random_neighbor))
				
				# always pick one track
				if ((edge_time > random_time) and counter != 0) or (edge_time > random_time - track_time):
					print("		Exception!")
					break
				counter += 1

				# update traversed critical connections as long as not all have been covered
				if len(critical_connections_traversed) != total_critical_connections:
					critical_connections_traversed = hlp.update_critical_connections_travesed((starting_station, random_neighbor), critical_connections, critical_connections_traversed)
				else:
					print("`GOT EM!") # yeah right...

				# updates the starting station
				starting_station = random_neighbor
				print("		Next station: {}".format(random_neighbor))
				print("			Edge time is: {}".format(edge_time))
				print("			Total time is: {}".format(track_time))
				print("-------------------------------------------------")

			# total time of the service
			total_time = track_time

			print("This service will take {}min\n".format(track_time))
		
		# percentage of critical tracs traversed
		p = hlp.get_p(critical_connections_traversed, critical_connections)
		p_list.append(p)

		# append score
		s = hlp.get_score(p, random_tracks, total_time)
		s_list.append(s)

		# update best track if its score is better than previous best
		if s > best_score:
			best_tracks.append(all_connections)
			best_score = s

		all_connections["score"] = s

		print("Connections made:")
		for i in range(random_tracks):
			print("Track {}:	".format(i + 1))
			edgeList = all_connections["tracks"][str(i)]
			score = all_connections["score"]
			for edge in edgeList:
				print("		{}".format(edge))
		print("Score: {}".format(score))

	return s_list, p_list, best_tracks

''''
HIERHOLZER
'''

def hierholzer(graph):

		# list of tuples: to add used edges, that is two nodes that share that edge
	list = graph.critical_station_list
	connections_traversed = []

	current_node = random.choice(graph.nodes)
	print(current_node)

		# ensure that starting node is critical station
	while current_node not in list:
		current_node = random.choice(graph.nodes)
		#print(current_node)
			
	while True:

		boolean_edges_unused = False

			# to check if current_node has any unused edges
		while boolean_edges_unused == False:

			# error: hoe krijg ik alle edges?
			for current_node in graph.edges:
				# BUT: saved in G.edges as tuple, does this search work?
				node_in_edges += 1

			for current_node in connections_traversed:
				# BUT: saved as tuple..: ?
				# item for item in G.edges if current_node in item
				# zorgen dat het beneden bij append aan deze lijst wel zo opgeslagen wordt als de G.edges, anders werkt dat met de counter niet.
				node_in_used_edges += 1

				# if current_node has no unused edges
			if node_in_edges == node_in_used_edges:
				current_node = random.choice(graph.nodes)
				# if current_node has some unused edges
			else:
				boolean_edges_unused = True

		random_neighbor_node = random.choice(all_neighbors(G, current_node))

			# choose random new neighbor node until you find one with unused edge.
		while ((current_node, random_neighbor_node) in connections_traversed) or ((random_neighbor_node, current_node) in connections_traversed):
			random_neighbor_node = random.choice(all_neighbors(G, current_node))
			print(random_neighbor_node)
				# in random_walk: random_neighbor = random.choice(list(G[current_node])); welke list? nog even checken.

			# add now used edge to critical_connections_traversed
		connections_traversed.append(current_node, random_neighbor_node)
			# BUT: hoe wordt het precies opgeslagen in G.edges? wordt de tuple daar ook andersom opgeslagen? voor de boolean_unused_edges

			# change current_node to random_neighbor_node
		current_node = random_neighbor_node
			
		if len(connections_traversed) == len(graph.edges):
			break;	

		# returns list of tuples so you can, "by hand" follow the path
	return connections_traversed

	
#It is not possible to get stuck at any vertex other than v, because indegree and outdegree of every vertex must be same, 
#when the trail enters another vertex w there must be an unused edge leaving w. ---- lijkt mij: it is not possible to get stuck, because it is a 
# Eulerian cycle.

#The tour formed in this way is a closed tour, but may not cover all the vertices and edges of the initial graph.
#As long as there exists a vertex u that belongs to the current tour but that has adjacent edges not part of the tour, 
#start another trail from u, following unused edges until returning to u, and join the tour formed in this way to the previous tour.

#Thus the idea is to keep following unused edges and removing them until we get stuck. Once we get stuck, we back-track to 
#the nearest vertex in our current path that has unused edges, and we repeat the process until all the edges have been used. We can use another container to mainta

