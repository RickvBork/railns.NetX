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
import line_edges_class as E
from copy import deepcopy

def hillclimber(service):
	track0 = service.tracks[0]	
	# replace track by a new track
	track_time = 120
	Graph = service.graph
	nodelist = Graph.nodes
	starting_station = random.choice(nodelist) 
	all_connections = all_connections = {"tracks": {}, "score": None} 
	track_number = 1 
	track_time, track_new = hh.generate_track(120, Graph, starting_station, all_connections, track_number) 
	service.add_track(track_new)
	service.remove_track(track0)
