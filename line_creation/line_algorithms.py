import helpers as hlp
import random
import line_analysis as ana
import networkx as nx
import collections # for Hierholzer's
import line_node_class as N
import track_class as T
import service_class as S
from copy import deepcopy
import service_class as sc
# from time import sleep

'''
Pure, random walk. No heuristics. Takes a graph object and an iterator as arguments. Returns an unordered list of 5 best service classes.
'''
def random_walk(Graph, iterator):

	G = Graph.G
	minimum_weight = Graph.minimal_edge_weight
	nodes = Graph.nodes

	# build node structure
	node_list = hlp.get_node_list(G, nodes)

	# initialise list for best services
	max_service_amount = 5
	best_services = [0] * max_service_amount

	best_score = - 140
	i = 0

	# initiate loading bar
	hlp.loading_bar(0, iterator, prefix = 'Progress:', suffix = 'Complete', length = 50, update = 100)

	for j in range(iterator):

		# build service loop
		service = sc.service(G)
		for k in range(random.randint(1, 7)):

			track = T.track(G)
			max_track_length = random.randint(minimum_weight, 120)
			start = random.choice(node_list)

			# build track loop
			while track.time < max_track_length:

				# choose random neighbor node
				neighbor = random.choice(start.neighbors)

				# add built edge
				track.add_edge((start.name, neighbor.name))

				# update start
				start = neighbor

			# make sure track is minimum of one edge
			if len(track.edges) != 1:
				track.remove_edge()

			# add new track to service
			service.add_track(track)

		score = service.s_score

		# remember best scores (unordered)
		if score > best_score:
			best_services[i % max_service_amount] = service
			best_score = score
			i += 1

		# update loading bar
		hlp.loading_bar(j, iterator, prefix = 'Progress:', suffix = 'Complete', length = 50, update = 100)

	# remove empty values as list is not always filled
	return [service for service in best_services if service != 0]

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

	# initializing list for all tracks
	connections_traversed = []

	# for access to the graph
	G = graph.G

	# initialize service
	service = S.service(graph)

	# adding all edges as tuples to all_edges_list
	all_edge_list = [edge for edge in graph.edges]

	# to keep track of amount of tracks
	track_counter = 0

	# to keep track of time of all tracks combined
	total_time = 0

	# for each track
	while True:

		# make new track object (one for each track)
		track = T.track(graph)

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

				service.add_track(track)

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

				service.add_track(track)

				# initialize new track object
				track = T.track(graph)

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
				track.add_edge((current_node, random_neighbor_node))

				# for possibly adding tracks together later on
				track.add_station(current_node, random_neighbor_node)

				# make neighbor node current node, so that this node can go through the while loop to create a track
				current_node = random_neighbor_node

	print("track_counter: ", end="")
	print(track_counter)

	for i in range(track_counter):
		print("time: ", end="")
		print(connections_traversed[i].time)


	tmp_new_track_list = []

	# iterate over all tracks
	for i in range(len(service.tracks)):
		# for each track, iterate over all other tracks
		for j in range(len(service.tracks)):
			# ensure that track is not compared to same track
			if i != j:
				# if track time combined is less than the maximum time
				if (service.tracks[i].time + service.tracks[j].time) < 120:
					# if starting station for both stations is the same
					if service.tracks[i].edges[0][0] == service.tracks[j].edges[0][0]:


						# kleine bug: in dit geval (starting + starting) wordt er twee keer hierdoor heen gegaan, aangezien i en j allebei i en j zijn
						# het resultaat: twee keer wordt aan tmp_new.. een track toegevoegd. deze is identiek, behalve dat deze helemaal
						# reversed is

						# nog een kleine bug: bij starting + ending, en ending + starting, kan het ook dubbel. Het resultaat is dat aan tmp_new.. twee keer
						# een deze keer compleet identieke lijst wordt toegevoeg.

						print("starting + starting")

						reversed_list = []
						partially_reversed_list = list(reversed(service.tracks[j].edges))
						for item in partially_reversed_list:
							reversed_list.append(tuple(reversed(item)))

						# make new list with edges of new track
						combined_list = reversed_list + connections_traversed[i].edges
						
						# add new route to tmp list
						tmp_new_track_list.append(combined_list)

						# indicate that track can later be removed from service
						service.tracks[i].necessary = False
						service.tracks[j].necessary = False

						# update track counter
						track_counter -=1
					
					# if starting station and ending station is the same
					elif service.tracks[i].edges[0][0] == service.tracks[j].edges[-1][1]:

						print("starting + ending")
						combined_list = service.tracks[j].edges + service.tracks[i].edges
						print("combined_list B: check")
						print(combined_list)
						
						# add new route to tmp list
						tmp_new_track_list.append(combined_list)

						# indicate that track can later be removed from service
						service.tracks[i].necessary = False
						service.tracks[j].necessary = False

						# update track counter
						track_counter -=1

					# if ending station and starting station is the same
					elif service.tracks[i].edges[-1][1] == service.tracks[j].edges[0][0]:

						print("ending + starting")
						combined_list = service.tracks[i].edges + service.tracks[j].edges
						print("combined_list C: check")
						print(combined_list)

						# add new route to tmp list
						tmp_new_track_list.append(combined_list)

						# indicate that track can later be removed from service
						service.tracks[i].necessary = False
						service.tracks[j].necessary = False

						# update track counter
						track_counter -=1

					# if ending station for both tracks is the same
					elif service.tracks[i].edges[-1][1] == service.tracks[j].edges[-1][1]:
						print("ending + ending")

						print("service tracks not yet reversed:")
						print(service.tracks[j].edges)

						reversed_list = []
						partially_reversed_list = list(reversed(service.tracks[j].edges))
						for item in partially_reversed_list:
							reversed_list.append(tuple(reversed(item)))

						print("reversed list:")
						print(reversed_list)

						# achter elkaar plakken
						combined_list = service.tracks[i].edges + reversed_list
						print("combined_list D: ?")
						print(combined_list)

						# add new route to tmp list
						tmp_new_track_list.append(combined_list)

						# indicate that track can later be removed from service
						service.tracks[i].necessary = False
						service.tracks[j].necessary = False

						# update track counter
						track_counter -=1	

	# remove all redundant tracks from service class
	for track in service.tracks:
		if track.necessary == False:
			service.remove_track
		elif track.necessary == True:
			print("sdgah")

	for item in tmp_new_track_list:
		track = T.track(graph)
		track.add_edge_list(item)
		service.add_track(track)		

	
	#################################################

	# print("connections_traversed time times two")

	# new_connections_traversed = connections_traversed

	# # iterate over all tracks
	# for i in range(len(connections_traversed)):
	# 	print("i: ", end="")
	# 	print(i)
	# 	# if track exists
	# 	try:
	# 	#if connections_traversed[i]:
	# 		# if track is, when traversed twice, shorter than maximum time
	# 		if (connections_traversed[i].time * 2) < 120:
	# 			# iterate over every station in track
	# 			for station in connections_traversed[i].stations:
	# 				# iterate over all tracks
	# 				for j in range(len(connections_traversed)):
	# 					print("J : ", end="")
	# 					print(j)
	# 					# if this track exists
	# 					try:
	# 						connections_traversed[j]
	# 						# if this track is, hopefully, not the same track as itself
	# 						if connections_traversed[j] != connections_traversed[i]:
	# 							# if station from track is also a station in another track
	# 							if station in connections_traversed[j].stations:
	# 								# if the other track has a track time less than the maximum track time
	# 								if connections_traversed[j].time < 120:
	# 									# if the first track, with the time twice, plus the time from the second track, is less than maxiumum time
	# 									if (connections_traversed[j].time + (connections_traversed[i].time * 2)) < 120:
	# 										print(station)

	# 										# if station is first station in first edge (beginning station)
	# 										if station in connections_traversed[i].edges[0][0]:
												
	# 											# if station from other track is first (beginning station)
	# 											if station in connections_traversed[j].edges[0][0]:

	# 												print("A")

	# 												# reverse the entire second track, so that the two tracks can be combined
	# 												reversed_list = []
	# 												partially_reversed_list = list(reversed(connections_traversed[j].edges))
	# 												for item in partially_reversed_list:
	# 													reversed_list.append(tuple(reversed(item)))

	# 												# make new list with edges of new track
	# 												combined_list = reversed_list + connections_traversed[i].edges
													
	# 												# initialize new track object
	# 												track = T.track(graph)

	# 												# add all edges to make complete track to new track
	# 												track.add_edge_list(combined_list)

	# 												# remove redundant tracks: maar dit moet dus niet. Gewoon nieuwe lijst aanmaken waarin dit niet voorkomt.
	# 												new_connections_traversed.remove(connections_traversed[i])
	# 												new_connections_traversed.remove(connections_traversed[j])

	# 												# add new combined track
	# 												new_connections_traversed.append(track)

	# 												track_counter -=1

	# 											# if station in other track is last station
	# 											elif station in connections_traversed[j].edges[len(connections_traversed[j].edges) - 1][1]:
													
	# 												# direct achter elkaar plakken zonder om te draaien:
	# 												combined_list = connections_traversed[j].edges + connections_traversed[i].edges
	# 												print("combined_list B: check, klopt!")
	# 												print(combined_list)

	# 												# initialize new track object
	# 												track = T.track(graph)

	# 												# add all edges to make complete track to new track
	# 												track.add_edge_list(combined_list)

	# 												# remove redundant tracks
	# 												new_connections_traversed.remove(connections_traversed[i])
	# 												new_connections_traversed.remove(connections_traversed[j])

	# 												# add new combined track
	# 												new_connections_traversed.append(track)

	# 												# update track counter
	# 												track_counter -= 1

	# 										# if station is last statin in last edge (final station)
	# 										elif station in connections_traversed[i].edges[len(connections_traversed[i].edges) - 1][1]:

	# 											# if station from other track is first (beginning station)
	# 											if station in connections_traversed[j].edges[0][0]:

	# 												# C: een route achter elkaar.
	# 												combined_list = connections_traversed[i].edges + connections_traversed[j].edges
	# 												print("combined_list C: check")
	# 												print(combined_list)
	# 												# check: de combined list klopt

	# 												# initialize new track object
	# 												track = T.track(graph)

	# 												# add all edges to make complete track to new track
	# 												track.add_edge_list(combined_list)

	# 												# remove redundant tracks
	# 												new_connections_traversed.remove(connections_traversed[i])
	# 												new_connections_traversed.remove(connections_traversed[j])

	# 												# add new combined track
	# 												new_connections_traversed.append(track)

	# 												# update track counter
	# 												track_counter -= 1

	# 											# if station in other track is last station
	# 											elif station in connections_traversed[j].edges[len(connections_traversed[j].edges) - 1][1]:
													
	# 												# een van de twee omdraaien
	# 												reversed_list = []
	# 												partially_reversed_list = list(reversed(connections_traversed[j].edges))
	# 												for item in partially_reversed_list:
	# 													reversed_list.append(tuple(reversed(item)))

	# 												# achter elkaar plakken
	# 												combined_list = connections_traversed[i].edges + reversed_list
	# 												print("combined_list D")
	# 												print(combined_list)

	# 												# initialize new track object
	# 												track = T.track(graph)

	# 												# add all edges to make complete track to new track
	# 												track.add_edge_list(combined_list)

	# 												# remove redundant tracks
	# 												new_connections_traversed.remove(connections_traversed[i])
	# 												new_connections_traversed.remove(connections_traversed[j])

	# 												# add new combined track
	# 												new_connections_traversed.append(track)

	# 												# update track counter
	# 												track_counter -= 1

	# 										# if station is in middle: (misschien dit checken voor andere twee?)
	# 										else:

	# 											# if station from other track is first (beginning station)
	# 											if station in connections_traversed[j].edges[0][0]:

	# 												print("testestetes")

	# 												# Nieuwe track: over edges  van J, reversed
	# 												reversed_list = []
	# 												partially_reversed_list = list(reversed(connections_traversed[j].edges))
	# 												for item in partially_reversed_list:
	# 													reversed_list.append(tuple(reversed(item)))

	# 												# zoek station in edges van i
	# 												for item in connections_traversed[i].edges:
	# 													if item == station:
	# 														print("item: ", end="")
	# 														print(item)

	# 												# ga dan vanaf daar edges af.
	# 												# reverse deze edges
	# 												# rest van de edges (in reverse.)	

	# 												### dit kan wel.

	# 												print("5")

	# 											# if station in other track is last station
	# 											elif station in connections_traversed[j].edges[len(connections_traversed[j].edges) - 1][1]:

	# 												print("ttesssstt")
	# 												# Nieuwe track: over edges  van J tot je aankomt bij station, niet in reverse.
	# 												# station vinden in edges I
	# 												for item in connections_traversed[i].edges:
	# 													if item == station:
	# 														print("item: ", end="")
	# 														print(item)
	# 												# ga dan vanaf daar edges af.
	# 												# diezelfde edges in reverse.
	# 												# rest van de edges (evt. in reverse.)

	# 												### dit kan ook.

	# 												print("6")

	# 											# if station in other track is in middle
	# 											else:

	# 												# Neem langste track, neem daar een willekeurige helft 
	# 												# van, dan over de twee helften elk heen en weer van de i
	# 												# en dan de rest van de langste track
	# 												print("7")
	# 						except ValueError:
	# 							pass
	# 						continue							
	# 	except:
	# 		pass
	# 	continue


	#######################################################################################		

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