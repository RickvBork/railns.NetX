import test_helpers
import random

'''
Pure, random walk. No heuristics.
Takes a graph object and an iterator.
'''
def random_walk(graph, iterator):

	# get information from graph to perform algorithm
	nodelist = graph.nodes
	minimum_weight = graph.minimal_edge_weight
	critical_connections = graph.critical_edge_list
	total_critical_connections = graph.total_critical_edges
	G = graph.G

	# set lists
	p_list = []
	s_list = []
	best_tracks = []
	best_score = -141

	# do the walk iterator amount of times
	for i in range(iterator):

		# start a list of unique critical tracks the random walk traverses
		critical_connections_traversed = []

		# begin new track dict
		all_connections = {}

		# rand number of tracks 1 up to including 7
		random_tracks = random.randint(1, 7)

		print("Track number: {}".format(random_tracks))

		# keep track of critical connections that are not used yet
		total_time = 0

		for track in range(random_tracks):

			# begin new dict with lists
			all_connections[str(track)] = []

			# rand start station 0 up to nodelist length - 1 to pick a node in nodelist
			starting_station = random.choice(nodelist)

			print("Begin walk: {}".format(starting_station))

			# keeps track of the time of one track of a service
			track_time = 0

			# random time for a given track
			random_time = random.randint(minimum_weight, 120)

			print("Track maximum time: {}".format(random_time))

			counter = 0
			while track_time < random_time:

				#random_neighbor = random.choice(G[starting_station]).keys()
				random_neighbor = random.choice(list(G[starting_station]))

				# append each new edge to track
				all_connections[str(track)].append((starting_station, random_neighbor))

				# keeps track of time of the track
				edge_time = G[starting_station][random_neighbor]['weight']
				track_time += edge_time
				
				# always pick one track
				if edge_time > random_time and counter != 0:
					print("		Exception!\nTime: {} > Edge Time: {}\n{} tracks walked".format(edge_time, random_time, counter))
					break
				counter += 1

				# update traversed critical connections as long as not all have been covered
				if len(critical_connections_traversed) != total_critical_connections:
					critical_connections_traversed = test_helpers.update_critical_connections_travesed((starting_station, random_neighbor), critical_connections, critical_connections_traversed)
				else:
					print("`GOT EM!") # yeah right...

				# updates the starting station
				starting_station = random_neighbor
				print("		Next station: {}".format(random_neighbor))
				print("			Edge time is: {}".format(edge_time))
				print("			Total time is: {}".format(track_time))
				print("-------------------------------------------------")

			# total time of the service
			total_time += track_time

			print("This service will take {}min".format(track_time))
		
		# percentage of critical tracs traversed
		p = test_helpers.get_p(critical_connections_traversed, critical_connections)
		p_list.append(p)

		# append score
		s = test_helpers.get_score(p, random_tracks, total_time)
		s_list.append(s)

		# update best track if its score is better than previous best
		if s > best_score:
			best_tracks.append(all_connections)
			best_score = s

		print("Connections made:\n")
		for i in range(random_tracks):
			print("Track {}:	".format(i + 1), end = '')
			edgeList = all_connections[str(i)]
			for edge in edgeList:
				print("{} -> ".format(edge), end = '')
			print("End")

	return s_list, p_list, best_tracks