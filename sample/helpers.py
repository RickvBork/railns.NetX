import csv
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

class Graph:

	def add_csv_nodes(file_name):

			with open(file_name) as csvfile:
			    rows = csv.reader(csvfile)

			    cs = []
			    for row in rows:

			    	if row[3] == "Kritiek":
			    		cs.append(row[0])
			    		G.add_node(row[0], pos = (float(row[2]), float(row[1])), label = str(row[0]), critical = True)

			    	else:
			    		G.add_node(row[0], pos = (float(row[2]), float(row[1])), label = str(row[0]))

			    return cs

	def add_csv_edges(file_name, list):

		with open(file_name) as csvfile:
			rows = csv.reader(csvfile)

			for row in rows:
				if row[0] and row[1] in list:
					G.add_edge(row[0], row[1], weight = int(row[2]))

				elif row[0] or row[1] in list:
					G.add_edge(row[0], row[1], weight = int(row[2]))

				else:
					G.add_edge(row[0], row[1], weight = int(row[2]))

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
