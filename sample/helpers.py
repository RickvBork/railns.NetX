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
		'''
		determine critical connections and make list
		'''
		"""critical_lines = 0
		critical_connections = []
		for v in G:
			print(v)
		   	for w in G[v]:
		    	print(w)
		        vid = v
		        wid = w
		        #print(w)
		        #print(wid)
		
		        # check wether station name is critical
		        if vid in critical_stations and [vid, wid] not in critical_connections and [wid, vid] not in critical_connections:
		
		            # for every neighbour, add 1 critical line
		            for n in G[vid]:
		                critical_lines += 1
		            print('( %s , %s, %3d), CRITICAL'  % ( vid, wid, G[v][w]['weight']))
		            # add connection in list in both directions
		            critical_connections.append([vid,wid,])
				"""
	#def hierholzer(self):
	#a directed graph has an Eulerian cycle if following conditions are true (1) All vertices with nonzero degree belong to a single strongly connected component. (2) In degree and out degree of every vertex is same. The algorithm assumes that the given graph has Eulerian Circuit.

#Choose any starting vertex v, and follow a trail of edges from that vertex until returning to v. It is not possible to get stuck at any vertex other than v, because indegree and outdegree of every vertex must be same, when the trail enters another vertex w there must be an unused edge leaving w.
#The tour formed in this way is a closed tour, but may not cover all the vertices and edges of the initial graph.
#As long as there exists a vertex u that belongs to the current tour but that has adjacent edges not part of the tour, start another trail from u, following unused edges until returning to u, and join the tour formed in this way to the previous tour.
#Thus the idea is to keep following unused edges and removing them until we get stuck. Once we get stuck, we back-track to the nearest vertex in our current path that has unused edges, and we repeat the process until all the edges have been used. We can use another container to maintain the final path.
