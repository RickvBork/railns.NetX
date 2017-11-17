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
		self.critical_station_list = self.add_csv_nodes(node_file)
		self.add_csv_edges(edge_file, self.critical_station_list)
		self.data_lists = self.spit_data_lists()
		self.nodes = self.data_lists[0]
		self.critical_edge_list = self.data_lists[1]
		self.min_edge_weight = self.data_lists[2]

	'''
	Adds nodes from the csv files passed to a specific instance 
	of the graph class.
	'''
	def add_csv_nodes(self, file_name):

			with open(file_name) as csvfile:
			    rows = csv.reader(csvfile)

			    critical_station_list = []
			    for row in rows:

			    	# immidiately single out stations for efficiency
			    	if row[3] == "Kritiek":
			    		critical_station_list.append(row[0])
			    		self.G.add_node(row[0],
			    			pos = (float(row[2]), float(row[1])), 
			    			color = 'r',
			    			size = 40)

			    	else:
			    		self.G.add_node(row[0], 
			    			pos = (float(row[2]), float(row[1])),
			    			color = 'k',
			    			size = 10)

			    return critical_station_list

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

				if station_0 in list and station_1 in list:
					self.G.add_edge(station_0, station_1, 
						weight = int(weight), color = 'r')

				elif station_0 in list or station_1 in list:
					self.G.add_edge(station_0, station_1, 
						weight = int(weight), color = 'r')

				else:
					self.G.add_edge(station_0, station_1, 
						weight = int(weight), color = 'k')

	'''
	Retrieves valuable data from the edges and nodes for a specific
	instance of the graph class.
	'''
	def spit_data_lists(self):
		
		# set datas
		nodes = self.G.nodes()
		edges = self.G.edges()
		weight_dict = nx.get_edge_attributes(self.G,'weight')
		critical_dict = nx.get_edge_attributes(self.G, 'color')

		# make nodelist
		node_list = [node for node in nodes]

		# seek minimum weight
		edge_weight_list = [weight_dict[edge] for edge in edges]

		# seek minimum weight
		min_edge_weight = min(edge_weight_list)

		# make unique critical edge list
		critical_edge_list = [edge for edge in critical_dict if critical_dict[edge] == 'r']

		# seek total critical edge time
		critical_edge_weight_list = [weight_dict[edge] for edge in critical_edge_list]


		# return values
		return [node_list, critical_edge_list, min_edge_weight]