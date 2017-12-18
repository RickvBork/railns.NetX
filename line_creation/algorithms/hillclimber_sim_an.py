'''
Hill cilmber simulated annealing
takes service oject consisting of several tracks. Tries to optimize service 
by improving tracks one by one
'''

# TODO
from algorithms import hillclimber_helper as hh
import helpers as hlp
import random
import csv
import math
from helpers import clear

def run_hillclimber_sim_an(service, max_number_of_tracks, max_track_time, \
	number_of_iterations):
	'''
	Runs hillclimber
	'''
	hillclimber_scores = []
	last_score = 0
	
	for j in range(number_of_iterations):
		number_of_tracks = len(service.tracks)
		for i in range(number_of_tracks):
			for k in range(number_of_iterations):
				service = hillclimber_sim_an(service,i,max_number_of_tracks, \
					max_track_time, j + k)
							
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


def hillclimber_sim_an(service, track_number, max_number_of_tracks, \
	max_track_time, temperature):
	'''
	Replaces a single track of a service by by a new random track. 
	If service has higher score with new random track, service with new random 
	track is returned. If not, old service is replaced by new service by a 
	probability of 1 / e^temperature.
	'''
	old_service_score_s = service.s_score
	track0 = service.tracks[track_number]	
	
	Graph = service.G
	nodes = Graph.nodes
	node_list = hlp.get_node_list(Graph, nodes)
	
	# generate new track
	start = random.choice(node_list) 
	track_new = hh.generate_random_track(Graph, start, max_track_time)
	

	old_track_removed = False
	service.add_track(track_new)
	if len(service.tracks) >= max_number_of_tracks:
		service.remove_track(track0)
		old_track_removed = True

	# check if score is higher
	new_service_score_s = service.s_score

	# accept new track if score is higher with probability one
	# if score of service with new track is lower, accept new track in service 
	# with probability 1/temperature

	# undo adding new track is score is lower
	if old_service_score_s > new_service_score_s:
		random_int = random.choice(range(1000))
		probability = math.e ** ( - 1 * temperature) 
		if (float(random_int/1000) >=  probability):
			service.add_track(track0)
			service.remove_track(track_new)

	return service
