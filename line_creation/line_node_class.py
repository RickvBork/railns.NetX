# Test class for nodes
class Node(object):
	def __init__(self, name):
		self.name = name
		self.neighbors = []
		self.visited = 'n'
		self.previous = Node
		self.next = None

	def __ne__(self, other):
		try:
			print(self.name, other.name)

		except ValueError:
			print('Not defined:{}'.format(other.name))

	def add_neighbor(self, Node):
		self.neighbors.append(Node)

	def walked(self):
		self.visited = 'y'

	# def check_neighbors(self, track, track_list, G):

	# 	print('\n__________________Enter Check__________________\n')

	# 	print('Checking for Node:\t' + self.name)

	# 	# take length of the track
	# 	track_length = len(track.edges)
	# 	pathfinder_edges = []

	# 	print('Test Track\n')
	# 	print(track.edges)
	# 	print()

	# 	# for every track already made
	# 	print('Built Tracks:\n')
	# 	for unique_track in track_list:

	# 		print(unique_track.edges)

	# 		# take the same length as the current track
	# 		test_track = unique_track.edges[0: track_length]

	# 		# if this equals the current track
	# 		if test_track == track.edges:

	# 			edge = unique_track.edges[track_length]

	# 			if edge not in pathfinder_edges:
	# 				pathfinder_edges.append(edge)

	# 	print('\nNeglect edges:\n{}'.format(pathfinder_edges))

	# 	# loop over all neighbors of the from node
	# 	for edge in pathfinder_edges:

	# 		print('Neglect edge:{}'.format(edge))

	# 		for neighbor in self.neighbors:

	# 			print('Edge:\t\t\t(\'{}\', \'{}\')'.format(self.name, neighbor.name))
	# 			print('Old Total Time:\t\t' + str(track.time))
	# 			print('Edge Time:\t\t{}'.format(G[neighbor.name][self.name]['weight']))
	# 			print('Total Time:\t\t{}\n'.format(G[neighbor.name][self.name]['weight'] + track.time))

	# 			# if the edge does not force total time over limit, and not equal to the node previous to the from node
	# 			if neighbor != self.previous and G[self.name][neighbor.name]['weight'] + track.time <= 120:

	# 				# if the edge is not equal to the pathfinder edge
	# 				if (self.name, neighbor.name) != edge:
	# 					print('test')
	# 					return neighbor
	# 	return False