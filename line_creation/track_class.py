'''
@author Team Stellar Heuristiek
'''
import line_graph_class as grc

class track:
	def __init__(self, stations, graph):

		self.G = graph.G
		self.critical_edge_list = graph.critical_edge_list
		self.starting_station = stations[0][0]
		self.last_station = stations[-1][1]

		# AANPASSEN TOT LIJST MET EDGES!
		self.edges = self.get_edges_list(stations)	
		self.critical_lines_traversed = self.get_critical_lines_traversed()	
		self.time = self.get_time()
	
	def get_time(self):
		time = 0
		for i in range(len(self.edges)-1):
			time += self.G[self.edges[i]][self.edges[i+1]]['weight']
		return time
 
	def get_edges_list(self, stations):
		edges = []
		for stationpair in stations:
			edges.append(stationpair[0])
		edges.append(stations[-1][1])
		return edges


	def get_critical_lines_traversed(self):
		critical_lines_traversed = []
		edges = self.edges
		for i in range(len(edges)-1):
			if ((edges[i], edges[i+1]) in self.critical_edge_list):
				critical_lines_traversed.append((edges[i], edges[i+1]))
				#print("add critical line traversed")
		return critical_lines_traversed
