import helpers as hlp

'''
service class models service (nl: 'lijnvoering') consisting of several tracks
argument to construct service is a graph as defined in line_graph_class.py
tracks are added seperately using add_track(self, track)
track is object as defined in track_class.py
'''

class service:
	def __init__(self, Graph):
		self.tracks = []

		# OPTIMALISATIE! GEEN GRAAF! PASSEER ALLEEN critical edge list als arg
		self.G = Graph.G

		# Een int te geven? Want meer is niet nodig voor score
		# self.all_critical_edges = graph_c.critical_edge_list

		self.all_critical_edges = Graph.critical_edge_list
		self.critical_edges_traversed = []
		self.all_edges_traversed = []
		self.time = 0
		self.p_score = 0
		self.s_score = 0

	def add_track(self, track):
		self.tracks.append(track)
		self.update_critical_edges_traversed(track)
		self.update_all_edges_traversed(track)	
		self.time = self.time + track.time
		# update scores
		self.p_score = hlp.get_p(self.critical_edges_traversed, self.all_critical_edges)
		self.s_score = hlp.get_score(self.p_score, len(self.tracks),self.time)

	def update_critical_edges_traversed(self, track):
		for edge in track.edges:
			station_0 = edge[0]
			station_1 = edge[1]

			# OUDE VERSIE
			edge_reversed = (station_1, station_0)
			# if (edge in self.all_critical_edges or edge_reversed in self.all_critical_edges):

			# AANPASSING (track.G[x][y]['color'] is hetzelfde...)
			if self.G[station_0][station_1]['color'] == 'r':
				if (edge not in self.critical_edges_traversed) and (edge_reversed not in self.critical_edges_traversed):
					self.critical_edges_traversed.append(edge)

	def update_all_edges_traversed(self, track):
		for edge in track.edges:
			station0 = edge[0]
			station1 = edge[1]
			edge_reversed = (station1, station0)
			if (edge not in self.all_edges_traversed and edge_reversed not in self.all_edges_traversed):
					self.all_edges_traversed.append(edge)

	def remove_track(self, track):
		self.tracks.remove(track)
		self.update_critical_edges_traversed_remove(track)
		self.update_all_edges_traversed_remove(track)	
		self.time -= track.time
		# update scores
		self.p_score = hlp.get_p(self.critical_edges_traversed, self.all_critical_edges)
		self.s_score = hlp.get_score(self.p_score, len(self.tracks),self.time)
	
	def update_critical_edges_traversed_remove(self, track):
		self.critical_edges_traversed = []
		for track in self.tracks:
			self.update_critical_edges_traversed(track)

	def update_all_edges_traversed_remove(self, track):
		self.all_edges_traversed = []
		for track in self.tracks:
			self.update_all_edges_traversed(track
)
