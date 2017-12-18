# Test class for nodes
class Node(object):
	def __init__(self, name):
		self.name = name
		self.neighbors = []
		self.previous = None
		self.test = {}
		self.next = None
		self.junction = False

	def __ne__(self, other):
		
		try:
			# print('Unequal:\t{} != {} = {}'.format(self.name, other.name, 
			# self.name != other.name))
			return self.name != other.name
		except AttributeError:

			# start node has None as previous which has no name attribute
			return True

	def add_neighbor(self, Node):
		self.neighbors.append(Node)