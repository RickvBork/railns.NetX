# Test class for nodes
class Node(object):
	def __init__(self, name, Node):
		self.name = name
		self.neighbors = []
		self.visited = 'n'
		self.previous = Node
		self.next = None

	def add_neighbor(self, Node):
		self.neighbors.append(Node)

	def walked(self):
		self.visited = 'y'

	def check_neighbors(self, track, track_list, G):

		print('\n__________________Enter Check__________________\n')

		print('Checking for Node:\t' + self.name)

		print('\nExisting tracks: ')
		for obj in track_list:
			print(obj.edges)
			print()

		print('Current track')
		print('{}'.format(track.edges))

		slice0 = len(track.edges)

		# from all tracks, seek the pathfinder edge
		for unique_track in track_list:

			slice1 = len(unique_track.edges)

			# slice off the track from unique strack, get first edge
			edge = unique_track.edges[slice0:slice1][0]

			print('Neglect edge:\t\t{}'.format(edge))

			# loop over all neighbors of the from node
			for neighbor in self.neighbors:

				print('Edge:\t\t\t(\'{}\', \'{}\')'.format(self.name, neighbor.name))
				print('Old Total Time:\t\t' + str(track.time))
				print('Edge Time:\t\t{}'.format(G[neighbor.name][self.name]['weight']))
				print('Total Time:\t\t{}\n'.format(G[neighbor.name][self.name]['weight'] + track.time))

				# if the edge does not force total time over limit, and not equal to the node previous to the from node
				if neighbor != self.previous and G[self.name][neighbor.name]['weight'] + track.time <= 120:

					# if the edge is not equal to the pathfinder edge
					if (self.name, neighbor.name) != edge:
						print('test')
						return neighbor
		return False