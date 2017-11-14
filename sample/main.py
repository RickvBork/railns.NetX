'''
main.py
@author Team Stellar Heuristiek
'''

# import the helpers file
import helpers
import barchart
import csv

# initialise graph class
Graph = helpers.Graph


# initialize path files
path_stations_file = '../data/StationsHolland.csv'
path_tracks_file = '../data/ConnectiesHolland.csv'

# OTHER WAY TO GET CRITICAL LIST?
critical_stations = Graph.add_csv_nodes(path_stations_file)

Graph.add_csv_edges(path_tracks_file, critical_stations)

nodelist, critical_edge_list, minimum_edge_weight = Graph.spit_data_lists()

scores = []
for i in range(500):
	score, S10 = Graph.random_walk(nodelist, minimum_edge_weight, critical_edge_list)
	print("score")
	print(S10)
	scores.append(score)
print("scoress:")
print(scores)
print("average:")
print(sum(scores)/len(scores))

# write scores to csv
# ref: https://stackoverflow.com/questions/39282516/python-list-to-csv-throws-error-iterable-expected-not-numpy-int64
# ref: https://docs.python.org/3/library/csv.html
with open('../data/results.csv', 'w', newline='') as myfile:
	wr = csv.writer(myfile,delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	wr.writerows(map(lambda x: [x], scores))

#make bar chart of scores
barchart.draw(scores)

#testing
# nodelist, critical_edge_list, min_edge_weight = spit_data_list(nodelist, critical_edge_list, min_edge_weight)
# print(critical_edge_list)
# print('hoi')
