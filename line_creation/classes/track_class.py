'''
@Author Team Stellar Heuristiek
'''
class track:
	'''
	Track class models a track, i.e. a single train riding between station on a networkx graph.
	Edges as well as critical edges that are traversed are stored in list.
	'''
	def __init__(self, G):

		self.G = G
		self.edges = []	
		self.critical_lines_traversed = []	
		self.time = 0
		self.stations = []
		self.necessary = True
		self.time = self.get_time()

	# hashes a track for quick lookup
	def __hash__(self):
		if self.edges:
			return hash(tuple(self.edges))
		else:
			return 1

	def get_time(self):
		time = 0
		for i in range(len(self.edges)-1):
			time += self.G[self.edges[i]][self.edges[i+1]]['weight']
		return time

	def get_edges_list(self, stations):
		edges = []

	def add_whole_track(self, stations):
		self.edges = []
		for stationpair in stations:
			self.edges.append(stationpair)
		self.update_time()
		self.update_critical_lines_traversed()

	def add_edge(self, edge):
		# check if current last station is starting point of new edge since trains cannot teleport
		if self.edges != []:
			# check if departing station is indeed the station where the train is 
			current_last_station = self.edges[-1][1]
			if current_last_station == edge[0]:
				self.edges.append(edge)	
				self.update_time()
				self.update_critical_lines_traversed()
			else:
				print("Error, cannot depart from station where train is located")
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
			
	def remove_all_edges(self):
		self.edges = []

	def update_time(self):
		self.time = 0
		for edge in self.edges:
			station0 = edge[0]
			station1 = edge[1]
			self.time += self.G[station0][station1]['weight']
	
	def update_critical_lines_traversed(self):
		edges = self.edges
		for edge in edges:
			station_0 = edge[0]
			station_1 = edge[1]
			edge_reversed = (station_1, station_0)
			# Check if station is critical 
			if self.G[station_0][station_1]['color'] == 'r':
				# check if line is already in critical_lines_traversed, if not, add edge to critical_lines_traversed
				if (edge not in self.critical_lines_traversed and edge_reversed not in self.critical_lines_traversed):
					self.critical_lines_traversed.append(edge)
	
	def add_station(self, from_node, to_node):

		if from_node not in self.stations:
			self.stations.append(from_node)
			
		if to_node not in self.stations:
			self.stations.append(to_node)
