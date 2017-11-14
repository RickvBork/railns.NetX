import csv
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

'''
Graph class, mostly storage for functions. Can later be turned into a init Class,
storing multiple graphs from multiple csv files.
'''
class Graph:

	'''
	Adds nodes with node attributes to the graph from a formatted csv file.
	For optimization purposes, a critical node list is also created.
	'''
	def add_csv_nodes(file_name):

			with open(file_name) as csvfile:
			    rows = csv.reader(csvfile)

			    critical_station_list = []
			    for row in rows:

			    	if row[3] == "Kritiek":
			    		critical_station_list.append(row[0])
			    		G.add_node(row[0],
			    			pos = (float(row[2]), float(row[1])), 
			    			color = 'r',
			    			size = 40)

			    	else:
			    		G.add_node(row[0], 
			    			pos = (float(row[2]), float(row[1])),
			    			color = 'k',
			    			size = 10)

			    return critical_station_list

	'''
	Adds the edges and attributes to the graph from a formatted csv file.
	'''
	def add_csv_edges(file_name, list):

		with open(file_name) as csvfile:
			rows = csv.reader(csvfile)

			for row in rows:
				if row[0] in list and row[1] in list:
					print('AAA' + row[0], row[1])
					G.add_edge(row[0], row[1], weight = int(row[2]), color = 'r')

				elif row[0] in list or row[1] in list:
					print('BBB' + row[0], row[1])
					G.add_edge(row[0], row[1], weight = int(row[2]), color = 'r')

				else:
					G.add_edge(row[0], row[1], weight = int(row[2]), color = 'k')

	'''
	Draws this instance of the graph. If an init is also implemented, multiple Graphs
	can be stored and drawn.
	'''
	def draw_graph():

		# get positions of nodes and edges
		pos = nx.get_node_attributes(G, 'pos')

		# make node color map and node size maps for draw function
		node_color_map = []
		node_size_map = []
		for node in G.nodes():
			node_color_map.append(nx.get_node_attributes(G, 'color')[node])
			node_size_map.append(nx.get_node_attributes(G, 'size')[node])

		# list comprehension to get edge color map
		edge_color_map = [nx.get_edge_attributes(G,'color')[edge] for edge in G.edges()]

		# draw everything except labels and show plot
		nx.draw_networkx(G, pos, node_color = node_color_map, node_size = node_size_map, edge_color = edge_color_map, with_labels = False)
		plt.show()


	def random_walk(self):
		print('BRUTE FROCE!!!')
