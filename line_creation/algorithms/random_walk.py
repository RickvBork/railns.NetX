from classes import service_class as svc
import helpers as hlp
import math
import random

def random_walk(Graph, max_number_of_tracks, max_time, iterator):
	'''
	Pure, random walk. No heuristics. Takes a graph object and an iterator as arguments. Returns an unordered list of 5 best service classes.
	'''

	print("\n======RANDOM WALK======\n")

	G = Graph.G
	minimum_weight = Graph.minimal_edge_weight
	nodes = Graph.nodes

	# build node structure
	node_list = hlp.get_node_list(G, nodes)

	# initialise list for best services
	max_service_amount = 5
	best_services = [0] * max_service_amount
	best_score = - math.inf
	i = 0

	for j in range(iterator):

		# build service loop
		service = svc.service(G)

		# rand number of tracks 1 up to including 7
		number_of_tracks_in_service = random.randint(1, max_number_of_tracks)
		number_of_tracks_in_service = max_number_of_tracks

		for k in range(number_of_tracks_in_service):

			# pick random starting station 
			start = random.choice(node_list)

			# random time for a given track
			random_time = random.randint(minimum_weight, max_time)
			random_time = max_time

			track = hlp.generate_random_track(Graph, start, random_time)
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