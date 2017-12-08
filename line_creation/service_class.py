import helpers as hlp

'''
service class models service (nl: 'lijnvoering') consisting of several tracks
argument to construct service is a graph as defined in line_graph_class.py
tracks are added seperately using add_track(self, track)
track is object as defined in track_class.py
'''

class service:
	def __init__(self, graph_c):
		self.tracks = []
		self.graph = graph_c
		self.all_critical_edges = graph_c.critical_edge_list 
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
		for i in range(len(track.edges)-1):
			if (((track.edges[i],track.edges[i+1]) in self.all_critical_edges) or ((track.edges[i+1],track.edges[i]) in self.all_critical_edges)):
				if (((track.edges[i],track.edges[i+1]) not in self.critical_edges_traversed) and ((track.edges[i+1],track.edges[i]) not in self.critical_edges_traversed)):
					self.critical_edges_traversed.append((track.edges[i],track.edges[i+1]))
		
	def update_all_edges_traversed(self, track):
		for i in range(len(track.edges)-1):
			if (((track.edges[i],track.edges[i+1]) not in self.all_edges_traversed) and ((track.edges[i+1],track.edges[i]) not in self.all_edges_traversed)):
					self.all_edges_traversed.append((track.edges[i],track.edges[i+1]))

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
