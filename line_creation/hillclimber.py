'''
Hill cilmber 
takes service oject consisting of several tracks. Tries to optimize service by improving tracks one by one
'''

import hillclimber_helper as hh
import helpers as hlp
import random
import line_analysis as ana
import networkx as nx
import collections # for Hierholzer's
import line_node_class as N
from copy import deepcopy
import track_class as tc

def hillclimber_random(service, track_number):
	old_service_score_s = service.s_score
	track0 = service.tracks[track_number]	
	max_track_length = 120
	Graph = service.graph
	nodes = Graph.nodes
	node_list = hlp.get_node_list(Graph.G, nodes)
	
	# generate new track
	start = random.choice(node_list) 
	track_new = hh.generate_random_track(Graph, start, max_track_length)
	service.add_track(track_new)
	service.remove_track(track0)

	# check if score is higher
	new_service_score_s = service.s_score
	# undo adding new track is score is lower
	if old_service_score_s > new_service_score_s:
		service.add_track(track0)
		service.remove_track(track_new)

def hillclimber_random(service, track_number):
	old_service_score_s = service.s_score
	track0 = service.tracks[track_number]	
	max_track_length = 120
	Graph = service.graph
	nodes = Graph.nodes
	node_list = hlp.get_node_list(Graph.G, nodes)
	
	# generate new track
	start = random.choice(node_list) 
	track_new = hh.generate_smart_random_track(Graph, start, max_track_length)
	service.add_track(track_new)
	service.remove_track(track0)

	# check if score is higher
	new_service_score_s = service.s_score
	# undo adding new track is score is lower
	if old_service_score_s > new_service_score_s:
		service.add_track(track0)
		service.remove_track(track_new)


def hillclimber_sim_an(service, track_number):
	old_service_score_s = service.s_score
	track0 = service.tracks[track_number]	
	max_track_length = 120
	Graph = service.graph
	nodes = Graph.nodes
	node_list = hlp.get_node_list(Graph.G, nodes)
	
	# generate new track
	start = random.choice(node_list) 
	track_new = hh.generate_random_track(Graph, start, max_track_length)
	service.add_track(track_new)
	service.remove_track(track0)

	# check if score is higher
	new_service_score_s = service.s_score
	# undo adding new track is score is lower
	if old_service_score_s > new_service_score_s:
		service.add_track(track0)
		service.remove_track(track_new)
