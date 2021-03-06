'''
Hill cilmber 
takes service oject consisting of several tracks. Tries to optimize service by improving tracks one by one
'''

from algorithms import hillclimber_helper as hh
import helpers as hlp
import random
import analysis as ana
import networkx as nx
from classes import track_class as tc
import math
import csv
from helpers import clear

def run_hillclimber(service, max_number_of_tracks, max_track_time, \
	number_of_iterations):
	'''
	Runs hillclimber. Hillclimber is runned number_of_iteration times on
	each single track of the service.
	Then this proces is repeated a number_of_iteration times.
	
	Arguments:
		(0) A service object as defined in service_class
		(1) The maximum nnumber of tracks the service that is returned
		may contain.
		(2) The maximum length of each track
		(3) The number of iterations the hillclimber is runned for each
		track.
	Returns:
		The improved service class.
	'''
	hillclimber_scores = []
	last_score = 0
	
	for j in range(number_of_iterations):
		number_of_tracks = len(service.tracks)
		for i in range(number_of_tracks):
			for k in range(number_of_iterations):
				service = hillclimber_random(service,i,max_number_of_tracks, \
					max_track_time)
							
				if (service.s_score != last_score):
					last_score = service.s_score
					clear()
					print(last_score)

				hillclimber_scores.append(service.s_score) 

	# write score to csv
	with open('../data/hillclimber_sim_an.csv', 'w', newline='') as csvfile:
		wr = csv.writer(csvfile, delimiter=' ', quotechar='|', \
			quoting=csv.QUOTE_MINIMAL)
		for score in hillclimber_scores:
			wr.writerow([score])

	return service
	

def hillclimber_random(service, track_number, max_number_of_tracks, \
	max_track_time):
	'''
	Replaces a single track of a service by by a new random track. 
	If service has higher score with new random track, service with new random 
	track is returned. If not, old service remains unchanged.
	'''
	old_service_score_s = service.s_score
	track0 = service.tracks[track_number]	
	
	Graph = service.G
	nodes = Graph.nodes
	node_list = hlp.get_node_list(Graph, nodes)
	
	# generate new track
	start = random.choice(node_list) 
	track_new = hh.generate_random_track(Graph, start, max_track_time)
	# add new track to service, remove old one if max_number_of_tracks is 
	# reached
	old_track_removed = False	
	service.add_track(track_new)
	if len(service.tracks) >= max_number_of_tracks:
		service.remove_track(track0)
		old_track_removed = True

	# check if score is higher
	new_service_score_s = service.s_score
	# undo adding new track is score is lower
	if old_service_score_s > new_service_score_s:
		service.remove_track(track_new)
		if old_track_removed:		
			service.add_track(track0)

	return service

def hillclimber_smart(service, track_number, max_number_of_tracks, \
	max_track_time):
	'''
	Replaces a single track of a service by by a new smart track. 
	If service has higher score with new random track, service with new random 
	track is returned. If not, old service remains unchanged.
	'''
	old_service_score_s = service.s_score
	track0 = service.tracks[track_number]	
	
	Graph = service.G
	nodes = Graph.nodes
	node_list = hlp.get_node_list(Graph, nodes)
	
	# generate new track
	start = random.choice(node_list) 
	track_new = hlp.generate_smart_random_track(Graph, start, max_track_time)

	# add new track to service, remove old one if max_number_of_tracks is 
	# reached	
	old_track_removed = False
	service.add_track(track_new)
	if len(service.tracks) >= max_number_of_tracks:
		service.remove_track(track0)
		old_track_removed = True

	# check if score is higher
	new_service_score_s = service.s_score
	# undo adding new track is score is lower
	if old_service_score_s > new_service_score_s:
		service.add_track(track0)
		if old_track_removed:		
			service.add_track(track0)

	return service
