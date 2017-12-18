from classes import service_class as svc
import helpers as hlp
import math
import random

def random_walk(Graph, max_number_of_tracks, max_time, iterator):
	'''
	A random walk algorithm, defined as such that no heuristics are involved.

	Arguments:
		(0) A networkx graph, which contains the data needed to make tracks and services
		(1) The maximum amount of tracks for each service
		(2) The maximum lenght of each track
		(3) The amount of services to be made

	Returns:
		A list, with an ever changing length, of a few of the best services
	
	For each of the tracks of each of the services, the random walk algoritm chooses a random
	starting station. Then a random neighboring edge is chosen and added to the track until the track is over the maximum time. The extra edge is removed and the track is added to the service.
	'''

	print("\n======RANDOM WALK======\n")

	G = Graph.G
	minimum_weight = Graph.minimal_edge_weight
	nodes = Graph.nodes

	# build node structure
	node_list = hlp.get_node_list(G, nodes)

	# set lists
	max_service_amount = 5
	score_list = [- math.inf] * max_service_amount
	service_list = [None] * max_service_amount
	min_score = score_list[0]
	min_index = 0

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

			track = hlp.generate_random_track(G, start, random_time)
			# add new track to service
			service.add_track(track)

		score = service.s_score

		# get key of minimum value in dict
		if score > min_score:
			score_list, service_list, min_score, min_index = hlp.update_lists(score, min_index, service, score_list, service_list)

		# update loading bar
		hlp.loading_bar(j, iterator, prefix = 'Progress:', suffix = 'Complete', length = 50, update = 100)

	# remove empty values as list is not always filled
	return service_list