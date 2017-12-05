class Track(object):

	def __init__(self, G):
		self.G = G
		self.edges = []
		self.time = 0
		self.critical = 0

	# add edges as tuples
	def add_edge(self, from_node, to_node):
		self.edges.append((from_node, to_node))

		self.time += self.G[from_node][to_node]['weight']

		if self.G[from_node][to_node]['color'] == 'r':
			self.critical += 1

	# remove last item in list to make new track for walkback
	def remove_edge(self):
		edge = self.edges.pop()
		self.time -= self.G[edge[0]][edge[1]]['weight']

	def get_score(self):
		return 10000 * (self.critical / 20) - (20 + self.time / 100000)