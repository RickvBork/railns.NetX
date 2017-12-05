# Test class for nodes
class Node(object):
	def __init__(self, name, Node):
		self.name = name
		self.neighbors = []
		self.visited = 'n'
		self.previous = Node

	def add_neighbor(self, Node):
		self.neighbors.append(Node)

	def walked(self):
		self.visited = 'y'

	def check_neighbors(self, total_time, G):

		print('\n_______________Enter Check_______________\n')

		print('Check neighbors for: ' + self.name)
		print('Total time is: ' + str(total_time) + '\n')

		print('Possible Neighbors:')
		for neighbor in self.neighbors:
			print(neighbor.name)

		for neighbor in self.neighbors:

			if neighbor.visited == 'n':
				if G[neighbor.name][self.name]['weight'] + total_time <= 120:
					print('Edge: ' + self.name + ' -> ' + neighbor.name)
					print('Old Total Time: ' + str(total_time))
					print('Edge Time:\t' + str(G[neighbor.name][self.name]['weight']))
					print(str(G[neighbor.name][self.name]['weight'] + total_time))
					return neighbor
		return False