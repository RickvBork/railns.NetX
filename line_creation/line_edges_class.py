class Edges(object):

	def __init__(self, G):
		self.G = G
		self.edges = []
		self.time = 0
		self.critical = 0

	# add edges as tuples
	def add_edge(self, edge):
		self.edges.append(edge)

		if self.G[edge[0]][edge[1]]['color'] == 'r':
			self.critical += 1

	def remove_edge(self):
		self.edges.pop(0)

	def get_score(self):
		return 10000 * (self.critical / 20) - (20 + self.time / 100000)
