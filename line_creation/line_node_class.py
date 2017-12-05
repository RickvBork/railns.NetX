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

	def check_neighbors(self, track, G):

		print('\n_______________Enter Check_______________\n')

		print('Check neighbors for: ' + self.name)
		print('Total time is: ' + str(track.time) + '\n')

		print('Possible Neighbors:')
		for neighbor in self.neighbors:

			# check surroundings, but not the node walked from and node already walked to
			if neighbor != self.next and neighbor != self.previous:

				print(neighbor.name)

				# only take nodes that have valid travel time
				if G[neighbor.name][self.name]['weight'] + track.time <= 120:
					print('Edge: ' + self.name + ' -> ' + neighbor.name)
					print('Old Total Time: ' + str(track.time))
					print('Edge Time:\t' + str(G[neighbor.name][self.name]['weight']))
					print(str(G[neighbor.name][self.name]['weight'] + track.time))

					# edge from -> to, also stored this way in edges
					edge = (self.name, neighbor.name)

					# check track if the edge has not been travelled
					if edge not in track.edges:
						return neighbor

		# no possible neighbor, continue walkback
		return False


			# if neighbor.visited == 'n':
			# 	if G[neighbor.name][self.name]['weight'] + total_time <= 120:
			# 		print('Edge: ' + self.name + ' -> ' + neighbor.name)
			# 		print('Old Total Time: ' + str(total_time))
			# 		print('Edge Time:\t' + str(G[neighbor.name][self.name]['weight']))
			# 		print(str(G[neighbor.name][self.name]['weight'] + total_time))
			# 		return neighbor
		return False