'''
@author Team Stellar Heuristiek
'''
import line_graph_class as grc

class track:
	def __init__(self, graph):

		self.G = graph.G
		self.critical_edge_list = graph.critical_edge_list
		self.edges = []	
		self.critical_lines_traversed = []	
		self.time = 0
		self.stations = []

	def add_whole_track(self, stations):
		self.edges = []
		for stationpair in stations:
			self.edges.append(stationpair)
		self.update_time()
		self.update_critical_lines_traversed()

	def add_edge(self, edge):
		# edge = ('station a', 'station b')
		# check if current last station is starting point of new edge since trains cannot teleport
		if self.edges != []:
			current_last_station = self.edges[-1][1]
			if current_last_station == edge[0]:
				self.edges.append(edge)	
				self.update_time()
				self.update_critical_lines_traversed()
			else:
				print("cannot depart from station other then the current station")
		else:
			self.edges.append(edge)	
			self.update_time()
			self.update_critical_lines_traversed()

	def add_edge_list(self, edge_list):
		self.edges = edge_list

	def remove_edge(self):
		self.edges = self.edges[:-1]
		self.update_time()
		self.update_critical_lines_traversed()
			
		
	def update_time(self):
		self.time = 0
		for edge in self.edges:
			station0 = edge[0]
			station1 = edge[1]
			self.time += self.G[station0][station1]['weight']
	
	def update_critical_lines_traversed(self):
		edges = self.edges
		for edge in edges:
			station0 = edge[0]
			station1 = edge[1]
			edge_reversed = (station1, station0)
			if (edge in self.critical_edge_list or edge_reversed in self.critical_edge_list):
				if (edge not in self.critical_lines_traversed and edge_reversed not in self.critical_lines_traversed):
					self.critical_lines_traversed.append(edge)
					#print("add critical line traversed")
	
	def add_station(self, from_node, to_node):

		if from_node not in self.stations:
			self.stations.append(from_node)
			
		if to_node not in self.stations:
			self.stations.append(to_node)