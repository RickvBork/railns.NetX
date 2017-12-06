'''
service class models service (nl: 'lijnvoering') consisting of several tracks
argument to construct service is a graph as defined in line_graph_class.py
tracks are added seperately using add_track(self, track)
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
		self.p_score = self.get_p_score()
		self.s_score = self.get_s_score()

	def update_critical_edges_traversed(self, track):
		for i in range(len(track.edges)-1):
			if (((track.edges[i],track.edges[i+1]) in self.all_critical_edges) or ((track.edges[i+1],track.edges[i]) in self.all_critical_edges)):
				if (((track.edges[i],track.edges[i+1]) not in self.critical_edges_traversed) and ((track.edges[i+1],track.edges[i]) not in self.critical_edges_traversed)):
					self.critical_edges_traversed.append((track.edges[i],track.edges[i+1]))
		
	def update_all_edges_traversed(self, track):
		for i in range(len(track.edges)-1):
			if (((track.edges[i],track.edges[i+1]) not in self.all_edges_traversed) and ((track.edges[i+1],track.edges[i]) not in self.all_edges_traversed)):
					self.all_edges_traversed.append((track.edges[i],track.edges[i+1]))
		
	
	def get_p_score(self):
		p_score = (float(len(self.critical_edges_traversed))/float(len(self.all_critical_edges)))
		return p_score

	def get_s_score(self):
		p_score = self.p_score
		s_score = (10000 * p_score - (float(len(self.tracks))*20 + float(self.time) / 100000)) 
		return s_score

	def remove_track(self, track):
		self.tracks.remove(track)
		self.update_critical_edges_traversed_remove(track)
		self.update_all_edges_traversed_remove(track)	
		self.time -= track.time
		# update scores
		self.p_score = self.get_p_score()
		self.s_score = self.get_s_score()
	
	def update_critical_edges_traversed_remove(self, track):
		self.critical_edges_traversed = []
		for track in self.tracks:
			update_critical_edges_traversed(track)

	def update_all_edges_traversed_remove(self, track):
		self.all_edges_traversed = []
		for track in self.tracks:
			update_all_edges_traversed(track
)
