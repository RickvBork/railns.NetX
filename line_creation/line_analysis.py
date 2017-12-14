import networkx as nx
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import helpers as hlp
import os

'''
Draws this instance of the graph. If an init is also implemented, multiple Graphs can be stored and drawn.

If a service object is passed, then the individual tracks will be saved to plots.
'''
def draw_graph(Graph, service = None):

	nodes = Graph.nodes
	edges = Graph.edges
	G = Graph.G

	# get positions of nodes and edges
	pos = nx.get_node_attributes(G, 'pos')

	if service == None:
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

	else:

		os.chdir("..") # moves up one directory
		style = ['dashed', 'dotted', 'dashdot']
		color = ['r', 'b', 'g', 'y']
		color_length = len(color)
		style_length = len(style)

		i = 0
		print('Writing files...')
		for track in service.tracks:
			nx.draw(G, pos, node_size = 40, node_color = 'k')
			nx.draw_networkx_edges(G, pos, edgelist = track.edges, edge_color = color[i % color_length], style = style[i % style_length], width = 5, arrows = True)
			plt.savefig('visualization/plots/track_' + str(i) + '.png')
			plt.clf()
			i += 1

		# removes old track files, 20 being the max track number
		for i in range(i, 21):
			file = 'visualization/plots/track_' + str(i) + '.png'
			hlp.file_remove(file)
		os.chdir('line_creation') # moves back to line_creation
		print('Done')

def draw_barchart(scores):

	minimum = min(scores)
	maximum = max(scores)

	counter = 0

	# sums everything smaller than or equal to next bar value
	# SET interval to something relating to data!
	if minimum >= 0.0 and maximum <= 1.0:

		objects = tuple([str(i) for i in np.arange(0.0, 1.05, 0.05)])
		categories = [int(i * 100) / 100.0 for i in np.arange(0.0, 1.05, 0.05)]
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

def draw_barchart_hierholzer(scores):

	minimum = min(scores)
	maximum = max(scores)

	counter = 0

	# sums everything smaller than or equal to next bar value
	# SET interval to something relating to data!
	if minimum >= 0.0 and maximum <= 1.0:

		objects = tuple([str(i) for i in np.arange(0.0, 1.05, 0.05)])
		categories = [int(i * 100) / 100.0 for i in np.arange(0.0, 1.05, 0.05)]
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