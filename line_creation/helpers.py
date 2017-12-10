import collections as col
import line_node_class as N
import os, errno

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

def get_prefered_neighbors(graph, starting_station, all_connections, track):
	# get list of neighbors of starting station
	neighbors = [station for station in list(graph.G[starting_station])]
	# get list of  critical neighbors of starting_station
	critical_neighbors = [station for station in list(graph.G[starting_station]) if station in graph.critical_station_list]

	for i in range(track + 1):
		print(all_connections['tracks'][str(i)])
	print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
	prefered_neighbors = list(neighbors)
	for i in range(track + 1):	
		for neighbor in neighbors:
			if ((starting_station, neighbor) in all_connections['tracks'][str(i)] or (starting_station, neighbor) in all_connections['tracks'][str(i)]):
				#print(starting_station, neighbor)
				if neighbor in prefered_neighbors:
					prefered_neighbors.remove(neighbor)
					
	print(prefered_neighbors)
	
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
		node_dict[node] = N.Node(node)

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

