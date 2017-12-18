from classes import service_class as svc
import helpers as hlp
import math
import random

'''
Smart 'random' walk
'''
def smart_random_walk(Graph, max_number_of_tracks, max_time, iterator):

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
	best_score = - math.inf
	max_service_amount = 5
	best_services = [0] * max_service_amount
	
	p_list = []
	s_list = []
	best_tracks = []
	
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
		if score > best_score:
			best_services[i % max_service_amount] = service
			best_score = score
			i += 1

		# update loading bar
		hlp.loading_bar(i, iterator, prefix = 'Progress:', suffix = 'Complete', length = 50, update = 100)

	# remove empty values as list is not always filled
	return [service for service in best_services if service != 0]