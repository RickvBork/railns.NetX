import networkx as nx
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import helpers as hlp

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
	nx.draw_networkx(G, pos, node_color = node_color_map, node_size = node_size_map, edge_color = edge_color_map, with_labels = True)

	# show plot
	plt.show()

def draw_barchart(scores):

	print(hlp.ordered_counter(scores))

	minimum = min(scores)
	maximum = max(scores)

	counter = 0

	# sums everything smaller than or equal to next bar value
	if minimum >= 0.0 and maximum <= 1.0:

		# optimalization possible... (0, 0.1, ..., 1.0)
		# 1.2 as the structure broke when scores of 1.0 where encountered, the list must count to 1.1 (range(x, 1.2, x))
		objects = tuple([str(i) for i in np.arange(0.0, 1.2, 0.1)])
		categories = [i for i in np.arange(0.0, 1.2, 0.1)]
	else:
		objects = tuple([str(i) for i in range(-500, 11000, 500)])
		categories = [i for i in range(-500, 11000, 500)]

	number_of_categories = len(categories)
	performance = []
	for i in range(number_of_categories):
		list = [score for score in scores if score >= categories[counter] and score < categories[counter + 1]]
		performance.append(len(list))
		counter += 1

	y_pos = np.arange(len(objects))

	plt.bar(y_pos, performance, align='center', alpha=0.5)
	plt.xticks(y_pos, objects)
	plt.ylabel('Frequency')
	plt.xlabel('Score')
	plt.title('Scores')

	plt.show()