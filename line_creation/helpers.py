'''
Helpers file.

Here all functions not directly important to
algorithm functioning and classes are defined
'''

from classes import node_class as ndc, track_class as trc 
import collections as col
import os, errno
import random
import collections
import helpers as hlp

def clear():
	'''
	Clears the console screen.
	'''
	os.system('cls' if os.name == 'nt' else 'clear')


def get_p(critical_connections_traversed, critical_connections):
	'''
	A function for calculating the percentage of critical tracks traversed of a given service.

	Arguments:
		(0) A list of the critical connections traversed
		(1) A list of all critical connections

	Returns:
		The fraction of critical tracks traversed (float)
	'''
	return len(critical_connections_traversed) / len(critical_connections)


def get_score(p, track_amount, total_track_time):
	'''
	A score function for calculating the score of a given service. Taken from: http://heuristieken.nl/wiki/index.php?title=RailNL

	Arguments:
		(0) Percentage of critical tracks traversed.
		(1) The amount of tracks in a service
		(2) Total track time

	Returns:
		The score of a given service (float)
	'''
	return p * 10000 - (track_amount * 20 + total_track_time / 100000)

def update_critical_connections_travesed(tuple, critical_edges, critical_edges_traversed):
	'''
	Checks wether a certain connection is critical in any direction.
	And wether the critical connection has already been travelled in any direction.
	'''
	edge = tuple
	edge_reversed = (tuple[1], tuple[0])

	if (edge in critical_edges) or (edge_reversed in critical_edges):
		if not (edge in critical_edges_traversed) and not (edge_reversed in critical_edges_traversed):
			critical_edges_traversed.append(edge)
	return critical_edges_traversed

def ordered_counter(score_list):

	# count the number of times an integer is in list
	count_dict = col.Counter(score_list)

	# sort list by integer
	ordered_dict = col.OrderedDict(sorted(count_dict.items()))

	return ordered_dict

def get_prefered_neighbors(G, starting_station, track):
	'''
	Takes graph, and a track (in progress) to a starting station. 
	Returns all neighbors from starting stations where tracks hasn't been.
	'''
	# get list of neighbors of starting station
	neighbors = [station for station in list(G[starting_station])]

	prefered_neighbors = list(neighbors)

	for neighbor in neighbors:
		if ((starting_station, neighbor) in track.edges or (neighbor, starting_station) in track.edges):
			prefered_neighbors.remove(neighbor)

	return prefered_neighbors


def test(edge, critical_edges, critical_edges_traversed):

	edge_reversed = (edge[1], edge[0])
	print(edge, edge_reversed)

	if not (edge in critical_edges_traversed) and not (edge_reversed in critical_edges_traversed):
		if (edge in critical_edges) or (edge_reversed in critical_edges):
			critical_edges_traversed.append(edge)
	return critical_edges_traversed

def get_node_list(G, nodes):
	'''
	Connects node objects to their neighbors for easy linking and delinking of nodes within an algorithm.

	Arguments:
		(0) A networkx Graph object.
		(1) A list of all nodes of the Graph object as strings.

	Returns:
		A list of interlinked node objects (list)
	'''
	node_dict = {}
	for node in nodes:
		node_dict[node] = ndc.Node(node)

	node_list = []
	for node in nodes:
		for neighbor in G[node]:
			node_dict[node].add_neighbor(node_dict[neighbor])
		node_list.append(node_dict[node])

	return node_list


def file_remove(path_file_name):
	'''
	Removes files of a given name.

	Arguments:
		(0) A string which represents the path to the file that is to be removed.
	'''
	try:
		os.remove(path_file_name)
	except OSError as e:
		if e.errno != errno.ENOENT:
			raise

def loading_bar(iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '.', update = 100, switch = 100):
	'''
	Loading bar. Two modes for faster computation of large iteration numbers. Switch sets the total iteration number where behaviour switches between modes.

	1: User chooses for update every 1% or .1% (update = 100, 1000)

	2: Always update every iteration. Show .1% increases

	Arguments:
		(0) The current iteration number (integer)
		(1) The total iteration number
		(2) Prefix of the loading bar
		(3) Suffix of the loading bar
		(4) Amount of decimals to show for the loading percentage amount
		(5) The length of the loading bar in amount of chars
		(6) The char to fill the loading bar with
		(7) The update amount, 100 is per percent, 1000 is per tenth of percent
		(8) The amount at which the behaviour of the loading bar automatically switches
	'''

	# behaviour mode 1: every update %
	if total >= switch and (iteration % (total / update)) == 0:
		iteration += total / update
		percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration / float(total)))
		filledLength = int(length * iteration // total)
		bar = fill * filledLength + '-' * (length - filledLength)
		print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')

	# behaviour mode 2: standard every .1%
	elif total < switch:
		iteration += 1
		percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration / float(total)))
		filledLength = int(length * iteration // total)
		bar = fill * filledLength + '-' * (length - filledLength)
		print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')

	if iteration == total: 
		print()

def get_neighbor(Node, Previous):
	'''
	Gets any neighbor a node except the previous neighbor if the node has more than one neighbor. If the node has one neighbor this behaviour is overwritten.

	Arguments:
		(0) A node to be checked for neighbors
		(1) A node object which is the previous of the node to be checked for neighbors

	Returns:
		A neighbor (node object).
	'''
	for neighbor in Node.neighbors:
		if neighbor != Previous: 
			return neighbor
		elif len(Node.neighbors) == 1:
			return neighbor


def is_junction(Node):
	'''
	Checks wether a node is a junction. A junction is defined as any node with more than two neighbors.

	Arguments:
		(0) A node object to be checked if it is a junction

	Returns:
		True if the node is a junction, False otherwise (Boolean)
	'''

	if len(Node.neighbors) > 2:
		return True
	else:
		return False


def update_path(Track, path, edge):
	'''
	Updates a dictionary of hashed tracks ending in a junction node keying edges that have been traversed any track previously made by the DFS algorithm.

	Arguments:
		(0) A track object
		(1) A dictionary to be updated
		(2) An edge to be added to the list keyed by the hashed track if it is not already in the list

	Returns:
		The updated dictionary.
	'''

	key = hash(Track)
	try:
		walked_edges = path[key]
		if edge not in walked_edges:
			path[key].append(edge)
	except KeyError:
		path[key] = [edge]
	return path

def junction_edges(Track, path):
	'''
	For a given track ending in a junction node, returns the edges that have been traversed by other tracks.
	
	Arguments:
		(0) A track object
		(1) A dictionary where hashed tracks key traversed edges

	Returns:
		A list of edges traversed by any other track.
	'''

	key = hash(Track)
	junction_edges = path[key]
	return junction_edges


def get_junction_neighbor(Start, Previous, junction_edges):
	'''
	Checks neighbors of a junction Node against the previously walked Node, and all directed junction edges that can be created with the neighbors.
	'''
	
	for neighbor in Start.neighbors:
		if neighbor != Previous:
			edge = (Start.name, neighbor.name)
			if not edge in junction_edges:
				return neighbor
	return None

def get_previous(Start, key):
	try:
		Previous = Start.test[key]
	except KeyError:
		Previous = None
	return Previous

def link_nodes(Start, Neighbor, key):
	'''
	Links two nodes. It sets the previous of the last node to the first node.
	'''

	Neighbor.test[key] = Start
	Start = Neighbor
	return Start

def delink_nodes(Start, key):
	'''
	Delinks two nodes. It sets the previous of the last node to 'None' and returns the node before the last node as the new start.
	'''
	
	try:
		Previous = Start.test[key]
		del Start.test[key]
		Start = Previous
	except KeyError:
		pass
	return Start

def generate_random_track(G, start, max_track_length):
	'''
	seperate function for generate_random_track
	'''
	
	track = trc.track(G)
	
	# always build track one edge longer than allowed
	while track.time < max_track_length:

		# choose random neighbor node
		neighbor = random.choice(start.neighbors)

		# add built edge
		track.add_edge((start.name, neighbor.name))

		# update start
		start = neighbor
		
	# make sure track is minimum of one edge, remove extra edge
	if len(track.edges) != 1:
		track.remove_edge()

	return track 

def generate_smart_random_track(G, start, max_track_length):

	track = trc.track(G)	
	start = start.name

	while track.time < max_track_length:
				
		# get list of critical neighbours of starting_station
		critical_neighbors = [station for station in list(G[start]) if G.node[station]['color'] == 'r']
	
		prefered_neighbors = hlp.get_prefered_neighbors(G, start, track)

		if prefered_neighbors == []:
			random_neighbor = random.choice(list(G[start]))
		else: 
			random_neighbor = random.choice(prefered_neighbors)

		track.add_edge((start, random_neighbor))

		# update start
		start = random_neighbor

	# make sure track is minimum of one edge
	if len(track.edges) != 1:
		track.remove_edge()

	return track

def get_one_edge_node(all_edge_list, graph, service):
	'''
	For Hierholzer's. Returns a node with only one edge with a critical neighbor.
	First makes a list of all stations that currently have one, untraversed, edge.
	It checks which of these have a critical neighbor, and if possible, a random
	starting station is chosen from these. If not, a station with one edge. If
	that is impossible aswell, a starting station with no constraints is chosen.
	'''

	# make list with every station as much as they have untraversed edges
	stations_in_edges_amount_list = [elem for t in all_edge_list for elem in t]

	# initalize list for stations with only one untraversed edge
	one_edge_list = []

	# determine which stations have only one edge, adding these to one_edge_list
	counter = collections.Counter(stations_in_edges_amount_list)
	for station, count in counter.items():
		if count == 1:
			one_edge_list.append(station)

	# make list for nodes with one edge, and the node at other end of edge is critical
	super_special = []

	# fill super special list
	for station in one_edge_list:
		if station in dict(service.all_critical_edges):
			super_special.append(station)

	# get random starting station that has only one edge with other node critical, if possible
	if super_special != []:
		current_node = random.choice(super_special)
	# else get random starting node with only one edge
	elif one_edge_list != []:
		current_node = random.choice(one_edge_list)
	# else get random starting node without constraints
	else:
		current_node = random.choice(list(graph.nodes))

	return current_node

def track_combination(service, max_track_length, G):
	'''
	For Hierholzer's. Combines two tracks into one track if: the total track length of the 
	two tracks doesn't exceed the maximum track length, and if the two tracks have either
	the same starting station, which means that the edges of one of the two tracks have to be
	reversed, or if the two tracks have the same ending and starting station.
	'''

	# list to store new tracks (to add to track object after iteration)
	tmp_new_track_list = []

	# iterate over all tracks
	for i in range(len(service.tracks)):
		# for each track, iterate over all other tracks
		for j in range(len(service.tracks)):
			# ensure that track is not compared to itself
			if i != j:
				# if track time combined is less than the maximum time
				if (service.tracks[i].time + service.tracks[j].time) < max_track_length:
					# to prevent index out of range errors
					if service.tracks[i].edges != [] and service.tracks[j].edges != []: 
						# if starting station for both stations is the same
						if service.tracks[i].edges[0][0] == service.tracks[j].edges[0][0]:

							# initialize reversed_list to completely reverse one of the tracks
							reversed_list = []
							# reverse edges
							partially_reversed_list = list(reversed(service.tracks[j].edges))
							# reverse content of edges
							for item in partially_reversed_list:
								reversed_list.append(tuple(reversed(item)))

							# make new list with edges of new track
							combined_list = reversed_list + service.tracks[i].edges
							
							# initizialize check_list to check if new track is already made in earlier iteration
							check_list = []

							# if new route is not in reversed already in tmp_new_track_list:
							for item in list(reversed(combined_list)):
								check_list.append(tuple(reversed(item))) 

							booleanTrack = False
							# iterate over lists of routes in tmp list
							for item in tmp_new_track_list:
								# if check_list is in tmp, than there is no need to add new combined list to 
								if item == check_list:
									# set boolean to true, to prevent combined list from being add
									booleanTrack = True

							if booleanTrack == False:

								# add new route to tmp list
								tmp_new_track_list.append(combined_list)

								# indicate that track can later be removed from service
								service.tracks[i].necessary = False
								service.tracks[j].necessary = False
								
						# if starting station and ending station is the same
						elif service.tracks[i].edges[0][0] == service.tracks[j].edges[-1][1]:

							# make new list with edges for new track
							combined_list = service.tracks[j].edges + service.tracks[i].edges
								
							# add new route to tmp list
							tmp_new_track_list.append(combined_list)

							# indicate that track can later be removed from service
							service.tracks[i].necessary = False					
							service.tracks[j].necessary = False

	# ensure that next part is skipped if no new tracks were made
	if tmp_new_track_list != []:

		# for all - old - tracks in the service
		for track in service.tracks:

			# if track is redundant
			if track.necessary != True:

				# remove track from service
				service.remove_track(track)

		# for all new track routes in tmp list
		for item in tmp_new_track_list:

			# make new track object
			track = trc.track(G)

			# add new track route to new track object
			track.add_edge_list(item)

			# add new track to service to replace redundant tracks
			service.add_track(track)

	return service

def update_lists(score, min_index, service, score_list, service_list):

	score_list[min_index] = score
	service_list[min_index] = service
	min_score = min(score_list)
	min_index = score_list.index(min_score)

	return score_list, service_list, min_score, min_index
