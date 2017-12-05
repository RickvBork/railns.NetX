import helpers as hlp
import random
import line_analysis as ana
import networkx as nx
import collections # for Hierholzer's
import line_node_class as N
import line_edges_class as E

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
	number_of_best_tracks = 5

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

		#append score to all_connections
		all_connections["score"] = s

		# update best track if its score is better than previous best
		if s > best_score:
			best_tracks.append(all_connections)
			best_score = s
		if (len(best_tracks) > number_of_best_tracks):
			best_tracks.pop(0)

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
	#critical_list = graph.critical_station_list
	connections_traversed = []
	G = graph.G

	# adding all edges as tuples to all_edges_list
	all_edge_list = []
	for tuples in graph.edges:
		all_edge_list.append(tuples)

	# making list of all stations
	all_stations_list = list(graph.nodes)

	track_counter = 0
	total_time = 0
	# loop for track
	while True:

		track_counter += 1
		print("track_counter: ", end="")
		print(track_counter)
	
		# breaks if all edges are traversed
		if all_edge_list == []:
			print("break")
			break

		# determines which track this is, and adds this to connections_traversed
		# track_counter += 1
		# track_amount = str(track_counter)
		# connections_traversed.append(track_amount)	

		one_edge_list = []
		# if item in tuple of all_edge_list count is 1, add to one_edge_list.
		test = [elem[0] for elem in all_edge_list]
		test2 = [elem[1] for elem in all_edge_list]
		test3 = test + test2
		counter = collections.Counter(test3)
		for station, count in counter.items():
			if count == 1:
				one_edge_list.append(station)

		# get random starting station that has only one edge, if possible
		if one_edge_list != []:
			current_node = random.choice(one_edge_list)
		else:
			current_node = random.choice(all_stations_list)

		#print("!!!!!!!!!!!!!!")

		# loop for edges in track
		while True:

			#print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
			# checking if station has unused edges.
			remaining_edge_check = [item for item in all_edge_list if current_node in item]
			
			# if current_node has no unused edges: beginning of new track, so break out of while loop
			if remaining_edge_check == []:
				break

			# choose random neighbor of station
			random_neighbor_node = random.choice(list(G[current_node]))

			# ensure that random neighbor station has several edges (otherwise, this will be the end of the track)
			if len(all_edge_list) != 1:
				while random_neighbor_node in one_edge_list:
					random_neighbor_node = random.choice(list(G[current_node]))

			# ensure that edge hasn't been traversed yet (vrij zeker dat dit werkt, niet 100%: is die 'and' oke?)
			while (current_node, random_neighbor_node) not in all_edge_list and (random_neighbor_node, current_node) not in all_edge_list:
				random_neighbor_node = random.choice(list(G[current_node]))

			# remove traversed edge from all_edge_list, and add traversed edge to connections traversed to keep track of route
			if (current_node, random_neighbor_node) in all_edge_list:
				all_edge_list.remove((current_node, random_neighbor_node))
				connections_traversed.append((current_node, random_neighbor_node))
			if (random_neighbor_node, current_node) in all_edge_list:
				all_edge_list.remove((random_neighbor_node, current_node))
				connections_traversed.append((random_neighbor_node, current_node))
			
			print(current_node, random_neighbor_node)

			track_time = G[current_node][random_neighbor_node]['weight']
			print("track_time", end="")
			print(track_time)

			total_time += track_time
			print("total_time", end="")
			print(total_time)

			current_node = random_neighbor_node
		
	# list of tuples
	score = hlp.get_score(1, track_counter, total_time)
	print("score", end="")
	print(score)

	return connections_traversed

	# HIERHOLZER DEEL II:
	# je hebt dus een list met tuples met daarin stations. tracks aan elkaar plakken: hiervoor nieuwe tracks beginnen bij een node
	# die al in 
	
def analytical_dfs(graph):

	G = graph.G

	station = 'Den Helder'

	# set starting station
	start = N.Node(station, None)
	previous = 'Start'

	# set start to visited
	start.walked()

	# set track object
	track = E.Edges(G)

	track_time = 0
	print('begin from: ' + start.name)
	print('_______________________________________')
	while True:

		print('\nStart: ' + start.name)
		print('Previous ' + previous)

		# for every neighbor of station, add neighbors as new Nodes with start as the previous Node
		for station in G[start.name]:

			if station == previous:
				print('\tStation neglected:  ' + station)
			if station != previous:
				print('\tStation added:\t    ' + station)

				# add all neighbors except previous node
				start.add_neighbor(N.Node(station, start))

		# DEBUG
		print('Neighbors of ' + start.name)
		for neighbor in start.neighbors:
			print('\t' + neighbor.name)

		# loop over neighbors
		for neighbor in start.neighbors:
			print('\tPossible edges: ' + start.name + ', ' + neighbor.name)

			# if one hasn't been visited
			if neighbor.visited == 'n':

				# append time of edge to track time
				track_time += G[start.name][neighbor.name]['weight']

				track.time += G[start.name][neighbor.name]['weight']

				# set neighbor to visited
				neighbor.walked()

				track.add_edge(tuple((start.name, neighbor.name)))

				print('\tEdge:       ' + start.name + ', ' + neighbor.name)
				print('\tEdge time:  ' + str(G[start.name][neighbor.name]['weight']))
				print('\tTrack time: ' + str(track_time))
				# set start to selected neighbor and begin new walk
				start.next = neighbor
				print('\tWalked from: ' + start.name + ' -> ' + start.next.name)
				start = neighbor
				previous = start.previous.name

				# found next edge break out of for loop
				break

			elif neighbor.visited == 'y':
				print('Found Loop')
				# check if the neighbor has neighbors that have not been visited
				break

		# begin walk back change for track_time == 120
		if track_time > 120:
			print(track.get_score())
			break
