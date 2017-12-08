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

def hillclimber(service, track_number):
	old_service_score_s = service.s_score
	track0 = service.tracks[track_number]	
	# replace track by a new track
	track_time = 120
	Graph = service.graph
	nodelist = Graph.nodes
	starting_station = random.choice(nodelist) 
	all_connections = all_connections = {"tracks": {}, "score": None} 
	track_number = 1 
	track_time, track_new = hh.generate_track(track_time, Graph, starting_station, all_connections, track_number) 
	track_new_c = tc.track(track_new['tracks'][str(track_number)], service.graph)
	service.add_track(track_new_c)
	service.remove_track(track0)
	# check if score is higher
	new_service_score_s = service.s_score
	# undo adding new track is score is lower
	if old_service_score_s > new_service_score_s:
		service.add_track(track0)
		service.remove_track(track_new_c)

