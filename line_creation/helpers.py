from classes import node_class as ndc, track_class as trc 
import collections as col
import os, errno
import random
import collections # for Hierholzer's
import helpers as hlp


'''
Helpers file.

Here all functions not directly important to
algorithm functioning and classes are defined
'''

'''
Gets the percentage of critical connections traversed.
'''
def get_p(critical_connections_traversed, critical_connections):
	return len(critical_connections_traversed) / len(critical_connections)

'''
Calculates the score and rounds to nearest 10.
m term small, hence the rounding. Plus makes searching for
score occurrence easier.
'''

# ROUND IN VISUALISATION, OTHERWHILE HILLCLIMBER WON'T RECOGNISE SMALL SCORE INCREASES!
def get_score(p, track_amount, total_track_time):
	return p * 10000 - (track_amount * 20 + total_track_time / 100000)

'''
Checks wether a certain connection is critical in any direction.
And wether the critical connection has already been travelled in any direction.
'''
def update_critical_connections_travesed(tuple, critical_edges, critical_edges_traversed):
	edge = tuple
	edge_reversed = (tuple[1], tuple[0])

	if (edge in critical_edges) or (edge_reversed in critical_edges):
		if not (edge in critical_edges_traversed) and not (edge_reversed in critical_edges_traversed):
			critical_edges_traversed.append(edge)
	return critical_edges_traversed

def print_score_information(score_list):

	# get range of score list, ints otherwhise range(min, max) does not take floats
	minimum = int(min(score_list))
	maximum = int(max(score_list))

	# make count dict
	count_dict = col.Counter(score_list)

	print('\nscore, amount\n++++++++++++++')

	# loop through all possible scores
	for i in range(minimum, maximum + 1, 1):

		score_count = count_dict[i]

		# only print relevant scores
		if score_count != 0:
			print('{:<10}'.format(i), end='')
			print(count_dict[i])

	print('++++++++++++++\n')
	print('minimum: {}'.format(minimum))
	print('maximum: {}\n'.format(maximum))

	print(count_dict)

def ordered_counter(score_list):

	# count the number of times an integer is in list
	count_dict = col.Counter(score_list)

	# sort list by integer
	ordered_dict = col.OrderedDict(sorted(count_dict.items()))

	return ordered_dict

def get_prefered_neighbors(graph, starting_station, track):
	'''
	Takes graph, and a track (in progress) to a starting station. 
	Returns all neighbors from starting stations where tracks hasn't been.
	'''
	# get list of neighbors of starting station
	neighbors = [station for station in list(graph.G[starting_station])]

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

'''
makes node objects complete with their neighbors as nodes
'''
def get_node_list(G, nodes):

	node_dict = {}
	for node in nodes:
		node_dict[node] = ndc.Node(node)

	node_list = []
	for node in nodes:
		for neighbor in G[node]:
			node_dict[node].add_neighbor(node_dict[neighbor])
		node_list.append(node_dict[node])

	return node_list

'''
Removes files, checks if file exists and silently ignores error if the error is a 'no such file or directory exists'.
'''
def file_remove(path_file_name):

	try:
		os.remove(path_file_name)
	except OSError as e:
		if e.errno != errno.ENOENT:
			raise

'''
Loading bar. Two modes for faster computation of large iteration numbers. Switch sets the total iteration number where behaviour switches between modes.

1: User chooses for update every 1% or .1% (update = 100, 1000)

2: Always update every iteration. Show .1% increases.
'''
def loading_bar(iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', update = 100, switch = 100):

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

'''
Check if added track creates a track with a junction at the end.
'''
def update_hash_dict(Track, Node, edge, hash_dict):

	if len(Node.neighbors) > 2:

		key = hash(Track)
		try:
			walked_edges = hash_dict[key]
		except KeyError:
			hash_dict[key] = [edge]
	return hash_dict

'''
Always returns the first valid neighbor of a list of neighbor Nodes. Always walks forward.
'''
def get_neighbor(Node, Previous):

	for neighbor in Node.neighbors:
		if neighbor != Previous: 
			return neighbor
		elif len(Node.neighbors) == 1:
			return neighbor

'''
Checks wether a node is a junction.
'''
def is_junction(Node):

	if len(Node.neighbors) > 2:
		return True
	else:
		return False

'''
Hashes a track leading up to a junction and adds the next walked edge.
'''
def update_path(Track, path, edge):

	key = hash(Track)
	try:
		walked_edges = path[key]
		if edge not in walked_edges:
			path[key].append(edge)
	except KeyError:
		path[key] = [edge]
	return path

def update_old_path(Track, path, edge):

	key = hash(Track)
	path[key].append(edge)
	return path

'''
Returns a list of junction edges for a given track which ends in a junction Node.
'''
def junction_edges(Track, path):

	key = hash(Track)
	junction_edges = path[key]
	return junction_edges

'''
Checks neighbors of a junction Node against the previously walked Node, and all directed junction edges that can be created with the neighbors.
'''
def get_junction_neighbor(Start, Previous, junction_edges):
	
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

'''
Links two nodes. It sets the previous of the last node to the first node.
'''
def link_nodes(Start, Neighbor, key):

	Neighbor.test[key] = Start
	Start = Neighbor
	return Start

'''
Delinks two nodes. It sets the previous of the last node to 'None' and returns the node before the last node as the new start.
'''
def delink_nodes(Start, key):
	
	try:
		Previous = Start.test[key]
		del Start.test[key]
		Start = Previous
	except KeyError:
		pass
	return Start

'''' 
seperate function for generate_random_track
'''
def generate_random_track(Graph, start, max_track_length):
	
	G = Graph.G
	track = trc.track(G)
	
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

def generate_smart_random_track(Graph, start, max_track_length):

	G = Graph.G

	track = trc.track(G)	
	start = start.name

	while track.time < max_track_length:
				
		# get list of critical neighbours of starting_station
		critical_neighbors = [station for station in list(Graph.G[start]) if station in Graph.critical_station_list]
	
		prefered_neighbors = hlp.get_prefered_neighbors(Graph, start, track)

		if prefered_neighbors == []:
			random_neighbor = random.choice(list(Graph.G[start]))
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

	# make list with every station as much as they have untraversed edges
	stations_in_edges_amount_list = [elem for t in all_edge_list for elem in t]

	# initalize list for stations with only one untraversed edge
	one_edge_list = []

	# determine which stations have only one edge, adding these to one_edge_list
	counter = collections.Counter(stations_in_edges_amount_list)
	for station, count in counter.items():
		if count == 1:
			one_edge_list.append(station)

	# #make list for nodes with one edge, and the node at other end of edge is critical
	super_special = []

	# fill super special list
	for station in one_edge_list:
		if station in dict(service.all_critical_edges):
			super_special.append(station)

	# get random starting station that has only one edge with other node critical, if possible
	if super_special != []:
		current_node = random.choice(super_special)
	#else get random starting node with only one edge
	elif one_edge_list != []:
		current_node = random.choice(one_edge_list)
	# else get random starting node
	else:
		current_node = random.choice(list(graph.nodes))

	return current_node

def track_combination(service, max_track_length, graph):

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

							reversed_list = []
							partially_reversed_list = list(reversed(service.tracks[j].edges))
							for item in partially_reversed_list:
								reversed_list.append(tuple(reversed(item)))

							# make new list with edges of new track
							combined_list = reversed_list + service.tracks[i].edges
								
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
