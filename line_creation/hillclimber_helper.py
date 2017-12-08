'''
helper for hillclimber, based on random_walk
'''

import helpers as hlp
import random
import line_analysis as ana
import networkx as nx
import collections # for Hierholzer's
import line_node_class as N
import line_edges_class as E
from copy import deepcopy

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

			track_time, all_conections = generate_track(random_time, Graph, starting_station, all_connections, track)
			
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
seperate function for generate_track
'''

def generate_track(total_track_time, Graph, starting_station, all_connections, track):
	
	# track is track number
	G = Graph.G
	counter = 0
	all_connections["tracks"][str(track)] = []
	

	track_time = 0
	while track_time < total_track_time:

		#random_neighbor = random.choice(G[starting_station]).keys()
		random_neighbor = random.choice(list(G[starting_station]))

		# keeps track of time of the track
		edge_time = G[starting_station][random_neighbor]['weight']
		track_time += edge_time

		# append each new edge to track
		all_connections["tracks"][str(track)].append((starting_station, random_neighbor))
	
		# always pick one track
		if ((edge_time > total_track_time) and counter != 0) or (edge_time > total_track_time - track_time):
			# print("		Exception!")
			break
		counter += 1

		
		# updates the starting station
		starting_station = random_neighbor
		# print("		Next station: {}".format(random_neighbor))
		# print("			Edge time is: {}".format(edge_time))
		# print("			Total time is: {}".format(track_time))
		# print("-------------------------------------------------")

	return total_track_time, all_connections


