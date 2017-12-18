'''
helper for hillclimber, based on random_walk
'''

from classes import service_class as svc, track_class as trc 
import helpers as hlp
import random
from copy import deepcopy

def random_walk(Graph, iterator, max_number_of_tracks, max_time):

	# get information from graph to perform algorithm
	G = Graph.G
	minimum_weight = Graph.minimal_edge_weight
	nodes = Graph.nodes
	
	# build node structure
	node_list = hlp.get_node_list(G, nodes)

	# set lists
	best_score = - 141
	max_service_amount = 5
	best_services = [0] * max_service_amount

	# do the walk iterator amount of times
	for i in range(iterator):

		# build service loop
		service = svc.service(Graph)

		# rand number of tracks 1 up to including 7
		number_of_tracks_in_service = random.randint(1, max_number_of_tracks)
		number_of_tracks_in_service = max_number_of_tracks

		# builds the service of multiple tracks
		for k in range(number_of_tracks_in_service):

			# pick random starting station 
			start = random.choice(node_list)

			# random time for a given track
			random_time = random.randint(minimum_weight, max_time)
			random_time = max_time

			track = generate_random_track(Graph, start, random_time)
			
			# add track to service
			service.add_track(track)
	
		score = service.s_score

		if score > best_score:
			best_services[i % max_service_amount] = service
			best_score = score
			i += 1

	# remove empty values as list is not always filled
	return [service for service in best_services if service != 0]

'''
seperate function for generate_random_track
'''
def generate_random_track(Graph, start, max_track_length):
	
	track = trc.track(Graph)
	
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

	return track 
