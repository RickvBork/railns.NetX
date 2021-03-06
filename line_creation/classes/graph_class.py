import csv
import networkx as nx

'''
Graph class
Automatically fills itself upon initialisation.
Only the correct csv files and a name must be passed as arguments.
'''
class Graph:

	# init uses methods of the graph class to 'fill itself' with information
	def __init__(self, name, node_file, edge_file):
		self.name = name
		self.G = nx.Graph()

		# for more efficient lookup of edge attributes use this dict
		self.critical_edge_dict = {}
		self.edge_weight_dict = {}

		# load csv files into this specific instance of nx
		self.critical_station_list, self.non_critical_station_list = \
		self.add_csv_nodes(node_file)
		self.add_csv_edges(edge_file, self.critical_station_list)

		# force iterator object from nx to list
		self.nodes = list(self.G.nodes())
		self.edges = list(self.G.edges())
		self.critical_edge_list = self.get_critical_edges()
		self.minimal_edge_weight = min(self.get_edge_weights())
		self.total_critical_edges = len(self.critical_edge_list)

	'''
	print(Object) now returns this string, usefull for profiding short 
	descriptions
	'''
	def __str__(self):
		return "Maybe something for later..."

	'''
	Adds nodes from the csv files passed to a specific instance 
	of the graph class.
	'''
	def add_csv_nodes(self, file_name):

		with open(file_name) as csvfile:
			rows = csv.reader(csvfile)

			critical_station_list = []
			non_critical_station_list = []
			for row in rows:

				# immidiately single out stations for efficiency
				if row[3] == "Kritiek":
					critical_station_list.append(row[0])
					self.G.add_node(row[0],
						pos = (float(row[2]), float(row[1])), 
						color = 'r',
						size = 40)

				else:
					non_critical_station_list.append(row[0])
					self.G.add_node(row[0], 
						pos = (float(row[2]), float(row[1])),
						color = 'k',
						size = 10)

			return critical_station_list, non_critical_station_list

	'''
	Adds edges from the csv files passed to a specific instance 
	of the graph class.
	'''
	def add_csv_edges(self, file_name, list):

		with open(file_name) as csvfile:
			rows = csv.reader(csvfile)

			for row in rows:

				station_0 = row[0]
				station_1 = row[1]
				weight = row[2]

				# these edges are critical
				if station_0 in list or station_1 in list:
					self.G.add_edge(station_0, station_1, 
						weight = int(weight), color = 'r', visited = 'n')

					self.critical_edge_dict[(station_0, station_1)] = True

				# these edges are not critical
				else:
					self.G.add_edge(station_0, station_1, 
						weight = int(weight), color = 'k', visited = 'n')

	'''
	Get the edges from this specific instance of the graph class
	'''
	def get_critical_edges(self):
		critical_dict = nx.get_edge_attributes(self.G, 'color')
		return [edge for edge in critical_dict if critical_dict[edge] == 'r']

	'''
	Get the edges weights from this specific instance of the graph class
	'''
	def get_edge_weights(self):
		edges = self.G.edges()
		weight_dict = nx.get_edge_attributes(self.G,'weight')
		return [weight_dict[edge] for edge in edges]

	'''
	Build critical edge dict for better search functionality
	'''
