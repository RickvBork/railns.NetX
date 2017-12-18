from classes import service_class as svc, track_class as trc
import helpers as hlp
import random
from copy import deepcopy
import analysis as ana

def hierholzer(graph, max_track_amount, max_track_length, iterator):
	'''
	Hierholzer's algorithm. A variation on Carl Hierholzer's efficient algorithm 
	to find Eularian Cycles, here used to make services.

	Arguments:
		(0) A networkx graph, which contains the data needed to make tracks 
		and services
		(1) The maximum amount of tracks for each service
		(2) The maximum lenght of each track
		(3) The amount of services to be made

	Returns:
		A list with a few of the best services
	
	For each of the tracks of each of the services, Hierholzer's algoritm 
	chooses a random starting station, which has only one edge and a neighbor 
	which is a critical station, if possible. Then every other edge is chosen 
	randomly, with the constraint that it hasn't been traversed yet, by this 
	track or by any other track in the service. If the track reaches a station 
	with no untraversed edges, or if the track reaches the maximum time allowed, 
	it is completed and added to the service. 
		Until there are no more untraversed edges, or until the maximum amount 
	of tracks is reached, new tracks will be made in the same way. After the 
	completion of the making of new tracks, tracks will be combined if possible. 
	Tracks will be combined if they have a combined length that doesn't exceed 
	the maximum length,	and if they have either the same starting station, 
	or the same starting and ending station.
	'''
	print("======HIERHOLZER======")
	
	# inititialize variables to save and return best service(s)
	best_score = 0
	max_service_amount = 5
	best_services = [0] * max_service_amount

	# initiate loading bar
	hlp.loading_bar(0, iterator, prefix = 'Progress:', suffix = 'Complete', length = 50, update = 100)

	# make iterator amount of services
	for i in range(iterator):

		# for access to the graph
		G = graph.G

		# initialize service
		service = svc.service(G)

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

			# get random node that has one edge and a critical neighbor
			current_node = hlp.get_one_edge_node(all_edge_list, graph, service)

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

					# add complete track to service
					service.add_track(track)

					# break out of while loop to begin new making of track
					break

				# choose random neighbor of station
				random_neighbor_node = random.choice(list(G[current_node]))

				# ensure that edge hasn't been traversed yet
				while (current_node, random_neighbor_node) not in all_edge_list \
				and (random_neighbor_node, current_node) not in all_edge_list:
					random_neighbor_node = random.choice(list(G[current_node]))

				# get edge time
				edge_time = G[current_node][random_neighbor_node]['weight']
				
				# keeping track of total time of all tracks
				total_time += edge_time

				# if track is longer than maximum track length
				if track.time > max_track_length:

					# remove last edge to make length less than 120 minutes
					track.remove_edge()

					# add complete track to service
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

					# for possibly adding tracks together later on via the optimization
					track.add_station(current_node, random_neighbor_node)

					# make neighbor node current node, so that this node can go through while loop to create track
					current_node = random_neighbor_node

		# optimization: combine two tracks to one track, in some situations; see helpers.py
		new_service = hlp.track_combination(service, max_track_length, G)

		# iterate over all tracks
		for track in new_service.tracks:
			# check which tracks actually traverse critical edges
			check_list = [edge for edge in track.edges if edge in graph.critical_edge_list or tuple(reversed(edge)) in graph.critical_edge_list]
			# if track traverses no critical edges
			if not check_list:
				# remove track
				new_service.remove_track(track)

		print("score: ", end="")
		print(new_service.s_score)

		# remember best scores (unordered)
		if new_service.s_score >= best_score:
			best_services[i % max_service_amount] = deepcopy(service)
			best_score = new_service.s_score
			i += 1

		# update loading bar
		hlp.loading_bar(i, iterator, prefix = 'Progress:', suffix = 'Complete', length = 50, update = 100)

	# remove empty values as list is not always filled
	return [service for service in best_services if service != 0]
