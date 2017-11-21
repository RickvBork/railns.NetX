import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

'''
Draws this instance of the graph. If an init is also implemented, multiple Graphs
can be stored and drawn.
'''
def draw_graph(Graph):

	nodes = Graph.nodes
	edges = Graph.edges
	G = Graph.G

	print(edges)

	# get positions of nodes and edges
	pos = nx.get_node_attributes(G, 'pos')

	# make node color map and node size maps for draw function
	node_color_map = []
	node_size_map = []

	# make node color maps and size maps
	for node in nodes:
		node_color_map.append(nx.get_node_attributes(G, 'color')[node])
		node_size_map.append(nx.get_node_attributes(G, 'size')[node])

	# list comprehension to get edge color map
	edge_color_map = [nx.get_edge_attributes(G,'color')[edge] for edge in G.edges()]

	# draw everything except labels and show plot
	nx.draw_networkx(G, pos, node_color = node_color_map, node_size = node_size_map, edge_color = edge_color_map, with_labels = False)

	# show plot
	plt.show()

def draw_p_barchart(scores):
	#list = [element for element in scores if element <= 0.5]
	#print(list)
	list = []
	objects = ("0.1","0.2","0.3","0.4","0.5","0.6","0.7","0.8","0.9","1.0")
	counter = 0
	categories = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
	number_of_categories = len(categories)	
	performance = []
	for i in range(number_of_categories):
		list = [element for element in scores if element >= categories[counter] and element < categories[counter + 1]]
		performance.append(len(list))
		counter += 1
		
	#print(performance)
	#print(scores)
	y_pos = np.arange(len(objects))
	#y_pos = np.arange(9)
	#y_pos = categories
	#performance = [10,8,6,4,2,1]
	 
	plt.bar(y_pos, performance, align = 'center', alpha = 0.5)
	plt.xticks(y_pos, objects)
	plt.ylabel('Frequency')
	plt.xlabel('Score')
	plt.title('Scores')
	 
	plt.show()