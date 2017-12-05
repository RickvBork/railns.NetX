'''
@author Team Stellar Heuristiek
'''
import line_graph_class as grc

class track:
	def __init__(self, stations, graph):
		
		self.critical_edge_list = graph.critical_edge_list
		self.starting_station = stations[0][0]
		self.last_station = stations[-1][1]
		self.route = self.get_route_list(stations)	
		self.critical_lines_traversed = self.get_critical_lines_traversed()	

	def get_route_list(self, stations):
		route = []
		for stationpair in stations:
			route.append(stationpair[0])
		route.append(stations[-1][1])
		return route


	def get_critical_lines_traversed(self):
		critical_lines_traversed = []
		route = self.route
		for i in range(len(route)-1):
			if ((route[i], route[i+1]) in self.critical_edge_list):
				critical_lines_traversed.append((route[i], route[i+1]))
				print("add critical line traversed")
		return critical_lines_traversed
