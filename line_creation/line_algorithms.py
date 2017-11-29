import helpers as hlp
import random
import line_analysis as ana

'''
Pure, random walk. No heuristics.
Takes a graph object and an iterator.
'''
def random_walk(Graph, iterator):

	# get information from graph to perform algorithm
	nodelist = Graph.nodes
	minimum_weight = Graph.minimal_edge_weight
	critical_connections = Graph.critical_edge_list
	total_critical_connections = Graph.total_critical_edges
	G = Graph.G

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
		random_tracks = 7

		# print("Track number: {}".format(random_tracks))

		# keep track of critical connections that are not used yet
		total_time = 0

		# builds the service of multiple tracks
		for track in range(random_tracks):

			# begin new dict with lists
			all_connections["tracks"][str(track)] = []

			# rand start station 0 up to nodelist length - 1 to pick a node in nodelist
			starting_station = random.choice(nodelist)

			# print("Begin walk: {}".format(starting_station))

			# keeps track of the time of one track of a service
			track_time = 0

			# random time for a given track
			random_time = random.randint(minimum_weight, 120)
			random_time = 120

			# print("Track maximum time: {}".format(random_time))

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
					# print("		Exception!")
					break
				counter += 1

				# update traversed critical connections as long as not all have been covered
				if len(critical_connections_traversed) != total_critical_connections:
					critical_connections_traversed = hlp.update_critical_connections_travesed((starting_station, random_neighbor), critical_connections, critical_connections_traversed)
				else:
					print("`GOT EM!") # yeah right...

				# updates the starting station
				starting_station = random_neighbor
				# print("		Next station: {}".format(random_neighbor))
				# print("			Edge time is: {}".format(edge_time))
				# print("			Total time is: {}".format(track_time))
				# print("-------------------------------------------------")

			# total time of the service
			total_time = track_time

			# print("This service will take {}min\n".format(track_time))
		
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

		# all_connections["score"] = s

		# print("Connections made:")
		# for i in range(random_tracks):
		# 	print("Track {}:	".format(i + 1))
		# 	edgeList = all_connections["tracks"][str(i)]
		# 	score = all_connections["score"]
		# 	for edge in edgeList:
		# 		print("		{}".format(edge))
		# print("Score: {}".format(score))

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
	#hlp = test_helpers

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
				
				prefered_neighbors = hlp.get_prefered_neighbors(graph, starting_station, all_connections, track)

				if prefered_neighbors == []:
					random_neighbor = random.choice(list(G[starting_station]))
				else: 
					random_neighbor = random.choice(prefered_neighbors)

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
Hierholzer's algorithm (v2)
'''

def hierholzer(graph):

	print("======HIERHOLZER======")
	# list of tuples: to add used edges, that is two nodes that share that edge
	critical_list = graph.critical_station_list
	connections_traversed = []
	one_edge_list = []
	#all_edges_list = graph.edges
	G = graph.G

	# setting all edges in list
	tuple_list = []
	all_edge_list = []
	for tuple in graph.edges:
	 	all_edge_list.append(tuple_list)
	 	tuple_list = []
	 	for item in tuple:
	 		tuple_list.append(item)
	 		print("item")
	 		print(item)

	print("all_edges_list:")
	print(all_edge_list)


	## checking which station have only one connection, and adding those to one_edge_list
	# iterate over every station
	for station in graph.nodes:
		breaker = 0
		counter = 0
		# iterate over every edge
		for tuple in graph.edges:
			# to break out of this for loop if critical station has more than one edge
			if breaker == 1:
				break
			# iterate over every node in edge
			for item in tuple:
				# to break out of this for loop if critical station has more than one edge
				if breaker == 1:
					break
				# if node is equal to station that is checked now
				if item == station:
					# counter for every edge the station has
					counter += 1
					# to break out if critical station has more than one edge
					if counter > 1:				
						breaker = 1
		if counter == 1:
			one_edge_list.append(station)
	## end: checking which stations have one connections and adding to one_edge_list

	# get random starting station that has only one edge
	current_node = random.choice(one_edge_list)

	# # check if current node has unused edges
	# boolean_node = False
	# breaker2 = 0
	# while boolean_node == False:
	# 	for tuple in all_edges_list:
	# 		if breaker2 = 1
	# 			break
	# 		for item in tuple:
	# 			if item == current_node:
	# 				breaker2 = 1
	# 				# in dit geval kan je uit de loop
	# 				boolean_node = True
	# 				# if current_node is in one_edge_list, delete it from that list
	# 	# if current_node has no unused edges, choose new one
	# 	if breaker2 == 0:
	# 		if one_edge_list:
	# 			current_node = random.choice(one_edge_list)
	# 			# delete from one_edge_list
	# 		else:
	# 			current_node = random.choice(graph.nodes)
	# 			# maar, nu wordt niet per se de optimale keuze wordt hier gemaakt,
			

	# eerst dit hierbeneden testen met dit hierboven op comment!!!
	#####
	
	# choose random neighbor of station
	random_neighbor_node = random.choice(list(G[current_node]))

	# ensure that random neighbor station has several edges (otherwise, this will be the end of the track)
	while random_neighbor_node in one_edge_list:
		random_neighbor_node = random.choice(list(G[current_node]))
	
	# ensure that edge hasn't been traversed yet
	while ((random_neighbor_node, current_node) not in all_edge_list) or ((current_node, random_neighbor_node) not in all_edge_list):
		random_neighbor_node = random.choice(list(G[current_node]))

	# dit werkt dus niet....
	# if (random_neighbor_node, current_node) in all_edges_list:
	# 	all_edges_list.remove(random_neighbor_node, current_node)
	# if (current_node, random_neighbor_node) in all_edges_list:
	# 	all_edges_list.remove(current_node, random_neighbor_node)

	# maar, 

	# # check:
	print("current_node, random_neighbor_node")
	print(current_node, random_neighbor_node)
	print("all_edges_list")
	print(all_edges_list)
			

	


			
	while True:

		boolean_edges_unused = False

		# to check if current_node has any unused edges
		while boolean_edges_unused == False:

			node_in_edges = 0;
			node_in_used_edges = 0;

			for edge_tuple in graph.edges:
				if current_node in edge_tuple:
					node_in_edges += 1
					print("node_in_edges")
					print(node_in_edges)

			for edge_tuple in connections_traversed:
				if current_node in edge_tuple:
					node_in_used_edges += 1
					print("node_in_used_edges")
					print(node_in_used_edges)

			# if current_node has no unused edges pick new current_node
			if node_in_edges == node_in_used_edges:
				#print(node_in_edges)
				#print(node_in_used_edges)
				current_node = random.choice(graph.nodes)
				print(current_node)
				connections_traversed.append("NEW TRACK")
				# BUT: ALS ER NOG NODES ZIJN MET MAAR ÉÉN EDGE, DAN DIE KIEZEN
			# if current_node has some unused edges, continue
			else:
				boolean_edges_unused = True

		#print("ZZZZZ")

		#print(current_node)
		
		random_neighbor_node = random.choice(list(G[current_node]))

		# lukt, en is ook neighbor
		#print(random_neighbor_node)

		print("next while loop")

		# choose random new neighbor node until you find one with unused edge.
		while ((current_node, random_neighbor_node) in connections_traversed) or ((random_neighbor_node, current_node) in connections_traversed):
			random_neighbor_node = random.choice(list(G[current_node]))
			print(random_neighbor_node)

		# # add now used edge to critical_connections_traversed: error hier: ik wil een tupple toevoegen.
		connections_traversed.append((current_node, random_neighbor_node))

		print("connections_traversed", end="")
		print(connections_traversed)
		# print("conn")

			# BUT: hoe wordt het precies opgeslagen in G.edges? wordt de tuple daar ook andersom opgeslagen? voor de boolean_unused_edges

			# change current_node to random_neighbor_node
		current_node = random_neighbor_node
			
		if len(connections_traversed) == len(G.edges):
			break;	

		# returns list of tuples so you can, "by hand" follow the path
	return connections_traversed
