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
		print('BRUTE FROCE!!!')
