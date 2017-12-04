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

	def previous(self, Node):
		self.previous = Node