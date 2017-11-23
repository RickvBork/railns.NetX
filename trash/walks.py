import random

'''
Pure, random walk. No heuristics.
Takes a graph object and an iterator.
'''
def random_walk(graph_object, iterator):
		
		# get information from graph to perform algorithm
		nodelist = graph_object.nodelist
		minimum_weight = graph_object.minimum_weight
		critical_connections = graph_object.critical_connections

		# set lists
		p_list = []
		s_list = []
		for i in range(iterator):
		
			# start a list of unique critical tracks the random walk traverses
			critical_connections_traversed = []

			# rand number of tracks 1 up to including 7
			random_tracks = random.randint(1,7)

			# keep track of critical connections that are not used yet
			delete_counter = 0
			total_time = 0

			for track in range(random_tracks):

				# rand start station 0 up to nodelist length - 1 to pick a node in nodelist
				starting_station = nodelist[random.randint(0,len(nodelist) - 1)]
				time = 0

				# rand time for a given track
				random_time = random.randint(minimum_weight,120)

				counter = 0
				while time < random_time:

					# chooses a random key from a dictionary (neighbors), is choosing a random neighbor

					#random_neighbor = random.choice(G[starting_station]).keys()
					random_neighbor = random.choice(list(G[starting_station]))

					# keeps track of time of the track
					time += G[starting_station][random_neighbor]['weight']
					total_time += G[starting_station][random_neighbor]['weight']
					
					# always pick one track, catch exception of second track being larger than random time
					if time > random_time and counter != 0:
						break
					counter += 1

					# make list of unique traversed critical connections
					if ((starting_station, random_neighbor) in critical_connections) or ((random_neighbor, starting_station) in critical_connections):
						if not ((starting_station, random_neighbor) in critical_connections_traversed) and not ((random_neighbor, starting_station) in critical_connections_traversed):
							critical_connections_traversed.append((starting_station, random_neighbor))

					# updates the starting station
					starting_station = random_neighbor
			
			# percentage of critical tracs traversed
			p.append(get_p(critical_connections_traversed, critical_connections))
			
			# score function 1
			s.append(get_score(p, random_tracks, total_time))

		return s, p
