import helpers as hlp
import random
import line_analysis as ana
import networkx as nx
import collections # for Hierholzer's
import line_node_class as N
import line_edges_class as E
from copy import deepcopy

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
Hierholzer's algorithm
'''
def hierholzer(graph):

	print("======HIERHOLZER======")

	# for access to the graph
	G = graph.G

	# initializing list for all tracks
	connections_traversed = []

	# adding all edges as tuples to all_edges_list
	all_edge_list = [edge for edge in graph.edges]

	# to keep track of amount of tracks
	track_counter = 0

	# to keep track of time of all tracks combined
	total_time = 0

	# for each track
	while True:

		# make new track object (one for each track)
		track = E.Track(G)

		# keeping track of amount of tracks
		track_counter += 1
	
		# if all edges are traversed
		if all_edge_list == []:

			# counter counted one track too much
			track_counter -= 1

			# break to end the algorithm
			break

		#### dit misschien in functie: dit is allemaal om, voor zover mogelijk, een starting node te krijgen
		# die maar één edge heeft

		# make list with every station as much as they have untraversed edges
		stations_in_edges_amount_list = [elem for t in all_edge_list for elem in t]

		# initalize list for stations with only one untraversed edge
		one_edge_list = []

		# determine which stations have only one edge, adding these to one_edge_list
		counter = collections.Counter(stations_in_edges_amount_list)
		for station, count in counter.items():
			if count == 1:
				one_edge_list.append(station)

		# get random starting station that has only one edge, if possible
		if one_edge_list != []:
			current_node = random.choice(one_edge_list)
		else:
			current_node = random.choice(list(graph.nodes))

		#### eind mogelijke functie


		# loop for each edge in each track
		while True:

			# checking if current station has unused edges
			remaining_edge_check = [item for item in all_edge_list if current_node in item]
			
			# if current_node has no unused edges
			if remaining_edge_check == []:

				# if last track made track longer than max length
				if track.time > 120:

					# remove last edge
					track.remove_edge()

				# add this track to connections traversed
				connections_traversed.append(track)

				# break out of while loop to begin new track
				break

			# choose random neighbor of station
			random_neighbor_node = random.choice(list(G[current_node]))

			# ensure that random neighbor station has several edges (otherwise, this will be the end of the track), if there is more than edge
			if len(all_edge_list) != 1:
				while random_neighbor_node in one_edge_list:
					random_neighbor_node = random.choice(list(G[current_node]))

			# ensure that edge hasn't been traversed yet
			while (current_node, random_neighbor_node) not in all_edge_list and (random_neighbor_node, current_node) not in all_edge_list:
				random_neighbor_node = random.choice(list(G[current_node]))

			# get edge time
			edge_time = G[current_node][random_neighbor_node]['weight']
			
			# keeping track of total time of all tracks
			total_time += edge_time

			# if track is longer than 120 minutes
			if track.time > 120:

				# remove last edge to make length less than 120 minutes
				track.remove_edge()

				# add track to list of all tracks
				connections_traversed.append(track)

				# initialize new track object
				track = E.Track(G)

				# keep track of amount of tracks
				track_counter += 1

			# if track with new edge is not longer than 120 minutes
			else:
				# check in what order edge is stored in all_edge_list
				if (current_node, random_neighbor_node) in all_edge_list:

					# remove edge from all_edge_list
					all_edge_list.remove((current_node, random_neighbor_node))

				elif (random_neighbor_node, current_node) in all_edge_list:

					# remove edge from all_edge_list
					all_edge_list.remove((random_neighbor_node, current_node))

				# add edge to track
				track.add_edge(current_node, random_neighbor_node)	

				# make neighbor node current node, so that this node can go through the while loop to create a track
				current_node = random_neighbor_node

	print("track_counter: ", end="")
	print(track_counter)

	for i in range(track_counter):
		print("time: ", end="")
		print(connections_traversed[i].time)	
	
	score = hlp.get_score(1, track_counter, total_time)
	print("score: ", end="")
	print(score)

	# list of tuples
	return connections_traversed

	# to do
	# - score op andere manier berekenen: via de connections_traversed[i].get_score oid.
	# - deze score ook returnen
	# - misschien: all_edges_list veranderen voor connections_traversed[i].edges: dit geeft precies
	#   het omgekeerde terug, daar kan misschien op de een of andere manier gebruikt worden?
	# - misschien: functie om voorzover mogelijk een random neighbor te krijgen met maar één edge die nog
	#   traversed moet worden. Had Thom niet al zoiets
	
	
def analytical_dfs(graph):

	G = graph.G

	station = 'Den Helder'

	# set starting station
	start = N.Node(station, None)
	previous = 'Start'

	# set start to visited
	start.walked()

	# set track object
	track = E.Track(G)
	track_list = []

	print('begin from: ' + start.name)
	print('_______________________________________')
	while True:

		print('\nStart: {}\n'.format(start.name))
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
		print('\nNeighbors of ' + start.name)
		for neighbor in start.neighbors:
			print('\t' + neighbor.name)

		# loop over neighbors
		for neighbor in start.neighbors:
			print('\tPossible edges: ' + start.name + ', ' + neighbor.name)

			# add the track to the track object
			track.add_edge(start.name, neighbor.name)

			print('\tEdge:       ' + start.name + ', ' + neighbor.name)
			print('\tEdge time:  ' + str(G[start.name][neighbor.name]['weight']))
			print('\tTrack time: ' + str(track.time))
			# set start to selected neighbor and begin new walk
			start.next = neighbor
			print('\tWalked from: ' + start.name + ' -> ' + start.next.name)
			start = neighbor
			previous = start.previous.name

			# found next edge break out of for loop
			break

		# begin walk back change for track_time == 120
		if track.time > 120:
			
			# store track in list
			track_list.append(track) 						# store old track
			track = deepcopy(track)							# copy old track
			track.remove_edge()								# remove last edge
			start = start.previous              			# go back one node

			while True:
				check = start.check_neighbors(track, track_list, G)
				if check == False:
					track.remove_edge()						# remove last edge
					start = start.previous      			# go back one node
				else:
					start.next = check 			  # link found station
					start = check 				  # set start to check
					previous = start.previous.name
					break
