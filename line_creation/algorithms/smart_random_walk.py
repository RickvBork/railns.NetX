from classes import service_class as svc
import helpers as hlp
import math
import random

def smart_random_walk(Graph, max_number_of_tracks, max_time, iterator):
	'''
	A random walk algorithm restricted by several heuristics.

	Arguments:
		(0) A networkx graph, which contains the data needed to make tracks and services
		(1) The maximum amount of tracks for each service
		(2) The maximum lenght of each track
		(3) The amount of services to be made

	Returns:
		A list of the 5 best services.
	
	For each of the tracks of each of the services, the random walk algoritm chooses a random
	starting station. Then a random neighboring edge is chosen and added to the track until the track is over the maximum time. The extra edge is removed and the track is added to the service.
	'''

	print("\n======SMART RANDOM WALK======\n")

	# get information from graph to perform algorithm
	G = Graph.G
	minimum_weight = Graph.minimal_edge_weight
	nodes = Graph.nodes
	
	#build node structure
	node_list = hlp.get_node_list(G, nodes)

	critical_connections = Graph.critical_edge_list
	total_critical_connections = Graph.total_critical_edges

	# set lists
	max_service_amount = 5
	score_list = [- math.inf] * max_service_amount
	service_list = [None] * max_service_amount
	min_score = score_list[0]
	min_index = 0

	# initiate loading bar
	hlp.loading_bar(0, iterator, prefix = 'Progress:', suffix = 'Complete', length = 50, update = 100)

	# do the walk iterator amount of times
	for i in range(iterator):

		# build service loop
		service = svc.service(G)

		# builds the service of multiple tracks
		for k in range(max_number_of_tracks):

			# pick random start station 
			# TODO: make sure node is critical
			start = random.choice(node_list)

			track = hlp.generate_smart_random_track(G, start, max_time)
			
			# add new track to service
			service.add_track(track)

		score = service.s_score

		# remember best scores (unordered)
		# get key of minimum value in dict
		if score > min_score:
			score_list, service_list, min_score, min_index = hlp.update_lists(score, min_index, service, score_list, service_list)

		# update loading bar
		hlp.loading_bar(i, iterator, prefix = 'Progress:', suffix = 'Complete', length = 50, update = 100)

	# remove empty values as list is not always filled
	return service_list