from classes import service_class as svc, track_class as trc
import helpers as hlp
import itertools
import random
import networkx as nx
from copy import deepcopy
import collections
import analysis as ana

def hierholzer(graph, max_track_length, max_track_amount, iterator):
	'''
	Hierholzer's algorithm. 
	'''

	print("======HIERHOLZER======")
	
	test_counter = 0

	mean_list = []
	
	service_list = []

	# inititialize variables to save and return best service(s)
	best_score = 0
	max_service_amount = iterator
	best_services = [0] * max_service_amount

	# initiate loading bar
	#hlp.loading_bar(0, iterator, prefix = 'Progress:', suffix = 'Complete', length = 50, update = 100)

	# do the walk iterator amount of times
	for i in range(iterator):

		# for access to the graph
		G = graph.G

		# initialize service
		service = svc.service(graph.G)

		# adding all edges as tuples to all_edges_list
		all_edge_list = [edge for edge in graph.edges]

		# to keep track of time of all tracks combined
		total_time = 0

		# for each track
		while True:

			# if all edges are traversed
			if all_edge_list == []:

				# break to end making of new tracks, and continue to the combining of tracks
				break

			# if the number of tracks made is the maximum amount of tracks allowed
			if (len(service.tracks)) == max_track_amount:

				# break to end making of new tracks, and continue to the combining of tracks
				break

			# make new track object (one for each track)
			track = trc.track(G)

			current_node = hlp.get_one_edge_node(all_edge_list, graph, service)
			#current_node = random.choice(critical_station_list)

			# loop for each edge in each track
			while True:

				# checking if current station has unused edges
				remaining_edge_check = [item for item in all_edge_list if current_node in item]
				
				# if current_node has no unused edges
				if remaining_edge_check == []:

					# if last track made track longer than maximum track length
					if track.time > max_track_length:

						# remove last edge
						track.remove_edge()

					service.add_track(track)

					# break out of while loop to begin new track
					break

				# choose random neighbor of station
				random_neighbor_node = random.choice(list(G[current_node]))

				# ensure that edge hasn't been traversed yet
				while (current_node, random_neighbor_node) not in all_edge_list and (random_neighbor_node, current_node) not in all_edge_list:
					random_neighbor_node = random.choice(list(G[current_node]))

				# get edge time
				edge_time = G[current_node][random_neighbor_node]['weight']
				
				# keeping track of total time of all tracks
				total_time += edge_time

				# if track is longer than maximum track length
				if track.time > max_track_length:

					# remove last edge to make length less than 120 minutes
					track.remove_edge()

					service.add_track(track)

					# initialize new track object
					track = trc.track(G)

				# if track with new edge is not longer than maximum track length
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

		# determine amount of tracks service has
		#track_counter = len(new_service.tracks)

		# for i in range(track_counter):
		# 	if service.tracks[i].


		# optimization: combine two tracks to one track, in some situations; see helpers.py
		new_service = hlp.track_combination(service, max_track_length, G)
		#new_service = service

		# determine amount of tracks service has
		track_counter = len(new_service.tracks)


		# for i in range(track_counter):
		# 	print("track: ", end="")
		# 	print(service.tracks[i].edges)
		# 	print()

		# print("track_counter: ", end="")
		# print(track_counter)

		#print("test")

		# if round(new_service.s_score) < 9000: # and round(new_service.s_score) <= 9700:
		# 	test_counter += 1
		# 	print("test_counter: ", end="")
		# 	print(test_counter)
		# 	print("service.self score: ", end="")
		# 	print(new_service.s_score)

		# print("service.self score: ", end="")
		# print(new_service.s_score)



		######################
		# track_counter2 = 0

		# if round(new_service.s_score) == 9380:
		# 	for i in range(track_counter):
		# 		print("track: ", end="")
		# 		print(service.tracks[i].edges)
		# 		for j in range(len(service.tracks[i].edges)):
		# 			track_counter2 += 1
		# 			print(track_counter2)

		# 		print()

		# if round(new_service.s_score) == 9900:
		# 	for i in range(track_counter):
		# 		print("track: ", end="")
		# 		print(service.tracks[i].edges)
		# 		for j in range(len(service.tracks[i].edges)):
		# 			track_counter2 += 1
		# 			print(track_counter2)
		# 		print()
		############################	

		#print()

		mean_list.append(deepcopy(service.s_score))

		service_list.append(deepcopy(service))

		# remember best scores (unordered)
		if new_service.s_score > best_score:
			best_services[i % max_service_amount] = deepcopy(service)
			best_score = new_service.s_score
			i += 1

		# update loading bar
		#hlp.loading_bar(i, iterator, prefix = 'Progress:', suffix = 'Complete', length = 50, update = 100)

	# remove empty values as list is not always filled

	ana.draw_graph(graph,service)

	# print("mean_list")
	# print(mean_list)

	# print("mean:")
	# print(np.mean(mean_list))


	return [service for service in best_services if service != 0]
	#return service_list