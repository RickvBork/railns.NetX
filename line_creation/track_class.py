'''
@author Team Stellar Heuristiek
'''
import line_graph_class as grc

class track:
	def __init__(self, stations, graph):
		
		self.critical_edge_list = graph.critical_edge_list
		self.starting_station = stations[0][0]
		self.last_station = stations[-1][1]
		route = []
		for stationpair in stations:
			route.append(stationpair[0])
		route.append(stations[-1][1])
		print(route)

	def get_critical_lines(self, route):
		print(critical_edge_list)

